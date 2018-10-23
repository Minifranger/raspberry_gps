import sqlite3
import properties

conn = sqlite3.connect(properties.GPS_DB)
c = conn.cursor()

for row in c.execute(""" SELECT * FROM gps_data """):
    print(row)
