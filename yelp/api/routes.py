from wsgiref import headers
from flask import Blueprint
import requests
import os

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/city/<city>/<term>', methods=['GET','POST'])
def getbiz(city,term):
    print(city)
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': f'{term}', 
          'location': f'{city}',
          'limit': 20}
    key = os.environ['API_KEY']
    res = requests.get(url, params = params, headers={'Authorization': f'Bearer {key}'})
    
    return res.json()