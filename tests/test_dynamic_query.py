import os

from flip_rpc_client import Client, DynamicQuery


def get_client():
    api_key = os.environ.get("FLIP_API_KEY")
    if not api_key:
        raise Exception("Missing environment variable: `FLIP_API_KEY`")

    base_url = os.environ.get("FLIP_BASE_URL")
    if not base_url:
        raise Exception("Missing environment variable: `FLIP_BASE_URL`")
    
    return Client(api_key, base_url)


def make_query():
    return {
        "table": "udm_events_aion",
        "schema": "source",
        "aggregates": [
          {
            "field": "event_amount",
            "label": "total_amount",
            "decimal_adjustment": 16,
            "operation": "sum"
          }
        ],
        "group_by": [
          {
            "field": "block_timestamp",
            "timebucket": "1 day",
            "label": "metric_date"
          }
        ],
        "order_by": [
          {
            "label": "metric_date",
            "direction": "DESC"
          }
        ],
        "filter": {
          "and": [
            {
              "gte": {
                "field": "block_timestamp",
                "value": "2020-05-25"
              }
            },
            {
              "in_segment": {
                "field": "event_to",
                "value": "small_exchange_accounts"
              }
            }
          ]
        },
        "segments": {
          "small_exchange_accounts": {
            "and": [
              {
                "and": [
                  {
                    "gte": {
                      "partition_id": "sorted_set:ad43bf8e-0f0c-4102-be91-52bc84150af2:current_balances:flipside",
                      "value": 50
                    }
                  },
                  {
                    "lte": {
                      "partition_id": "sorted_set:ad43bf8e-0f0c-4102-be91-52bc84150af2:current_balances:flipside",
                      "value": 200
                    }
                  }
                ]
              },
              {
                "partition_id": "set:ad43bf8e-0f0c-4102-be91-52bc84150af2:l1_labels:distributor:flipside"
              }
            ]
          }
        }
    }


def test_dynamic_query_Execute():
    dynamic_query = DynamicQuery(get_client())
    result = dynamic_query.execute(make_query())
    assert result.get('result_count') != None
