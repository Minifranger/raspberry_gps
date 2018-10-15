import sqlite3
import properties

conn = sqlite3.connect(properties.GPS_DB)
c = conn.cursor()

c.execute(""" CREATE TABLE if not exists gps_data (date text, lat real, lon real) """)