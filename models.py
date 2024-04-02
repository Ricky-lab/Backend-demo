# Used for defining the simple in-memory data structures for lobbies and players


# key: email, value: {'first_name': str, 'last_name': str, 'password': str, 'player_id': str}
users = {}  
users['user1@email.com'] = {'first_name': 'John', 'last_name': 'Doe', 'password': '123', 'player_id': 'p0001'}
users['user2@email.com'] = {'first_name': 'Jane', 'last_name': 'Doe', 'password': '456', 'player_id': 'p0002'}
users['user3@email.com'] = {'first_name': 'Alice', 'last_name': 'Smith', 'password': '789', 'player_id': 'p0003'}
users['user4@email.com'] = {'first_name': 'Bob', 'last_name': 'Brown', 'password': '012', 'player_id': 'p0004'}


# Update next_user_id accordingly
next_user_id = len(users) + 1


# key: lobby_id, value: {'holder_name': str, 'holder_id': str, 'limit': int}
lobbies = {}  
lobbies['lobby_1'] = {'holder_name': 'John Doe', 'holder_id': 'p0001', 'limit': 4}
lobbies['lobby_2'] = {'holder_name': 'Jane Doe', 'holder_id': 'p0002', 'limit': 5}
lobbies['lobby_3'] = {'holder_name': 'Alice Smith', 'holder_id': 'p0003', 'limit': 3}


next_user_id = len(users) + 1  #auto-incrementing user IDs