from flask import Flask, render_template, jsonify
import pymongo
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

db = pymongo.MongoClient("localhost", 27017).hnlive
app = Flask(__name__)

@app.route("/get_links/<page>")
def get_links(page):
    links = db.links.find_one({"page":page})
    if links:
        links = links['links']
    if not links:
        links = []
    return render_template("links.html", links=links)

@app.route("/")
def hot():
    return render_template("hot.html")

@app.route("/newest")
def newest():
    return render_template("newest.html")

@app.route("/show")
def show():
    return render_template("show.html")

@app.route("/ask")
def ask():
    return render_template("ask.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
