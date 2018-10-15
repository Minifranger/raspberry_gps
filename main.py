#!/usr/bin/python3.5
from gps3 import gps3
import loggers
import sqlite3
import properties

conn = sqlite3.connect(properties.GPS_DB)
c = conn.cursor()

c.execute(""" CREATE TABLE if not exists gps_data (date text, lat float, lon float) """)

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        if type(data_stream.TPV["lat"]) is float and type(data_stream.TPV["lon"]) is float:
            c.execute(""" INSERT INTO gps_data(date, lat, lon) VALUES (?, ?, ?); """, (data_stream.TPV["time"],
                                                                                       "%.8f" % (data_stream.TPV["lat"]),
                                                                                       "%.8f" % (data_stream.TPV["lon"])))
            conn.commit()
            loggers.gps_data.info("Latitude = {lat}, Longitude = {lon}".format(lat="%.8f" % (data_stream.TPV["lat"]),
                                                                               lon="%.8f" % (data_stream.TPV["lon"])))
conn.close()
