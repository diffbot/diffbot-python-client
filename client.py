import requests


class DiffbotClient(object):
    def __init__(self):
        self.base_url = "http://api.diffbot.com/"

    def request(self, url, token, api, fields=[], version=2, **kwargs):
        """
        Returns a python object containing the requested resource from the diffbot api
        """
        params = {"url": url, "token": token}
        if fields:
            params['fields'] = fields
        if kwargs:
            params.update(kwargs)
        response = requests.get(self.compose_url(api, version), params=params)
        return response.json()

    def compose_url(self, api, version_number):
        """
        Returns the uri for an endpoint as a string
        """
        version = self.format_version_string(version_number)
        return '{}{}/{}'.format(self.base_url, version, api)

    @staticmethod
    def format_version_string(version_number):
        """
        Returns a string representation of the API version
        """
        return '{}v'.format(version_number)
