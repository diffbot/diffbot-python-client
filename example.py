from client import DiffbotClient
from config import API_TOKEN
import pprint

diffbot = DiffbotClient()
url = "http://shichuan.github.io/javascript-patterns/"
token = API_TOKEN
api = "article"
version = 2

print "Calling article API endpoint on the url: http://shichuan.github.io/javascript-patterns/...\n"
response = diffbot.request(url, token, api, version=2)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print "Calling article API endpoint with fields specified on the url: http://shichuan.github.io/javascript-patterns/...\n"
response = diffbot.request(url, token, api, fields=['title', 'type'], version=2)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)
