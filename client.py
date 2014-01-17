import requests


class DiffbotClient(object):
    def __init__(self):
        self.base_url = "http://api.diffbot.com/"

    def request(self, url, token, api, fields=[], version=2):
        """
        Returns a python object containing the requested resource from the diffbot api
        """
        params = {"url": url, "token": token}
        response = requests.get(self.compose_url(api, version), params=params)
        print response.content
        obj = response.json()
        obj = self.select_fields_from_response(obj, fields)
        return obj

    @staticmethod
    def select_fields_from_response(obj, fields):
        """
        Returns the response object with the specified fields or all fields if
        the fields list is empty
        """
        if fields:
            obj = dict((x, obj[x]) for x in fields)
        return obj

    def compose_url(self, api, version_number):
        """
        Returns the uri for an endpoint as a string
        """
        version = self.format_version_string(version_number)
        url = self.base_url + version + "/" + api
        return url

    @staticmethod
    def format_version_string(version_number):
        """
        Returns a string representation of the API version
        """
        version = "v" + str(version_number)
        return version
