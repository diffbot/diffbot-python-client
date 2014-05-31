from client import DiffbotClient,DiffbotCrawl
from config import API_TOKEN
import pprint
import time

print "Calling article API endpoint on the url: http://shichuan.github.io/javascript-patterns/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
url = "http://shichuan.github.io/javascript-patterns/"
api = "article"
response = diffbot.request(url, token, api)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling article API endpoint with fields specified on the url: http://shichuan.github.io/javascript-patterns/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
url = "http://shichuan.github.io/javascript-patterns/"
api = "article"
response = diffbot.request(url, token, api, fields=['title', 'type'])
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling frontpage API endpoint on the url: http://www.huffingtonpost.com/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
url = "http://www.huffingtonpost.com/"
api = "frontpage"
response = diffbot.request(url, token, api)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling product API endpoint on the url: http://www.overstock.com/Home-Garden/iRobot-650-Roomba-Vacuuming-Robot/7886009/product.html...\n"
diffbot = DiffbotClient()
token = API_TOKEN
url = "http://www.overstock.com/Home-Garden/iRobot-650-Roomba-Vacuuming-Robot/7886009/product.html"
api = "product"
response = diffbot.request(url, token, api)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling image API endpoint on the url: http://www.google.com/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
url = "http://www.google.com/"
api = "image"
response = diffbot.request(url, token, api)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print
print "Calling classifier API endpoint on the url: http://www.twitter.com/...\n"
diffbot = DiffbotClient()
token = API_TOKEN
url = "http://www.twitter.com/"
api = "analyze"
response = diffbot.request(url, token, api)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)

print "Create a new crawl of http://support.diffbot.com/ using the Article API...\n"
token = API_TOKEN
seeds = "http://support.diffbot.com"
api = "article"
name = "testCrawl"
diffbot = DiffbotCrawl(token, name, seeds=seeds, api=api)
time.sleep(5)
status = diffbot.status()
print "\nPrinting status:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(status)
print "\nDeleting test crawl.\n"
diffbot.delete()