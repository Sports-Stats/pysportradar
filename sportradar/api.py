
import requests


class Api:
    def __init__(self, api_key):
        """"""
        self.session = requests.Session()
        self.api_key = api_key
        self.base_url = "https://api.sportradar.us"
        self.params = {
            "api_key": self.api_key
        }
        
    def _get(self, path):
        """"""
        url = f"{self.base_url}{path}"
        print(url)
        response = self.session.get(url=url, params=self.params)
        return response


    def _post(self, path, body):
        """"""
        if not isinstance(body, dict):
            raise Exception("Body is not JSON or dict") # Better way to do this
        else:
            url = f"{self.base_url}{path}"
            response = self.session.get(url=url, params=self.params, json=body)
            return response