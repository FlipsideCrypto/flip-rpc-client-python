import os

from flip_rpc_client import Client, Datasets


def get_client():
    api_key = os.environ.get("FLIP_API_KEY")
    if not api_key:
        raise Exception("Missing environment variable: `FLIP_API_KEY`")

    base_url = os.environ.get("FLIP_BASE_URL")
    if not base_url:
        raise Exception("Missing environment variable: `FLIP_BASE_URL`")
    
    return Client(api_key, base_url)


def test_GetDatasets():
    d = Datasets(get_client())
    result = d.get()
    assert result.get('datasets') != None
