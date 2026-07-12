# 🤖 AI Chatbot

An AI-powered conversational chatbot built using **FastAPI, JavaScript, SQLite, Groq API, and the Llama 3.3 70B model**.

The application provides intelligent AI responses while maintaining conversation history and independent chat sessions through a clean and responsive web interface.

## 🚀 Project Overview

The main objective of this project is to understand and implement the complete workflow of a modern AI-powered conversational application.

The chatbot connects a web-based frontend with a FastAPI backend, SQLite database, and a Large Language Model through the Groq API.

When a user sends a message, the application stores the conversation, maintains the current chat context, sends the conversation history to the AI model, and displays the generated response to the user.

## ✨ Features

- 🤖 AI-powered conversational responses
- 💬 Conversation context management
- 🗂️ Persistent chat history
- 📝 Automatic conversation titles
- 🕘 Recent chat history
- 🔄 Reopen previous conversations
- ➕ Create new conversations
- 🗑️ Delete individual conversations
- 🧹 Clear current chat messages
- ⌨️ AI typing indicator
- 📱 Responsive user interface

## 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- FastAPI
- Uvicorn

### Database

- SQLite

### AI Integration

- Groq API
- Llama 3.3 70B

## 🏗️ System Architecture

User  
↓  
HTML / CSS / JavaScript Frontend  
↓  
REST API Request  
↓  
FastAPI Backend  
↓  
SQLite Database  
↓  
Groq API  
↓  
Llama 3.3 70B Model  
↓  
AI Generated Response  
↓  
FastAPI Backend  
↓  
Frontend  
↓  
User

## ⚙️ How It Works

1. The user enters a message through the chatbot interface.

2. JavaScript sends the message to the FastAPI backend using a REST API request.

3. The backend stores the user message in the SQLite database.

4. Previous messages from the active conversation are retrieved using a unique conversation ID.

5. The complete conversation context is sent to the Llama 3.3 70B model through the Groq API.

6. The AI model generates a response.

7. The backend stores the AI response in the database.

8. The response is returned to the frontend and displayed to the user.

## 🗄️ Database Design

The application mainly uses two database tables.

### Conversations Table

- id
- title
- created_at

### Messages Table

- id
- conversation_id
- role
- content
- created_at

The project uses a **one-to-many relationship**, where one conversation can contain multiple messages.

## 🔐 Environment Variables

Create a `.env` file in the backend project directory.

Add your Groq API key:

GROQ_API_KEY=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

### 🧠 Conversation Context

The chatbot maintains conversation context by retrieving previous messages from the database and sending the complete conversation history to the AI model.

For example:

User: My name is Akshitha.

Assistant: Nice to meet you, Akshitha.

User: What is my name?

The AI can understand the previous context and respond appropriately.

## 🧩 Challenges and Learning

One of the major challenges during development was conversation state management.

Initially, the active conversation was resetting after sending a message. The conversation was stored in the database but had to be reopened from Recent Chats.

This issue was solved by improving conversation ID management and frontend state handling.

Another challenge was the Clear Chat functionality. Initially, it deleted all conversations. The backend logic was redesigned to remove only the messages of the currently selected conversation.

Through this project, I gained practical experience in:

- Frontend state management
- REST API development
- FastAPI
- SQLite database relationships
- AI model integration
- Conversation context management
- Debugging client-server applications

## 🔮 Future Enhancements

Future versions of the project may include:

- 🧠 Permanent user memory
- 🔐 User authentication
- 👥 Multiple user accounts
- 📄 PDF and document-based question answering
- 🔎 Retrieval-Augmented Generation (RAG)
- 🌐 Live web search
- 🎤 Voice input
- 🔊 Voice output
- 🖼️ Image understanding
- ⚡ Streaming AI responses

## 🎯 Project Objective

This project demonstrates that building an AI application involves more than simply connecting an AI API.

It combines frontend development, backend API design, database management, conversation state handling, and Large Language Model integration.

## 👨‍💻 Developer

**Akshitha Reddy**

AI Chatbot Project  
K-HUB Project

## 📄 License

This project is developed for educational and learning purposes.
