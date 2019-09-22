import socketio
from time import sleep


sio = socketio.Client()


@sio.event
def connect():
    print("Connection established")


@sio.event
def disconnect():
    print("Disconnected from server")


sio.connect('http://localhost:5000')
# new_data = {"lat": 1, "lon": 5}
# while True:
#     sio.emit("new_data", new_data)
#     print("sent {new_data}".format(new_data=new_data))
#     sleep(2)
# sio.disconnect()
