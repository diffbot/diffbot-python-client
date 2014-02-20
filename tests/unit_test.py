import os
import urlparse
import unittest
import requests
from mock import patch

from client import DiffbotClient


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

    def test_article_api(self):
        url = "http://www.xconomy.com/san-francisco/2012/07/25/diffbot-is-using-computer-vision-to-reinvent-the-semantic-web/"
        token = "SOME_TOKEN"
        api = "article"
        version = 2
        response = self.client.request(url, token, api, version=version)
        self.assertIn('title', response)
        self.assertEqual(response['title'], "Diffbot Is Using Computer Vision to Reinvent the Semantic Web")

    def test_frontpage_api(self):
        url = "http://www.huffingtonpost.com/"
        token = "SOME_TOKEN"
        api = "frontpage"
        version = 2
        response = self.client.request(url, token, api, version=version)
        self.assertEqual(response['tagName'], "dml")
        self.assertIn('childNodes', response)

    def test_product_api(self):
        url = "http://www.overstock.com/Home-Garden/iRobot-650-Roomba-Vacuuming-Robot/7886009/product.html"
        token = "SOME_TOKEN"
        api = "product"
        version = 2
        response = self.client.request(url, token, api, version=version)
        self.assertEqual(response['type'], "product")
        self.assertEqual(response['products'][0]['title'], "iRobot 650 Roomba Vacuuming Robot")

    def test_image_api(self):
        url = "http://www.google.com/"
        token = "SOME_TOKEN"
        api = "image"
        version = 2
        response = self.client.request(url, token, api, version=version)
        self.assertEqual(response['title'], "Google")
        self.assertEqual(response['images'][0]['url'], "https://www.google.com/images/srpr/logo9w.png")

    def test_analyze_api(self):
        url = "http://www.twitter.com/"
        token = "SOME_TOKEN"
        api = "analyze"
        version = 2
        response = self.client.request(url, token, api, version=version)
        self.assertEqual(response['type'], "image")
        self.assertEqual(response['title'], "Welcome to Twitter.")


if __name__ == '__main__':
    unittest.main()
