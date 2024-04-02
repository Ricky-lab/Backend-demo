from flask import Flask, render_template, request, redirect, url_for, flash, session
from extensions import socketio


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for session management and flash messages
socketio.init_app(app)

import models
from lobby_manager import create, join, leave, notifyPlayers


@app.route('/')
def index():
    return render_template('login.html')  

@app.route('/lobby')
def lobby():
    if 'user_id' not in session:
        # If the user is not logged in, redirect to login page
        flash('Please log in to view this page.', 'warning')
        return redirect(url_for('login'))
    
    # Fetch and pass the lobbies to the lobby template
    return render_template('index.html', lobbies=models.lobbies)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email)
        print(password)

        user = models.users.get(email)
        if user and user['password'] == password:
            # Log the user in:
            session['user_id'] = user['player_id']
            session['first_name'] = user['first_name']
            session['last_name'] = user['last_name']
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
        # key: email, value: {'first_name': str, 'last_name': str, 'password': str, 'player_id': str}
        models.users[email] = {
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
            'player_id': player_id
        }
        flash('Registration successful. Please log in.', 'success')
        print(models.users)
        return redirect(url_for('login'))

    return render_template('signup.html')


@socketio.on('create_lobby')
def handle_create_lobby(data):
    playerId = data['playerId']
    limit = data['limit']
    lobbyDetails = {'holder_name': 'Placeholder Name', 'limit': limit}
    create(playerId, lobbyDetails)
    # Emit an update to all clients about the new lobby
    # socketio.emit('update_lobbies', {'lobbies': models.lobbies.values()})


if __name__ == '__main__':
    socketio.run(app, debug=True)
