from flask import render_template, Blueprint, request, redirect, url_for, session
import feedparser

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST',])
@main.route("/home",methods=['GET', 'POST',])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        #parsed_url = feedparser.parse(url)
        session['url'] = url
    return render_template("home.html")

@main.route("/feed",methods=['GET', 'POST',])
def feed():
    if request.method == "GET":
        print("It's working!")
    return render_template("feed.html")