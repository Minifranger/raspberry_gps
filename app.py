#!/usr/bin/python3.5
from gps3 import gps3
import loggers

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        if type(data_stream.TPV["lat"]) is float and type(data_stream.TPV["lon"]) is float:
            loggers.gps_data.info("Latitude = {lat}, Longitude = {lon}".format(lat="%.8f" % (data_stream.TPV["lat"]),
                                                                               lon="%.8f" % (data_stream.TPV["lon"])))
