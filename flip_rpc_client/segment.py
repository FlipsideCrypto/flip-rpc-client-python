

class Segment(object):

    def __init__(self, client):
        self.client = client

    def get_members(self, segment):
        result = self.client.call("RPCService.GetSegmentMembers", {
            "segment": segment
        })
        return result

    def intersect_members_to_segment(self, members, segment):
        result = self.client.call("RPCService.GetSegmentMembers", {
            "members": members,
            "segment": segment
        })
        return result
