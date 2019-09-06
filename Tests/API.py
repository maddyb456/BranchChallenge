# importing the requests library
import requests
from BranchProject.Tests.login import *

URL = "https://api2.branch.io/v1/url"  # API-endpoint
API_KEY = 'key_live_gpMvVL8RA0KgQqZnyHIdZpnlEFnbyh18'  # API key

# defining user agent and header
user_agent = 'Mozilla/5.0 (Linux; Android 9.0; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
headers = {'User-Agent': user_agent}

# defining a params dict for the parameters to be sent to the API
payload = {'branch_key': API_KEY, 'campaign': 'QATesting', 'channel': 'Automation', 'type': 2}


# Creating and verifying the link
def create_link():
    # Sending post request and saving the response as response object
    api_response = requests.post(URL, data=payload)
    if api_response.status_code == 200:
        response = api_response.json()
        print(response)
        print("Link created successfully")
        # making a call to the campaign link created via the API
        url = response['url']
        click_response = requests.get(url, headers=headers)
        print(click_response.status_code)
        if click_response.status_code == 200:
            print("Link clicked successfully")
            return url
        else:
            return None
    elif api_response.status_code == 404:
        print("Link not created successfully")
        return None


campaignURL = create_link()
if campaignURL is not None:
    branch_login()
    live_view_events(campaignURL)

