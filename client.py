import requests

class DiffbotClient(object):
    def __init__(self):
        pass

    def request(self, url, token, api, fields=[], version=2):
        """
        Returns a python object containing the requested resource from the diffbot api
        """
        params = {"url": url, "token": token}
        response = requests.get(self.get_url(api, version), params=params)
        obj = response.json()
        if fields:
            obj = dict( (x, obj[x]) for x in fields)
        return obj

    def get_url(self, api, version):
        """
        Returns the uri for an endpoint as a string
        """
        base_url = "http://api.diffbot.com/"
        version = "v" + str(version)
        url = base_url + version + "/" + api
        return url
