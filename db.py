import sqlite3


def start_db(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    c.execute(""" CREATE TABLE if not exists gps_data (date text, lat float, lon float) """)
    return conn, c
