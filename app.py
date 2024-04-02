from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_socketio import SocketIO
import models
import lobby_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for session management and flash messages
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = models.users.get(email)
        if user and user['password'] == password:
            session['user_id'] = user['player_id']  # Log the user in
            return redirect(url_for('lobby'))  # Redirect to lobby page
        else:
            flash('Invalid email or password', 'error')  # Flash an error message

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email already exists
        if email in models.users:
            flash('Email already exists.', 'error')
            return render_template('signup.html')

        # Simulate a database save operation
        player_id = f'p{len(models.users)+1:04d}'
        models.users[email] = {
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
            'player_id': player_id
        }

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
