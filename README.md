# flip-rpc-client-python

Python3 client for accessing Flip RPC Interface

## Usage

### Install

```python
python3 setup.py install
```

or via `requirements.txt:`

```
git+ssh://git@github.com/FlipsideCrypto/flip-rpc-client-python.git
```

### Initialization

```python
from flip_rpc_client import Client

client = Client("<api-key>", "<base_url>")

```

### Get Condition Members

Evaluate a condition and retrieve the members.

```python
from flip_rpc_client import Condition

condition_logic = {
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
}

condition = Condition(client)
result = condition.get_members(condition_logic)

```

### Intersect Members to Condition

Identify the intersection of an array of members to evaluated conditions.

```python
from flip_rpc_client import Condition

condition_logic = {
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
}

members = ["a0969f676e0274c34fffb4261b59d3de48de0d5845ed9780ac43045cf954ed81"]


condition = Condition(client)
result = condition.intersect_members_to_condition(
    members,
    condition_logic
)
```

### Get Member Partitions

For a particular entityID and memberID return the partitions that the member belongs to.

```python
from flip_rpc_client import Condition

entity_id = "ad43bf8e-0f0c-4102-be91-52bc84150af2"
member_id = "a0969f676e0274c34fffb4261b59d3de48de0d5845ed9780ac43045cf954ed81"

member = Member(client)
result = member.get_partitions(entity_id, member_id)

```

### Get Datasets

Retreive available datasets and apply optional filters (`entityID`, `ownerID`).

```python
from flip_rpc_client import Datasets

d = Datasets(client)
result = d.get()

```

## Tests

Set environment variables `FLIP_API_KEY` and `FLIP_BASE_URL`.

```bash
export FLIP_API_KEY=<your-api-key>;
export FLIP_BASE_URL=<flip-rpc-service-url>;

cd tests && pytestl
```
