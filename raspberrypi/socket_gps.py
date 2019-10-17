import socketio
from time import sleep


sio = socketio.Client()
sio.connect('http://localhost:5000')

@sio.event
def connect():
    print("Connection established")


@sio.event
def disconnect():
    print("Disconnected from server")


# gps_data = {"lat": 43.614992457, "lon": 1.39491507}
# while True:
#     sio.emit("dbs", gps_data)
#     sleep(1)
# sio.disconnect()
