from flask import render_template
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    sources = get_sources()
    print(sources[:5])
    return render_template("index.html")