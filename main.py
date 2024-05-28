from constants import url, params, headers, selected_columns
from extract import make_api_call
from transform import transform_instagram_username, transform_twitter_username, split_contracts
from load import load_raw_to_json, load_data_to_database
from setting import dbname, user, host, password, port
import logging

# Extraction
logging.basicConfig(level=logging.INFO)

df, next_token = make_api_call(url=url, headers=headers, params=params)
if df is not None:
    logging.info("Successful API call")

while next_token is not None:
    params['next'] = next_token
    df, next_token = make_api_call(url=url, headers=headers, params=params)
    if df is None:
        break
    load_raw_to_json(df, "ethereum", next_token)

# Transformation
df['twitter_username'] = df['twitter_username'].apply(transform_twitter_username)
df['instagram_username'] = df['instagram_username'].apply(transform_instagram_username)
df = split_contracts(df)

# Loading
df_selected = df[selected_columns]

load_data_to_database(df_selected, dbname, user, host, password, port)




