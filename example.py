from client import DiffbotClient
import pprint

diffbot = DiffbotClient()
url = "http://shichuan.github.io/javascript-patterns/"
token = "3c66f28f72ea40c1b02e6a4cc195b07e"
api = "article"
version = 2

print "Calling article API endpoint on the url: http://shichuan.github.io/javascript-patterns/...\n"
response = diffbot.request(url, token, api, version=2)
print "\nPrinting response:\n"
pp = pprint.PrettyPrinter(indent=4)
print pp.pprint(response)
