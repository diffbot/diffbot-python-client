Python Diffbot API Client
=========

Currently supports calls to the article endpoint.


Installation
-----------
To install activate a new virtual environment and run the following command:

    $ pip install -r requirements.txt

To run the example:

    $ python example.py

Example use
--------------
An example of how to use the client in your code:

```
diffbot = DiffbotClient()
url = "http://shichuan.github.io/javascript-patterns/"
token = "3c66f28f72ea40c1b02e6a4cc195b07e"
api = "article"
version = 2

response = diffbot.request(url, token, api, version=2)
```

Testing
------------

First install the test requirements with the following command:

    $ pip install -r test_requirements.txt

Unit and integration tests are configured to run using nose.  From the project directory, simply run:

    $ nosetests
