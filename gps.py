from gps3 import gps3


def start_stream():
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()
    return gps_socket, data_stream


def check_data(lat, lon):
    return isinstance(lat, float) and isinstance(lon, float)
