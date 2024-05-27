from itertools import chain
import pandas as pd
import json
import os
import psycopg2
from psycopg2.extras import execute_values

def load_raw_to_json(df, chain, next_token):
    if next_token is not None:
        filename = f"{chain}_{next_token}.json"
    else:
        filename = f"{chain}_first_page.json"

    df.to_json(f"/home/user/PycharmProjects/OpenSea-ETL/raw_data/{filename}",  orient = "records", indent = 4)


def load_data_to_database(transformed_df_selected):
    try:
       conn = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="postgres", port="5432")
       cur = conn.cursor()

       cur.execute("""
               CREATE TABLE IF NOT EXISTS opensea_collections (
                   id SERIAL PRIMARY KEY,
                   collection VARCHAR,
                   name VARCHAR,
                   description TEXT,
                   image_url VARCHAR,
                   owner VARCHAR,
                   twitter_username VARCHAR,
                   instagram_username VARCHAR,
                   chain TEXT,
                   address VARCHAR
               )
       """)

       for index, row in transformed_df_selected.iterrows():
           cur.execute("""
                      INSERT INTO opensea_collections (collection, name, description, image_url, owner, twitter_username, instagram_username, chain, address)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                  """, (
           row['collection'], row['name'], row['description'], row['image_url'], row['owner'], row['twitter_username'],
           row['instagram_username'], row['chain'], row['address']))

       conn.commit()
       cur.close()
       conn.close()

    except psycopg2.Error as e:
        print(e)


