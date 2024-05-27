import requests
from urllib import response
import pandas as pd
from constants import url, params, headers
import json


def make_api_call(url, headers, params):
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        print("Successful API call")
        try:
            data = response.json()["collections"]
            next_token = response.json().get("next")
            df = pd.DataFrame(data)
            return df, next_token
        except Exception as e:
            print(e)
            return None, None
    else:
        print(f"Error: {response.status_code}")
        return None, None

