from setting import dbname, user, host, password, port
import psycopg2
import logging

def load_raw_to_json(df, chain, next_token):
    if next_token:
        filename = f"{chain}_{next_token}.json"
    else:
        filename = f"{chain}_first_page.json"

    df.to_json(f"raw_data/{filename}",  orient = "records", indent = 4)


def load_data_to_database(transformed_df_selected):
    try:
       conn = psycopg2.connect(dbname=dbname, user=user, host=host, password=password, port=port)
       cur = conn.cursor()

        #TODO: when creating a table specify types, include len of VARCHAR for example to save up memory
       # TODO: it would be best if you can create tables dinamically, have table schema as json, build the query like that
       #TODO: every time you use load_data_to_database function, it will check the table existance, move this functionality as a separate fucntion

       #creating query in constants.py
       cur.execute(create_table_query)

       records = transformed_df_selected.values.tolist()
       execute_values(cur, """
                        INSERT INTO opensea_collections (collection, name, description, image_url, owner, 
                                                        twitter_username, instagram_username, chain, address)
                        VALUES %s
                        """, records)

       conn.commit()
       cur.close()
       conn.close()

    except psycopg2.Error as e:
        logging.error(f"Error occured: {e}")

