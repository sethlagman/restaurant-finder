"""Business Finder"""

import requests
import os

from decouple import config

API_KEY = config('API_KEY')
API_URL = "https://api.yelp.com/v3/businesses/search"
LOCATION_API_URL = "http://ipinfo.io/"

class BusinessFinder:
    """Finds restaurants, malls, foods, entertainment, services, and many more"""

    def __init__(self, term, location, attributes=''):
        """Initialize attributes"""
            
        self.key = API_KEY
        self.url = API_URL

        self.header = {
            'Authorization': 'Bearer ' + API_KEY,
            'accept': 'application/json',
        }

        self.limit = 10 # Number of results to return
        self.term = term # Example: food, pizza, bar, malls
        self.location = location # Location of the business
        self.attributes = attributes # hot_and_new, deals, open_to_all, wifi_free

        self.param = {
            'location': self.location.title(),
            'limit': self.limit,
            'term': self.term.title(),
            'attributes': self.attributes
        }

        self.status = self.getStatus() # Status code of the query
        self.result = self.getResult() # Result of the query

    def getStatus(self):
        """Returns status code"""

        return requests.get(self.url, params=self.param, headers=self.header).status_code
    
    def getResult(self):
        """Retrieves the business"""

        return requests.get(self.url, params=self.param, headers=self.header).json()
    
    def getName(self):
        """Retrieves the name of the businesses"""

        return [business['name'] for business in self.result['businesses']]
    
    def getRating(self):
        """Retrieves the ratings of the business"""

        return [business['rating'] for business in self.result['businesses']]
    
    def getLocation(self):
        """Retrieves the location of the business"""

        return [business['location']['display_address'][0:-1] for business in self.result['businesses']]
    
    def getUrl(self):
        """Retrieves the url page of the business"""
        
        return [business['url'] for business in self.result['businesses']]

    def getImage(self):
        """Retrieves the images of the business"""
        
        return [business['image_url'] for business in self.result['businesses']]
    
def get_location(ip_address):
    """Retrieves the current location"""

    response = requests.get(f'{LOCATION_API_URL}/{ip_address}/json').json()
    return f"{response['city']}, {response['region']}, {response['country']}"


def main():
    pass

if __name__ == '__main__':
    main()
