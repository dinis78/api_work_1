import requests
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
import pas


url = "https://api.foursquare.com/v3/places/search"

params = {
  	"query": "coffee",
  	"near": "Novosibirsk",
  	"open_now": "true",
  	"sort":"DISTANCE"
}

headers = {
    "Accept": "application/json",
    "Authorization": pas.api_key
}

response = requests.request("GET", url, params=params, headers=headers)

print(response.text)


def search_venues(category):
    url = 'https://api.foursquare.com/v2/venues/search'
    
    params = {
        'client_id': pas.client_id,
        'client_secret': pas.client_secret,
        'v': '20240314',
        'near': 'Novosibirsk',  # Замените на нужный вам город или местоположение
        'query': category
    }
    
    response = requests.get(url, params=params).json()
    
    if response['meta']['code'] == 200:
        venues = response['response']['venues']
        for venue in venues:
            name = venue['name']
            address = venue['location']['address']
            rating = venue.get('rating', 'N/A')
            
            print(f'Название: {name}')
            print(f'Адрес: {address}')
            print(f'Рейтинг: {rating}')
            print('---')
    
    else:
        print('Произошла ошибка при выполнении запроса.')

category = input('Введите интересующую вас категорию: ')
search_venues(category)