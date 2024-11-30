# Chat System Application

This is a simple chat system project consisting of a back-end RESTful API built with FastAPI and a front-end user interface using React. The system allows a user to chat with an agent, providing an interactive experience with basic validations and dynamic responses.

---

## Features

- **Front-End**: Interactive chat interface built with React and the `react-chat-widget`.
- **Back-End**: RESTful API created with FastAPI for handling user messages and providing agent responses.
- **Chat Validation**: Ensures valid chat history (alternating "user" and "agent" messages).
- **Personalized Responses**: The agent's replies are dynamic and slightly personalized.
- **Modern UI Design**: A clean, minimalist design with a gradient background.

---

## Project Structure

├── front/chat-app # Front-end React application
│ ├── src/
│ │ ├── App.js # Main component for the chat system
│ │ ├── App.css # Styling for the chat interface
│ │ └── index.js # Entry point for the React app
│ └── package.json # Dependencies for the React app
├── back/ # Back-end FastAPI server
│ ├── main.py # Main FastAPI application
│ ├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## Requirements

### Front-End

- Node.js (v16 or higher)
- npm or yarn

### Back-End

- Python 3.9 or higher
- FastAPI
- Uvicorn (ASGI server)

---

## Installation and Setup

### Back-End

1. Navigate to the `back/` folder:
   ```bash
   cd back
   ```
   python -m venv env
   source env/bin/activate # For Linux/Mac
   env\Scripts\activate # For Windows
   pip install -r requirements.txt
   uvicorn main:app --reload
   The back-end server will be available at http://127.0.0.1:8000.

### Front-End

1. Navigate to the front/ folder
   cd front
   npm install
   npm start
   http://localhost:3000

### How to Use

1. Open the React application in your browser (http://localhost:3000).
2. Type a message in the chat box and send it.
3. The back-end server will process the message and reply with the agent’s response.
4. The entire chat history will be displayed in the chat widget.

### Testing

API Testing: http://localhost:8000/docs
