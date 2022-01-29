from calendar import c
from nis import cat
from flask import render_template
from . import main
from ..requests import get_all_news, get_sources, get_headlines

@main.route('/')
def index():
    sources = get_sources()
    headlines = get_headlines(page_size=15)

    top_news = get_all_news()

    return render_template("index.html", tags = sources[:7], headlines=headlines, top_news=top_news)

@main.route('/category/<category>')
def category(category):
    top_news = get_all_news(category=category)

    title = category.title()

    return render_template("category.html", news_articles=top_news, title=title, category=category)    

@main.route('/source/<source>')
def souce(source):
    top_news = get_all_news(sources=source)

    title = source.title()

    return render_template("source.html", news_articles=top_news, title=title, source=title)        