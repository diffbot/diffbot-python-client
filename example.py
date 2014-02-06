from client import DiffbotClient
from config import API_TOKEN
import pprint


print "Calling article API endpoint on the url: http://shichuan.github.io/javascript-patterns/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
version = 2
url = "http://shichuan.github.io/javascript-patterns/"
api = "article"
response = diffbot.request(url, token, api, version=2)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling article API endpoint with fields specified on the url: http://shichuan.github.io/javascript-patterns/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
version = 2
url = "http://shichuan.github.io/javascript-patterns/"
api = "article"
response = diffbot.request(url, token, api, fields=['title', 'type'], version=2)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling frontpage API endpoint on the url: http://www.huffingtonpost.com/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
version = 2
url = "http://www.huffingtonpost.com/"
api = "frontpage"
response = diffbot.request(url, token, api, version=version)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling product API endpoint on the url: http://www.overstock.com/Home-Garden/iRobot-650-Roomba-Vacuuming-Robot/7886009/product.html...\n"
diffbot = DiffbotClient()
token = API_TOKEN
version = 2
url = "http://www.overstock.com/Home-Garden/iRobot-650-Roomba-Vacuuming-Robot/7886009/product.html"
api = "product"
response = diffbot.request(url, token, api, version=version)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling image API endpoint on the url: http://www.google.com/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
version = 2
url = "http://www.google.com/"
api = "image"
response = diffbot.request(url, token, api, version=version)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling classifier API endpoint on the url: http://www.twitter.com/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
version = 2
url = "http://www.twitter.com/"
api = "analyze"
response = diffbot.request(url, token, api, version=version)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)