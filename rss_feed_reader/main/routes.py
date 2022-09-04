from flask import render_template, Blueprint, session
from rss_feed_reader.rss.forms import URLForm
import feedparser

main = Blueprint('main', __name__)

@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    titles = []
    descriptions = []
    dates = []
    links = []
    form = URLForm()
    if form.validate_on_submit():
        url = form.url.data
        rss = feedparser.parse(url)
        for feed in rss.entries:
            titles.append(feed.title[0])
            dates.append(feed.updated[0])
            descriptions.append(feed.description[0])
            links.append(feed.link[0])
    session['titles'] = titles
    session['descriptions'] = descriptions
    session['dates'] = dates
    session['links'] = links
    
    return render_template("home.html", form=form, titles=titles, descriptions=descriptions, dates=dates, links=links)


@main.route("/rss", methods=['GET'])
def rss():
    titles=session.get("titles",None)
    descriptions=session.get("descriptions",None)
    dates=session.get("dates",None)
    links=session.get("links",None)
    return render_template("feed.html", titles=titles, descriptions=descriptions, dates=dates, links=links)
