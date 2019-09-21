class Sensor(object):

    def __init__(self, socket, stream):
        self.socket = socket
        self.stream = stream

    def connect(self):
        self.socket.connect()
        self.socket.watch()
        # return self.socket, self.stream

# def start_stream():
#     gps_socket = gps3.GPSDSocket()
#     data_stream = gps3.DataStream()
#     gps_socket.connect()
#     gps_socket.watch()
#     return gps_socket, data_stream


def check_data(lat, lon):
    return isinstance(lat, float) and isinstance(lon, float)
