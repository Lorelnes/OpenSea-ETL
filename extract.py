####################################################
# here you should have all functionality for        #
# extracting ONLY EXTRACTING data from the API      #
# this means you should make calls to the API.      #
# transforming or loading should happen in another  #
# file                                              #
####################################################
import requests
from urllib import response
import pandas as pd
from constants import url, params, headers

# Sending HTTP get request to API endpoint

def make_api_call(url, headers, params):
    r = requests.get(url, params=params, headers=headers)
    if r.status_code == 200:
        print("Successful API call")
        try:
            data = r.json()["collections"]
            df = pd.DataFrame(data)
            next_token = r.json().get("next")
            return df, next_token
        except Exception as e:
            print(e)
            return None, None
    else:
        print(f"Error: {r.status_code}")
        return None, None

response, next_token = make_api_call(url=url, headers=headers, params=params)

print(response)
print("Next token:", next_token)
