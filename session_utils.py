player_sessions = {}  # Global storage for player sessions

def get_session_id_for_player(player_id):
    return player_sessions.get(player_id)

def update_player_session(player_id, session_id):
    player_sessions[player_id] = session_id

def remove_player_session(player_id):
    player_sessions.pop(player_id, None)
