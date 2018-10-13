import gps3

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print("Longitude = {lon}".format(lon=data_stream.TPV['lon']), "Latitude = {lat}".format(lat=data_stream.TPV['lat']))

