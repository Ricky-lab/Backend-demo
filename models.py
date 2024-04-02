# Used for defining the simple in-memory data structures for lobbies and players


# key: email, value: {'first_name': str, 'last_name': str, 'password': str, 'player_id': str}
users = {}  

# key: lobby_id, value: {'holder_name': str, 'holder_id': str, 'limit': int}
lobbies = {}  

next_user_id = len(users) + 1  #auto-incrementing user IDs