import os

from flip_rpc_client import Client, Condition


def get_client():
    api_key = os.environ.get("FLIP_API_KEY")
    if not api_key:
        raise Exception("Missing environment variable: `FLIP_API_KEY`")

    base_url = os.environ.get("FLIP_BASE_URL")
    if not base_url:
        raise Exception("Missing environment variable: `FLIP_BASE_URL`")
    
    return Client(api_key, base_url)


def make_condition():
    return {
        "and": [
            {
                "and": [
                    {
                    "gte": {
                        "partition_id": "sorted_set:ad43bf8e-0f0c-4102-be91-52bc84150af2:current_balances:flipside",
                        "value": 0
                    }
                    },
                    {
                    "lte": {
                        "partition_id": "sorted_set:ad43bf8e-0f0c-4102-be91-52bc84150af2:current_balances:flipside",
                        "value": 100
                    }
                    }
                ]
            },
            {
                "partition_id": "set:ad43bf8e-0f0c-4102-be91-52bc84150af2:l1_labels:distributor:flipside"
            }
        ]
    }


def test_condition_GetMembers():
    condition = Condition(get_client())
    result = condition.get_members(make_condition())
    assert result.get('member_count') != None


def test_condition_IntersectMembersToCondition():
    condition = Condition(get_client())
    result = condition.intersect_members_to_condition(
        ["a0969f676e0274c34fffb4261b59d3de48de0d5845ed9780ac43045cf954ed81"],
        make_condition()
    )
    assert result.get('member_count') != None
