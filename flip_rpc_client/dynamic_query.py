

class DynamicQuery(object):

    def __init__(self, client):
        self.client = client

    def execute(self, query, debug=False):
        result = self.client.call("RPCService.ExecuteDynamicQuery", {
            "query": query,
            "debug": debug
        })
        return result

   