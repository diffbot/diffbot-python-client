import os
import urlparse
import unittest
import simplejson
import logging
import requests
from mock import Mock, patch

from client import DiffbotClient


logger = logging.getLogger(__name__)


def fake_get(url, params):
    path = urlparse.urlparse(url).path
    path_tuple = os.path.split(path)
    api = path_tuple[len(path_tuple) - 1]
    resource_file = os.path.normpath('tests/test_fixtures/%s.json' % api)
    with open(resource_file, mode='rb') as file:
        json = file.read()
    r = requests.Response()
    r.status_code = 200
    r._content = json
    return r


class DiffbotClientUnitTest(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('client.requests.get', fake_get)
        self.patcher.start()
        self.client = DiffbotClient()

    def tearDown(self):
        self.patcher.stop()

    def test_request_for_article(self):
        url = "http://shichuan.github.io/javascript-patterns/"
        token = "3c66f28f72ea40c1b02e6a4cc195b07e"
        api = "article"
        version = 2
        response = self.client.request(url, token, api, version=version)
        self.assertIn('text', response)
        self.assertEqual(response['meta']['title'], 'JavaScript Patterns')


if __name__ == '__main__':
    unittest.main()