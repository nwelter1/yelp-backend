import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'Yelp will never guess...'
    API_KEY = os.environ.get('API_KEY')