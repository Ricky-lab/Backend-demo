# For implementing the functions for managing lobbies and player interactions

import models
from extensions import socketio
import session_utils
lobbies = models.lobbies

# create
def create(playerId, lobbyDetails):
    """
    Creates a new game lobby with details provided by the lobby holder.
    """
    lobbyId = f"lobby_{len(lobbies) + 1}"  # Generate a unique lobby ID
    lobbies[lobbyId] = {
        'holder_id': playerId,
        'limit': lobbyDetails['limit'],
        'players': [playerId]  # Initially, the lobby holder is the only player
    }
    return lobbyId


# Join
def join(playerId, lobbyId):
    """
    Adds a player to the specified lobby if it's not full.
    """
    if lobbyId in lobbies and len(lobbies[lobbyId]['players']) < lobbies[lobbyId]['limit']:
        lobbies[lobbyId]['players'].append(playerId)
        # check if it is ready to start
        startGame(lobbyId)
        return True
    return False

# Leave
def leave(playerId, lobbyId):
    """
    Removes a player from the specified lobby. Deletes the lobby if it becomes empty.
    """
    if lobbyId in lobbies and playerId in lobbies[lobbyId]['players']:
        lobbies[lobbyId]['players'].remove(playerId)
        # Check if the lobby is now empty and delete it if so
        if not lobbies[lobbyId]['players']:
            del lobbies[lobbyId]
        return True
    return False

# StartGame
def startGame(lobbyId):
    """
    Simulates starting a game by deleting the lobby. 
    """
    if lobbyId in lobbies and len(lobbies[lobbyId]['players']) == lobbies[lobbyId]['limit']:
        del lobbies[lobbyId]
        return True
    return False

# notify players
def notifyPlayers(lobbyId, message):
    """
    Notifies all players in a lobby using WebSocket.
    """
    from session_utils import get_session_id_for_player  # Ensure correct import path

    if lobbyId in models.lobbies:
        players = models.lobbies[lobbyId]['players']
        for playerId in players:
            session_id = get_session_id_for_player(playerId)
            if session_id:
                # Emit the notification only to this player's session
                socketio.emit('lobby_notification', {'message': message, 'lobbyId': lobbyId}, room=session_id)
        return True
    return False