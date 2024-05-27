from extract import make_api_call
from constants import url, params, headers
from transform import transform_instagram_username, transform_twitter_username, split_contracts
from load import load_raw_to_json, load_data_to_database

# Extraction
df, next_token = make_api_call(url=url, headers=headers, params=params)
for i in range(5):
    print(df.head())
    print("Next token:", next_token)
    params['next'] = next_token
    df, next_token = make_api_call(url=url, headers=headers, params=params)
    filename = load_raw_to_json(df, "ethereum", next_token)

    print(df.head())
    print("Next token:", next_token)

    # Transformation
    transformed_df = df.copy()
    transformed_df['twitter_username'] = transformed_df['twitter_username'].apply(transform_twitter_username)
    transformed_df['instagram_username'] = transformed_df['instagram_username'].apply(transform_instagram_username)
    transformed_df = split_contracts(transformed_df)

    # Loading
    load_raw_to_json(df, "ethereum", next_token)

    selected_columns = ['collection', 'name', 'description', 'image_url', 'owner', 'twitter_username', 'instagram_username', 'chain', 'address']
    transformed_df_selected = transformed_df[selected_columns]

    load_data_to_database(transformed_df_selected)




