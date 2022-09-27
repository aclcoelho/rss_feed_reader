from flask import render_template, Blueprint, request, redirect, url_for
import feedparser

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST',])
@main.route("/home",methods=['GET', 'POST',])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        parsed_url = feedparser.parse(url)
        for post in parsed_url.entries:
            print(post['title'])
    return render_template("home.html")