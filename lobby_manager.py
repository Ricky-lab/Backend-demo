# For implementing the functions for managing lobbies and player interactions

import models
from extensions import socketio
lobbies = models.lobbies

# create
def create(playerId, lobbyDetails):
    """
    Creates a new game lobby with details provided by the lobby holder.
    """
    lobbyId = f"lobby_{len(lobbies) + 1}"  # Generate a unique lobby ID
    lobbies[lobbyId] = {
        'holder_id': playerId,
        'holder_name': lobbyDetails['holder_name'],
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
    if lobbyId in lobbies:
        # Retrieve all player IDs in the lobby
        players = lobbies[lobbyId]['players']
        for playerId in players:
            # TBD
            # socketio.emit('notification', {'message': message}, to=player_session_id)
            pass
        # For demonstration, just broadcast to all connected clients
        socketio.emit('notification', {'lobbyId': lobbyId, 'message': message})
        return True
    return False