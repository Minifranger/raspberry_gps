#!/usr/bin/python3.5
import gps
import loggers
import db
import properties
from datetime import datetime

conn, c = db.start_db(name=properties.GPS_DB)

gps_socket, data_stream = gps.start_stream()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        time = datetime.strptime(data_stream.TPV["time"], '%Y-%m-%dT%H:%M:%S.%fZ')
        lat, lon = data_stream.TPV["lat"], data_stream.TPV["lon"]
        if gps.check_data(lat=lat, lon=lon):
            c.execute(""" INSERT INTO gps_data(date, lat, lon) VALUES (?, ?, ?); """, (time, lat, lon))
            conn.commit()
            loggers.gps_data.info("Latitude = {lat}, Longitude = {lon}".format(lat=lat, lon=lon))
conn.close()
