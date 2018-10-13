from gps3 import gps3
import loggers

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        loggers.gps_data.info("Latitude = {lat}, Longitude = {lon}".format(lat=data_stream.TPV["lat"][:8],
                                                                           lon=data_stream.TPV["lon"][:8]))
