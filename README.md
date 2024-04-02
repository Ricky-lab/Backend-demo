# Funnect - Where Fun Meets Connection

Funnect is an innovative platform that bridges the gap between fun and connection, allowing users to dive into the heart of gaming with ease. By offering seamless access to vibrant gaming communities and multiplayer experiences, Funnect aims to create unforgettable moments of joy and camaraderie in real-time.

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
