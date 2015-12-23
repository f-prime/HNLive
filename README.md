HNLive
======

HNLive is a live version of Hacker News (https://news.ycombinator.com/news) which streams the data from Hacker News in real time without the need to reload the page.

How to run
==========

Running HNLive is very easy.

First install the following dependencies:

* Python 2.7
* Flask
* Pymongo
* MongoDB
* lxml
* gunicorn

Next launch `getLinks.py` and let it sit running in it's own screen session. This is the script that grabs the links from HN.

Finally, launch the app with gunicorn and you are good to go.
