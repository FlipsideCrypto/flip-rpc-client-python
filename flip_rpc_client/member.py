

class Member(object):

    def __init__(self, client):
        self.client = client

    def get_partitions(self, entity_id: str, member_id: str):
        result = self.client.call("RPCService.GetMemberPartitions", {
            "entity_id": entity_id,
            "member_id": member_id
        })
        return result
