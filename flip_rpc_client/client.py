import requests
import json


class Client(object):

    def __init__(self, api_key, base_url, tls_verify=True):
        self.api_key = api_key
        self.base_url = base_url
        self.rpc_url = "{base_url}/rpc?api_key={api_key}".format(
            base_url=base_url, api_key=api_key
        )
        self.tls_verify = tls_verify

    def makeRpcCall(self, headers, payload):
        try:
            response = requests.post(
                self.rpc_url,
                headers=headers, 
                data=payload, 
                verify=self.tls_verify
            )
        except Exception as e:
            raise RpcCallFailedException(e)

        if response.status_code != 200:
            raise RpcCallFailedException("Invalid status code: %s" % response.status_code)

        responseJson = response.json(parse_float=lambda f: f)
        if type(responseJson) != list:
            if "error" in responseJson and responseJson["error"] is not None:
                raise RpcCallFailedException("RPC call error: %s" % responseJson["error"])
            else:
                return responseJson["result"]
        else:
            result = []
            for subResult in responseJson:
                if "error" in subResult and subResult["error"] is not None:
                    raise RpcCallFailedException("RPC call error: %s" % subResult["error"])
                else:
                    result.append(subResult["result"])
            return result
    
    def call(self, method, params=None, headers={}):
        base_headers = {'content-type': 'application/json'}
        headers.update(base_headers)

        payload = json.dumps({
            "jsonrpc": "2.0", 
            "id": "0", 
            "method": method, 
            "params": [
                params
            ]
        })

        return self.makeRpcCall(headers, payload)


class RpcCallFailedException(Exception):
    pass

