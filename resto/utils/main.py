"""Business Finder"""

import requests

API_KEY = "iiWBdl8HrY0NWnXKj-K9jsGHGN60vm1jJJ_9EAdRGAA_V03ntToGWvrlQxMUMWVrjAO3aeDP6hg7EcdFv7lIiXhiY0P9QHZfVF7u0GuLCvR_BWj5QL6qWmG4uo0mZnYx"
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

        self.limit = 5 # Number of results to return
        self.term = term # example: food, pizza, bar, malls
        self.location = location # location of the business
        self.attributes = attributes # hot_and_new, deals, open_to_all, wifi_free

        self.param = {
            'location': self.location.title(),
            'limit': self.limit,
            'term': self.term.title(),
            'attributes': self.attributes
        }

        self.status = self.getStatus() # status code of the query
        self.result = self.getResult() # result of the query

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

def get_location(ip_address):
    """Retrieves the current location"""

    response = requests.get(f'{LOCATION_API_URL}/{ip_address}/json').json()
    return f"{response['city']}, {response['region']}, {response['country']}"


def main():
    pass

if __name__ == '__main__':
    main()
