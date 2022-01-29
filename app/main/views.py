from flask import render_template
from . import main
from ..requests import get_sources, get_headlines

@main.route('/')
def index():
    sources = get_sources()
    headlines = get_headlines(page_size=15)

    return render_template("index.html", tags = sources[:7], headlines=headlines)