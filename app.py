from flask import Flask, request
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)

# Routing endpoints

if __name__ == '__name__':
    socketio.run(app, debug = True)