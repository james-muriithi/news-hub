import requests
from .models import Sources,Articles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_headlines(country="us",page_size=10):  # get all sources from the news api
    '''
    Function that gets the json response to our url request
    '''
    headlines_endpoint = '{}/top-headlines?apiKey={}&pageSize={}&country={}'.format(base_url, api_key, page_size, country)
    

    headlines_response = requests.get(headlines_endpoint).json()

    headline_results = None

    if headlines_response['articles']:
        source_results_list = headlines_response['articles']
        headline_results = process_results_articles(source_results_list)

    return headline_results  


def get_all_news(sources="engadget,techcrunch,abc-news,al-jazeera-english,bbc-news", page_size=30, category=None):  # get all sources from the news api
    '''
    Function that gets the json response to our url request
    '''
    headlines_endpoint = '{}/everything?apiKey={}&pageSize={}&sources={}'.format(base_url, api_key, page_size, sources)

    if category:
        headlines_endpoint = '{}/top-headlines?apiKey={}&pageSize={}&categoty={}'.format(base_url, api_key, page_size, category)
    

    headlines_response = requests.get(headlines_endpoint).json()

    headline_results = None

    if headlines_response['articles']:
        source_results_list = headlines_response['articles']
        headline_results = process_results_articles(source_results_list)

    return headline_results  


def get_sources():  # get all sources from the news api
    '''
    Function that gets the json response to our url request
    '''
    source_endpoint = '{}/sources?apiKey={}'.format(base_url, api_key)

    get_source_response = requests.get(source_endpoint).json()

    source_results = None

    if get_source_response['sources']:
        source_results_list = get_source_response['sources']
        source_results = process_results_sources(source_results_list)

    return source_results      


def process_results_articles(articles_list):
    '''
    Function that processes the articles list result and transform them to a list of Objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        url_to_image = article_item.get('urlToImage')
        published_at = article_item.get('publishedAt')
        content = article_item.get('content')

        if url_to_image and url_to_image != 'null':
            articles_object = Articles(
                author, title, description, url, url_to_image, published_at, content)
            articles_results.append(articles_object)

    return articles_results


def process_results_sources(source_list):
    '''
    Function that processes the source list result and transform them to a list of Objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')

        source_object = Sources(
            id, name, description, url, category, language)
        source_results.append(source_object)

    return source_results    