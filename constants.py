url = 'https://api.opensea.io/api/v2/collections'

headers = {
    "Accept": "application/json",
    "X-API-KEY": "dacdcd35228a40638599c4c33ceb4a74"
}

params = {
    'chain': "ethereum",
    'next': None

}

selected_columns = ['collection', 'name', 'description', 'image_url', 'owner', 'twitter_username', 'instagram_username',
                    'chain', 'address']

create_table_query = (
    """ CREATE TABLE IF NOT EXISTS opensea_collections (
                   id SERIAL PRIMARY KEY,
                   collection VARCHAR,
                   name VARCHAR, 
                   description TEXT,
                   image_url VARCHAR,
                   owner VARCHAR,
                   twitter_username VARCHAR,
                   instagram_username VARCHAR,
                   chain TEXT,
                   address VARCHAR """)

