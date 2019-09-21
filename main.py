#!/usr/bin/python3.5
import sensor
import loggers
from gps3 import gps3
import properties
import db
import sensor

gps_db = db.MetaDatabase(name=properties.GPS_DB)
gps_table = db.MetaTable(name="gps_table", schema="date text, lat float, lon float")
gps_db.create_table(gps_table)
print(gps_db.list_tables())

gps_sensor = sensor.Sensor(socket=gps3.GPSDSocket(), stream=gps3.DataStream())
gps_sensor.connect()
# conn, c = db.start_db(name=properties.GPS_DB)

# gps_socket, data_stream = gps.start_stream()
for new_data in gps_sensor.socket:
    if new_data:
        gps_sensor.stream.unpack(new_data)
        print(new_data)
#         time, lat, lon = data_stream.TPV["time"], data_stream.TPV["lat"], data_stream.TPV["lon"]
#         if gps.check_data(lat=lat, lon=lon):
#             c.execute(""" INSERT INTO gps_data(date, lat, lon) VALUES (?, ?, ?); """, (time, lat, lon))
#             conn.commit()
#             loggers.gps_data.info("Latitude = {lat}, Longitude = {lon}".format(lat=lat, lon=lon))
# conn.close()
