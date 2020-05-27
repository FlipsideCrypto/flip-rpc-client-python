

class Datasets(object):

    def __init__(self, client):
        self.client = client

    def get(self, entity_id: str=None, owner_id: str=None):
        result = self.client.call("RPCService.GetDatasets", {
            "entity_id": entity_id,
            "owner_id": owner_id
        })
        return result

