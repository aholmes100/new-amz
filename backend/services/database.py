import sqlite3
import pandas as pd


def save_to_sql(data, table_name="ad_performance"):
    conn = sqlite3.connect('amazon_ads.db')
    data.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print("Data saved to SQL database successfully.")
