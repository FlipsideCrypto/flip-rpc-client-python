

class Condition(object):

    def __init__(self, client):
        self.client = client

    def get_members(self, condition):
        result = self.client.call("RPCService.GetConditionMembers", {
            "condition": condition
        })
        return result

    def intersect_members_to_condition(self, members, condition):
        result = self.client.call("RPCService.GetConditionMembers", {
            "members": members,
            "condition": condition
        })
        return result
