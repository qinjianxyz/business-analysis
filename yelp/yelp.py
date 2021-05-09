#Business Search        URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match         URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search           URL -- 'https://api.yelp.com/v3/businesses/search/phone'
#Business Details       URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews       URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

# import modules
import requests
from YelpAPI import get_my_key

# define a business ID


# Define the API Key, define endpoint, define the header
business_id = 'panera-bread-san-diego-6'
API_KEY = get_my_key()
#ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
ENDPOINT = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id)
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define the parameters
PARAMETERS = {'term': 'coffee', 
                'limit': 50,
                'raidis': 10000,
                'offset': 50,
                'location': 'San Diego'}

# Make a request to Yelp API

#response = requests.get(url = ENDPOINT, params= PARAMETERS, headers= HEADERS)
response = requests.get(url = ENDPOINT, headers= HEADERS)


# convert the JSON string to a dictionary

business_data = response.json()
print(business_data)