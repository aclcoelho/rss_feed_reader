from turtle import title
from flask import render_template, Blueprint

rss = Blueprint('rss', __name__)

@rss.route("/rss_feed")
def rss_feed():
    return render_template("feed.html")
