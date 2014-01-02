import os
import unittest
from client import DiffbotClient
from mock import patch
import simplejson

def fake_request(client, api):
    resource_file = os.path.normpath('test_fixtures/%s.json' % api)
    with open(resource_file, mode='rb') as file:
        json = file.read()
    return simplejson.loads(json)


class TestDiffbotClient(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('client.DiffbotClient.request', fake_request)
        self.patcher.start()
        self.client = DiffbotClient()

    def tearDown(self):
        self.patcher.stop()

    def test_request_for_article(self):
        api = "article"
        response = self.client.request(api)
        self.assertIn('text', response)
        self.assertEqual(response['meta']['title'], 'JavaScript Patterns')

if __name__ == '__main__':
    unittest.main()