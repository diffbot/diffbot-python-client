import requests

class DiffbotClient(object):

    base_url = 'http://api.diffbot.com/'

    def request(self, url, token, api, fields=None, version=3, **kwargs):
        """
        Returns a python object containing the requested resource from the diffbot api
        """
        params = {"url": url, "token": token}
        if fields:
            params['fields'] = fields
        params.update(kwargs)
        response = requests.get(self.compose_url(api, version), params=params)
        response.raise_for_status()
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
        return 'v{}'.format(version_number)

class DiffbotJob(DiffbotClient):
    """
    Various calls for managing a Diffbot Crawlbot or Bulk API job.
    """

    def request(self,params):
        response = requests.get(self.compose_url(self.jobType,3),params=params)
        response.raise_for_status
        try:
            return response.json()
        except:
            print response.text

    def start(self,params):
        response = self.request(params)
        return response

    def status(self):
        response = self.request(self.params)
        return response

    def delete(self):
        temp_params = self.params
        temp_params['delete'] = 1
        response = self.request(temp_params)
        return response

    def restart(self):
        temp_params = self.params
        temp_params['restart'] = 1
        response = self.request(temp_params)
        return response

class DiffbotCrawl(DiffbotJob):
    """
    Initializes a new Diffbot crawl. Pass additional arguments as necessary.
    """

    def __init__(self,token,name,seeds,api,apiVersion=3,**kwargs):
        self.params = {
            "token": token,
            "name": name,
        }
        startParams = dict(self.params)
        startParams['seeds'] = seeds
        startParams['apiUrl'] = self.compose_url(api,apiVersion)
        startParams.update(kwargs)
        self.jobType = "crawl"
        self.start(startParams)