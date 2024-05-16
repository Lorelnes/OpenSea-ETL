
####################################################
# here you should have all functionality for        #
# extracting ONLY EXTRACTING data from the API      #
# this means you should make calls to the API.      #
# transforming or loading should happen in another  #
# file                                              #
####################################################
import requests
import pandas as pd
from constants import url, params, headers

# Sending HTTP get request to API endpoint
def make_api_call(url, headers, params):
    r = requests.get(url, params = params, headers = headers)
    if r.status_code == 200:
        print("Successful API call")
        try:
            data = r.json() #Parsing JSON
            collections = data.get("collections")
            df = pd.DataFrame(collections) #Turning into dataframe
            return df
        except Exception as e:
            print(e)
            return None
    else:
        print(f"Error: {r.status_code}")

    return r

response = make_api_call(url = url, headers=headers, params=params)

"""
    This function should take care of sending single request to API endpoint
    you will need to modify arguments that have to be passed, feel free to mess around.

    My advice: single call returns 100 collections for a single page as JSON
    use pandas and turn it into DataFrame, will be easier to manager
"""
pass


def extract_next_page_token():
    """

    this function is just as an advice, you can use it above to wrap the functionality
    about extracting next page token from the response, and it should return a simple
    string that needs to be passed to the API endpoint.

    for example: next could be ======> LXBrPTMyMjEyNDY5
    """
    pass

