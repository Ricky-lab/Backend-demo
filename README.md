# Funnect - Where Fun Meets Connection
Hey here is developer Ricky 😃 <br><br>
Funnect is an innovative platform that bridges the gap between fun and connection, using `Flask`. For the testing and reviewing convinience, I decide not to use any database (even in the lightweight one). Hence, I use the in-memory data structure to store the related data, which are well designed to join each other.<br> <br>
Even this project would just blink for a while in my life but I won't think lowly of this. Each experience for me is so valuable. Hence, I am willing to assign all it deserves, including basical `login` and `signup` functions with basic UI. Hope you like my porject!<br>

## Follow up?
Ofc, I already have some ideas on our follow-up questions and I do some thinking on these. Here are my ideas and notes: [Follow-Up](follow_up.md)

## Setup and Running 🧰

### Prerequisites

Before you begin, ensure you have Python 3.x installed on your system. It's recommended to use a virtual environment for Python projects to manage dependencies effectively.

### Installation

1. Clone the repository to your local machine (on your terminal):
```
git clone https://github.com/Ricky-lab/Funnect.git
```
2. Navigate to the project directory:
```
cd Funnect
```
3. Create a virtual environment:
- For macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
- For Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
### Running the Application

To start the application, run:
```
python app.py
```


## System Interaction 👣

### API Endpoints

- `/login` - POST request to authenticate users.
- `/signup` - POST request for user registration.
- `/lobby` - GET request to fetch the lobby page after login.

### WebSocket Events

- `connect` - Event triggered when a client connects to the server.
- `disconnect` - Event triggered when a client disconnects.
- `create_lobby` - Event for creating a new game lobby.
- `join_lobby` - Event for joining an existing game lobby.
- `leave_lobby` - Event for leaving a game lobby.
- `notify_lobby` - Event for sending notifications to all players in a lobby.

## Project Structure 🏠

- `app.py` - The main entry point of the application, initializing Flask and Socket.IO.
- `models.py` - Defines the data models and interactions with the database.
- `lobby_manager.py` - Manages lobby creation, joining, leaving, and notifications.
- `session_utils.py` - Utility functions for managing user sessions.
- `requirements.txt` - Contains all the necessary Python package dependencies.

## For testing 🧪
My testing way are really `brute force`: using three account to login at the same time and do the interactions among them.<br>
Here are the accounts from the in-memory database, and remember to use `Email` and `Pw` to login:
```
Name: John Doe, Email: 1@e.com, Pw: 123
Name: Jane Doe, Email: 2@e.com, Pw: 123
Name: Alice Smith, Email: 3@e.com, Pw: 123
...
(For more accounts' info, you can have a look in models.py)
```
You absolutely can sign up new one for yourself, only if your email `has not been registered` previously. (Yes I implement this verification as well~)

## Further Improvements 🤔

While Funnect provides a solid foundation for real-time online gaming and community engagement, several areas could enhance its functionality and user experience:

1. **Authentication Security**: Implement OAuth or similar for more secure authentication.
2. **Database Integration**: Use Flask-SQLAlchemy for persistent storage of user and lobby data.
3. **Frontend Enhancements**: Develop a more interactive and responsive UI with frameworks like React or Vue.js.
4. **Scalability**: Optimize the backend for scalability using Docker and Kubernetes for containerization and orchestration.
5. **Testing**: Increase test coverage for both frontend and backend components to ensure reliability.

## Comment: 😃

I wanted to take a moment to share my genuine excitement and the sheer joy I experienced while working on this project. From conceptualizing the idea of Funnect, where fun meets connection, to tackling the technical challenges of bringing it to life, every step of the process and further ideas have been thoroughly engaging and immensely rewarding.

As I submit this project for your review, I do so with the hope that it marks the beginning of a journey rather than a singular checkpoint. I am eagerly looking forward to the possibility of exploring further crossroads with your innovative team. Whether it be refining Funnect or embarking on new projects, I am excited about the potential to contribute to your vision and to make a positive impact together.

Thank you for considering my work and for the opportunity to engage in this exciting challenge. I am truly looking forward to any future interactions we might have and the chance to potentially join your dynamic team. -Yuehui 😸
