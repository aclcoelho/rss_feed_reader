from flask import render_template, Blueprint, request, redirect, url_for, session, flash
import feedparser

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
@main.route("/home",methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        session['url'] = url
        return redirect(url_for("main.feed"))
    return render_template("home.html")

@main.route("/feed", methods=['GET', 'POST'])
def feed():
    if request.method == "GET":
        url=session.get("url",None)
        parsed_url = feedparser.parse(url)
        entries = parsed_url.entries
        if len(entries) == 0:
            flash("No feed to show! Please enter another URL!")
    elif request.method == "POST":
        url = request.form.get("url")
        session['url'] = url
        return redirect(url_for("main.feed"))
    return render_template("feed.html", entries=entries)