from log import loggers


class Sensor(object):

    def __init__(self, socket, stream):
        self.socket = socket
        self.stream = stream

    def connect(self):
        loggers.logger.info("Connecting sensor {self}".format(self=self))
        self.socket.connect()
        self.socket.watch()


def check_data(lat, lon):
    return isinstance(lat, float) and isinstance(lon, float)
