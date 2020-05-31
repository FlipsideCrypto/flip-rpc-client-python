import os

from flip_rpc_client import Client, Member


def get_client():
    api_key = os.environ.get("FLIP_API_KEY")
    if not api_key:
        raise Exception("Missing environment variable: `FLIP_API_KEY`")

    base_url = os.environ.get("FLIP_BASE_URL")
    if not base_url:
        raise Exception("Missing environment variable: `FLIP_BASE_URL`")
    
    return Client(api_key, base_url)


def test_member_GetPartitions():
    member = Member(get_client())
    entity_id = "ad43bf8e-0f0c-4102-be91-52bc84150af2"
    member_id = "a0969f676e0274c34fffb4261b59d3de48de0d5845ed9780ac43045cf954ed81"
    result = member.get_partitions(entity_id, member_id)
    assert result.get('partition_count') != None
