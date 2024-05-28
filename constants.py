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

create_table_query = """
CREATE TABLE IF NOT EXISTS opensea_collections_2nd (
                   id SERIAL PRIMARY KEY,
                   collection VARCHAR(255),
                   name VARCHAR(255),
                   description TEXT,
                   image_url VARCHAR(255),
                   owner VARCHAR(255),
                   twitter_username VARCHAR(255),
                   instagram_username VARCHAR(255),
                   chain TEXT,
                   address VARCHAR(255)
);
"""

insert_data_query = """
INSERT INTO opensea_collections_2nd (collection, name, description, image_url, owner, twitter_username, instagram_username, chain, address)
VALUES %s
"""

