from flask import render_template
from . import main
from ..requests import get_all_news, get_sources, get_headlines

@main.route('/')
def index():
    sources = get_sources()
    headlines = get_headlines(page_size=15)

    top_news = get_all_news()

    return render_template("index.html", tags = sources[:7], headlines=headlines, top_news=top_news)