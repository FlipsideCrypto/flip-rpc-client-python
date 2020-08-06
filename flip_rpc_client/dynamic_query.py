

class DynamicQuery(object):

    def __init__(self, client):
        self.client = client

    def execute(self, query, ttl_seconds, debug=False):
        result = self.client.call("RPCService.ExecuteDynamicQuery", {
            "query": query,
            "debug": debug,
            "ttl_seconds": ttl_seconds
        })
        return result

   