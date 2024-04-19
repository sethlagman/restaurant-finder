"""Business Finder"""

import requests

API_KEY = "rjoLDsiD-Irc-IxTlqN9bR9YulKh61DvKhBegR_sf45XauY2RLPHoXDSN9MJChOePAogmpE9ceaIQbbEstGP0fPF6YKlPez45mZNoWz8R5lBo_9dJyYwtZ3--TBXZXYx"
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

        self.status_code = self.status() # Response status code

        self.limit = 5 # Number of results to return
        self.term = term # example: food, pizza, bar, malls
        self.location = location # location of the business
        self.attributes = attributes # hot_and_new, deals, open_to_all, wifi_free

        self.result = self.getResult() # result of the query

    def status(self):
        """Returns status code"""

        return requests.get(self.url, headers=self.header)
    
    def getResult(self):
        """Finds the business"""

        param = {
            'location': self.location.title(), 
            'limit': self.limit,
            'term': self.term.title(), 
            'attributes': self.attributes 
        }

        return requests.get(self.url, params=param, headers=self.header).json()
    
    def getName(self):
        """Finds the name of the businesses"""

        return [business['name'] for business in self.result['businesses']]
    

def get_location(ip_address):
    """Retrieves the current location"""

    response = requests.get(f'{LOCATION_API_URL}/{ip_address}/json').json()
    return f"{response['city']}, {response['region']}, {response['country']}"


def main():
    pass


if __name__ == '__main__':
    main()
