from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

# Define the API endpoint and parameters, start at 2 because we're looking for ETH
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '2',
    'limit': '1',
    'convert': 'USD'
}

# Set up API key and headers
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'f31ab6e2-4633-4bd6-86fe-8ce5bd7a114e',
}

# Create a session with the provided headers
session = Session()
session.headers.update(headers)

# Make the API request and handle exceptions
try:
    # Send a GET request to the API endpoint with specified parameters
    response = session.get(url, params=parameters)

    # Print the retrieved data, we use the keys to isolate the price value
    pprint.pprint(json.loads(response.text)['data'][0]['quote']['USD']['price'])

except (ConnectionError, Timeout, TooManyRedirects) as e:
    # Handle potential errors such as connection issues
    print(e)