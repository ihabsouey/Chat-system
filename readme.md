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

![image](https://github.com/user-attachments/assets/b753af39-0ceb-4204-879b-1610fcad0e12)


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

   ```bash
   python -m venv env
   ```

   ```bash
   source env/bin/activate # For Linux/Mac
   env\Scripts\activate # For Windows
   ```

   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   uvicorn main:app --reload
   ```

   The back-end server will be available at http://127.0.0.1:8000.

### Front-End

1. Navigate to the front/ folder

```bash
  cd front
```

```bash
    npm install
```

```bash
    npm start
```

http://localhost:3000

### How to Use

1. Open the React application in your browser (http://localhost:3000).
2. Type a message in the chat box and send it.
3. The back-end server will process the message and reply with the agent’s response.
4. The entire chat history will be displayed in the chat widget.

### Testing

API Testing: http://localhost:8000/docs

