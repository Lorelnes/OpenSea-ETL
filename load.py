from itertools import chain # TODO: why do you need chain from itertools
import pandas as pd #TODO: not used
import json #TODO: not used
import os #TODO: you are importing and note using modules at all
import psycopg2
from psycopg2.extras import execute_values #TODO: not used


def load_raw_to_json(df, chain, next_token):
    
    
    if next_token is not None: # you can simply say if next_token (please review truthy and falsy values in python)
        filename = f"{chain}_{next_token}.json"
    else:
        filename = f"{chain}_first_page.json"

    # no need to specify full path
    df.to_json(f"/home/user/PycharmProjects/OpenSea-ETL/raw_data/{filename}",  orient = "records", indent = 4)


def load_data_to_database(transformed_df_selected):
    try:
       # TODO: try saving postgres variables in seaprate file, for instance in setting.py, config.yaml or anything similar
       # TODO: save them as constants and then import as needed (e.g DBNAME='postgres', USER='postgres')
       conn = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="postgres", port="5432")
       cur = conn.cursor()

        # TODO: this is too hardcoded, save the query in separate variable, for isntance save it as CREATE_TABLE_QUERY in constants.py or queries.py
        #TODO: when creating a table specify types, include len of VARCHAR for example to save up memory
       # TODO: it would be best if you can create tables dinamically, have table schema as json, build the query like that
       #TODO: every time you use load_data_to_database function, it will check the table existance, move this functionality as a separate fucntion
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

        #TODO: you are loading rows in database one by one, look up batch loading and try to do the same
       for index, row in transformed_df_selected.iterrows():
           cur.execute("""
                      INSERT INTO opensea_collections (collection, name, description, image_url, owner, twitter_username, instagram_username, chain, address)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                  """, (
           row['collection'], row['name'], row['description'], row['image_url'], row['owner'], row['twitter_username'],
           row['instagram_username'], row['chain'], row['address']))
           # TODO: in python we have unpacking operators *, ** (look them up) might come in handy in this case

       conn.commit()
       cur.close()
       conn.close()

    except psycopg2.Error as e:
        print(e) # TODO: printing an error does not do anythign, firstly try to log it. handle errors more logically



