#!/usr/bin/python3.5
from gps3 import gps3
import properties
from db import db
from sensor import sensor
# from socket_gps import sio


gps_db = db.MetaDatabase(path=properties.GPS_DB)
gps_table = db.MetaTable(name="gps_table", schema="date text, lat float, lon float")
gps_db.create_table(gps_table)
print(gps_db.list_tables())

gps_sensor = sensor.Sensor(socket=gps3.GPSDSocket(), stream=gps3.DataStream())
gps_sensor.connect()

for new_data in gps_sensor.socket:
    if new_data:
        gps_sensor.stream.unpack(new_data)
        time, lat, lon = gps_sensor.stream.TPV["time"], gps_sensor.stream.TPV["lat"], gps_sensor.stream.TPV["lon"]
        if sensor.check_data(lat, lon):
            print("lat = {lat} - lon = {lon}".format(lat=lat, lon=lon))
            sio.emit("dbs", gps_sensor.stream.TPV)
