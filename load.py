from setting import dbname, user, host, password, port
from constants import create_table_query, insert_data_query
from psycopg2.extras import execute_values
import psycopg2
import logging
import json

def load_raw_to_json(df, chain, next_token):
    if next_token:
        filename = f"{chain}_{next_token}.json"
    else:
        filename = f"{chain}_first_page.json"

    df.to_json(f"raw_data/{filename}",  orient = "records", indent = 4)


def check_table_existence(conn, table_name):
    cur = conn.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    exists = cur.fetchone()[0]
    cur.close()
    return exists

def table_name_from_schema(conn, table_name, schema):
    cur = conn.cursor()
    columns = ", ".join(f"{column_name} {data_type}" for column_name, data_type in schema.items())
    cur.execute(f"CREATE TABLE {table_name} ({columns})")
    conn.commit()
    cur.close()

def load_data_to_database(df_selected, dbname, user, host, password, port):
    try:
       conn = psycopg2.connect(dbname=dbname, user=user, host=host, password=password, port=port)
       cur = conn.cursor()

       cur.execute(create_table_query)

       records = df_selected.values.tolist()
       execute_values(cur, insert_data_query, records)

       conn.commit()
       cur.close()
       conn.close()

    except psycopg2.Error as e:
        logging.error(f"Error occured: {e}")

