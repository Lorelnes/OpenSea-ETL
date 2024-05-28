import pandas as pd
import requests
import constants
import logging
import time

logging.basicConfig(level=logging.INFO)
def make_api_call(url, headers, params, max_retries=3, retry_delay=2):
    for i _ in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            logging.info("Successful API call")

            data = response.json().get("Collections", [])
            next_token = response.json().get("next")

            df = pd.DataFrame(data)
            return df, next_token
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestsException as request_err:
            logging.error(f"Requests exception occurred: {request_err}")
        except ValueError as value_err:
            logging.error(f"ValueError occurred: {value_err}")

        time.sleep(retry_delay)

    logging.warning("Maximum retries reached")
    return None, None #

          #  data = response.json()["collections"] # TODO: response might be empty, on the last page, look up different ways to access element in json, dictionaries



    

