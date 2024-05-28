from setting import dbname, user, host, password, port
import psycopg2

def load_raw_to_json(df, chain, next_token):
    if next_token: #removed is not None
        filename = f"{chain}_{next_token}.json"
    else:
        filename = f"{chain}_first_page.json"

    # no longer using absolute path
    df.to_json(f"raw_data/{filename}",  orient = "records", indent = 4)


def load_data_to_database(transformed_df_selected):
    try:
       # importing postgres values from setting rather than declaring them here
       conn = psycopg2.connect(dbname, user, host, password, port)
       cur = conn.cursor()

        # TODO: this is too hardcoded, save the query in separate variable, for isntance save it as CREATE_TABLE_QUERY in constants.py or queries.py
        #TODO: when creating a table specify types, include len of VARCHAR for example to save up memory
       # TODO: it would be best if you can create tables dinamically, have table schema as json, build the query like that
       #TODO: every time you use load_data_to_database function, it will check the table existance, move this functionality as a separate fucntion

       #creating query in constants.py
       cur.execute(create_table_query)


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



