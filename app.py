from gps3 import gps3
import loggers

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        # print("Latitude = {lat}".format(lat=data_stream.TPV['lat']),
        #       "Longitude = {lon}".format(lon=data_stream.TPV['lon']))
        print(type(data_stream.TPV["lat"]))
        loggers.gps_data.info("Latitude = {lat}".format(lat=data_stream.TPV["lat"]))

