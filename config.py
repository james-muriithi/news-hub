from email.policy import default
import os
from decouple import config

class Config:
    """
    General configuration parent class
    """
    NEWS_API_KEY = config('API_KEY', default="")
    NEWS_API_BASE_URL = 'https://newsapi.org/v2'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(NEWS_API_KEY)
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    
    SECRET_KEY = config('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config_options = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}