# Python Diffbot API Client


## Preface
Identify and extract the important parts of any web page in Python!  This client currently supports calls to Diffbot's Automatic APIs and Crawlbot.


Installation
To install activate a new virtual environment and run the following command:

    $ pip install -r requirements.txt

## Configuration

To run the example, you must first configure a working API token in config.py:

    $ cp config.py.example config.py; vim config.py;

Then replace the string "SOME_TOKEN" with your API token.  Finally, to run the example:

    $ python example.py

## Usage

### Article API
An example call to the Article API:

```
diffbot = DiffbotClient()
token = "SOME_TOKEN"
version = 2
url = "http://shichuan.github.io/javascript-patterns/"
api = "article"
response = diffbot.request(url, token, api, version=2)
```

### Product API
An example call to the Product API:

```
diffbot = DiffbotClient()
token = "SOME_TOKEN"
version = 2
url = "http://www.overstock.com/Home-Garden/iRobot-650-Roomba-Vacuuming-Robot/7886009/product.html"
api = "product"
response = diffbot.request(url, token, api, version=version)
```

### Image API
An example call to the Image API:

```
diffbot = DiffbotClient()
token = "SOME_TOKEN"
version = 2
url = "http://www.google.com/"
api = "image"
response = diffbot.request(url, token, api, version=version)
```

### Analyze API
An example call to the Analyze API:

```
diffbot = DiffbotClient()
token = "SOME_TOKEN"
version = 2
url = "http://www.twitter.com/"
api = "analyze"
response = diffbot.request(url, token, api, version=version)
```

### Crawlbot API
To start a new crawl, specify a crawl name, seed URLs, and the API via which URLs should be processed. An example call to the Crawlbot API:

```
token = "SOME_TOKEN"
name = "sampleCrawlName"
seeds = "http://www.twitter.com/"
api = "analyze"
sampleCrawl = DiffbotCrawl(token,name,seeds=seeds,api=api)
```

Omit "seeds" and "api" to load an existing crawl, or create a crawl as a placeholder.

To check the status of a crawl:

```
sampleCrawl.status()
```

To update a crawl:

```
maxToCrawl = 100
upp = "diffbot"
sampleCrawl.update(maxToCrawl=maxToCrawl,urlProcessPattern=upp)
```

To delete or restart a crawl:

```
sampleCrawl.delete()
sampleCrawl.restart()
```

To download crawl data:

```
sampleCrawl.download() # returns JSON by default
sampleCrawl.download(data_format="csv")
```

To pass additional arguments to a crawl:

```
sampleCrawl = DiffbotCrawl(token,name,seeds,apiUrl,maxToCrawl=100,maxToProcess=50,notifyEmail="support@diffbot.com")
```

## Testing

First install the test requirements with the following command:

    $ pip install -r test_requirements.txt

Currently there are some simple unit tests that mock the API calls and return data from fixtures in the filesystem.  From the project directory, simply run:

    $ nosetests
