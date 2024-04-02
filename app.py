from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('create_lobby')
def handle_create_lobby(data):
    playerId = data['playerId']
    lobbyId = "some_unique_id" 
    
    # Now broadcast the update
    socketio.emit('update_lobbies', {'lobbies': [{'id': lobbyId, 'info': 'New Lobby Created'}]})


@app.route('/')
def index():
    return render_template('index.html')  

if __name__ == '__main__':
    socketio.run(app, debug=True)
