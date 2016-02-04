import lxml.html
import urllib
import pymongo
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

db = pymongo.MongoClient("localhost", 27017).hnlive

def getLinks(page):
    
    url = "https://news.ycombinator.com/{}".format(page)
    html = lxml.html.fromstring(urllib.urlopen(url).read())
    links = []
    for x in html.xpath("//tr[@class='athing']/td[@class='title']/a"):
        link, text = x.attrib['href'], unicode(x.text)
        links.append([link, text])
    for i, p in enumerate(html.xpath("//tr/td[@class='subtext']/span[@class='score']")):
        points = p.text.split()[0]
        links[i].append(points)
    on = 0
    for i, p in enumerate(html.xpath("//tr/td[@class='subtext']/a")):
        if "comment" in p.text:
            comments = p.text.split()[0]
            try:
                links[on - 1].append(comments)
            except:
                pass
        if i % 3 == 0:
            on += 1
    if not links:
        return getLinks(page)
    return links


while __name__ == "__main__":
    pages = ["", "newest", "show", "ask"]
    for page in pages:
        links = getLinks(page)
        if page == "":
            page = "hot"
        db.links.remove({"page":page})
        db.links.insert({"page":page, "links":links})
        print "Updated {}".format(page)
    time.sleep(10)
