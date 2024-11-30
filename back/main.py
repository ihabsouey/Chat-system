import random
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplacez par ["http://localhost:3000"] pour plus de sécurité
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes HTTP (POST, GET, OPTIONS, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)
class Message(BaseModel):
    role: str  # 'user' or 'agent'
    content: str

class ChatHistory(BaseModel):
    messages: List[Message]

@app.post("/chat/")
async def chat_endpoint(chat: ChatHistory):
    # Validate chat history
    for i in range(len(chat.messages) - 1):
        if chat.messages[i].role == chat.messages[i + 1].role:
            raise HTTPException(status_code=400, detail="Invalid chat history")
    
    user_message = chat.messages[-1].content.lower()
    print(f"User message: {user_message}")

    greetings = ["Hi there!", "Hello!", "Hey!"]
    thank_you_responses = ["You're welcome!", "Glad to be of help!", "My pleasure!"]

    if "hi" in user_message or "hello" in user_message:
        reply = random.choice(greetings)
    elif "thank you" in user_message:
        reply = random.choice(thank_you_responses)
    else:
        reply = "How can I assist you further?"

    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
