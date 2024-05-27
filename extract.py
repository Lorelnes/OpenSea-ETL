"""
GENERAL COMMENT (APPLIES NOT ONLY TO THIS .py FILE): when importing modules, you could order them
its fine the way it is now but for readability it might be good to order.

for example you could decide to import starting with   
    - standard library imports
    - related third party imports
    - local library imports

or you could deside to go for more aesthetic way:
start by
from <something> import <something>
import <something> as <alias>
import <something>

this is what your imports could look like:
    from constants import url, params, headers
    from urllib import response
    import pandas as pd
    import requests
    import json
"""

import requests
from urllib import response # why are you importing response from urllib, you are not using it
import pandas as pd
from constants import url, params, headers # no need to import variables here
import json # not using json 


def make_api_call(url, headers, params):
    response = requests.get(url, params=params, headers=headers)
    #TODO: instead of checking for status code, you can use try...except
    # send request to API, if error happens wait to resend request or handle it in different way

    if response.status_code == 200:
        print("Successful API call") #TODO: instead of printing try using logging. e.g logging.info("Successful API call")
        try:
            data = response.json()["collections"] #TODO: response might be empty, on the last page, look up different ways to access element in json, dictionaries
            # here you could use .get("collections")
            next_token = response.json().get("next")
            df = pd.DataFrame(data)
            return df, next_token
         #TODO: using Exception as e is pointless, error handling needs to be more specific
        except Exception as e:
            #TODO: instead of printing use logging
            return None, None
    else:
        #TODO: you are already handling error in exception, why include it in else?
        #TODO: instead of printing use logging
        print(f"Error: {response.status_code}")
        return None, None
    
    #TODO: why is the function returing None, None

