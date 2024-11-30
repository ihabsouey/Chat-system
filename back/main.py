from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

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
    
    # Generate static agent response
    return {"reply": "Thank you for your message! This is a static reply."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
