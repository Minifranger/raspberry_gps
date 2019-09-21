import socketio
from time import sleep

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('newnumber', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
print("trying to sent response")
while True:

    sio.emit('newnumber', {'number': 1})
    sleep(2)
    print("sent my response")
# sio.disconnect()
