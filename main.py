from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai import get_ai_response
import uuid

from database import (
    clear_messages,
    create_conversation,
    get_conversations,
    delete_conversation,
    save_message,
    get_messages,
    clear_database,
    update_conversation_title
)

app = FastAPI(title="AI Chatbot API")

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Request Model
# -----------------------------
class ChatRequest(BaseModel):
    conversation_id: str
    message: str


# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "AI Chatbot Backend Running 🚀"
    }


# -----------------------------
# Create New Chat
# -----------------------------
@app.post("/new_chat")
def new_chat():

    conversation_id = str(uuid.uuid4())

    create_conversation(conversation_id)

    return {
        "conversation_id": conversation_id
    }
# -----------------------------
# Chat
# -----------------------------
@app.post("/chat")
def chat(request: ChatRequest):

    try:

        # Save user message
        save_message(request.conversation_id, "user", request.message)

        # Get all messages
        messages = get_messages(request.conversation_id)

        # Update title only for first user message
        user_messages = [m for m in messages if m["role"] == "user"]

        if len(user_messages) == 1:
            update_conversation_title(
                request.conversation_id,
                request.message[:40]
            )

        # AI Response
        ai_response = get_ai_response(messages)

        print(type(ai_response))
        print(ai_response)
        print("----------------")

        # Save AI response
        save_message(
            request.conversation_id,
            "assistant",
            ai_response
        )

        return {
            "response": ai_response
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "response": str(e)
        }
#------------------------
# Get All Conversations
# -----------------------------
@app.get("/conversations")
def conversations():

    return get_conversations()


# -----------------------------
# Get Messages
# -----------------------------
@app.get("/conversation/{conversation_id}")
def conversation(conversation_id: str):

    return get_messages(conversation_id)


# -----------------------------
# Delete Conversation
# -----------------------------
@app.delete("/conversation/{conversation_id}")
def delete_chat(conversation_id: str):

    delete_conversation(conversation_id)

    return {
        "message": "Conversation Deleted Successfully"
    }


# -----------------------------
# Clear Database
# -----------------------------
@app.delete("/conversation/{conversation_id}/messages")
def clear_messages_api(conversation_id: str):

    clear_messages(conversation_id)

    return {
        "message":"Cleared"
    }