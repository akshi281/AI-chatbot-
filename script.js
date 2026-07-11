const chatBox = document.getElementById("chatBox");
const messageInput = document.getElementById("message");
const sendBtn = document.getElementById("sendBtn");
const newChatBtn = document.getElementById("newChatBtn");
const clearBtn = document.getElementById("clearChat");
const typing = document.getElementById("typing");
const chatHistory = document.getElementById("chatHistory");

const API_URL = "http://127.0.0.1:8000";

let conversationId = null;

// ==========================
// Create New Chat
// ==========================
// ==========================
// Create New Chat
// ==========================
async function createNewChat() {

    const response = await fetch(`${API_URL}/new_chat`, {
        method: "POST"
    });

    const data = await response.json();

    conversationId = data.conversation_id;

    chatBox.innerHTML = "";

    // Welcome message
    chatBox.innerHTML = `
        <div class="welcome">
            <div class="bot-icon">🤖</div>
            <h2>Welcome!</h2>
            <p>Start chatting with your AI assistant.</p>
        </div>
    `;

    await loadConversations();

}

// ==========================
// Add Message
// ==========================
function addMessage(text, sender) {

    const div = document.createElement("div");

    div.className = sender === "user"
        ? "message user"
        : "message bot";

    div.innerHTML = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// ==========================
// Send Message
// ==========================
// ==========================
// Send Message
// ==========================
async function sendMessage() {

    const message = messageInput.value.trim();

    if (!message) return;

    // Conversation lekapothe automatic ga create cheyyi
    if (!conversationId) {

        console.log("No conversation. Creating...");

        await createNewChat();
    }

    // Create fail ayithe maatrame stop
    if (!conversationId) {

        alert("Unable to create conversation.");

        return;
    }

    // Remove welcome screen
    const welcome = chatBox.querySelector(".welcome");

    if (welcome) {
        welcome.remove();
    }

    addMessage(message, "user");

    messageInput.value = "";

    typing.classList.remove("hidden");

    try {

        const response = await fetch(`${API_URL}/chat`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                conversation_id: conversationId,
                message: message
            })

        });

        if (!response.ok) {

            throw new Error(`Chat API Error: ${response.status}`);

        }

        const data = await response.json();

        console.log("CHAT RESPONSE:", data);

        typing.classList.add("hidden");

        addMessage(data.response, "bot");

        await loadConversations();

    } catch (error) {

        console.error("SEND MESSAGE ERROR:", error);

        typing.classList.add("hidden");

        addMessage("Server Error!", "bot");

    }
}
// ==========================
// Load Conversations
// ==========================
async function loadConversations() {

    try {

        const response = await fetch(`${API_URL}/conversations`);

        const chats = await response.json();

        chatHistory.innerHTML = "";

       chats.forEach(chat => {

    // Hide empty chats
    if (chat.title === "New Chat") {
        return;
    }

    const div = document.createElement("div");

    div.className = "history-item";

    div.innerHTML = `
        <div class="history-content">
            <span onclick="loadConversation('${chat.id}')">
                ${chat.title}
            </span>

            <button onclick="event.stopPropagation(); deleteChat('${chat.id}')">
                🗑
            </button>
        </div>
    `;

    chatHistory.appendChild(div);

});

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================
// Load Selected Conversation
// ==========================
async function loadConversation(id) {

    try {

        conversationId = id;

        const response = await fetch(`${API_URL}/conversation/${id}`);

        const messages = await response.json();

        chatBox.innerHTML = "";

        messages.forEach(msg => {

            addMessage(
                msg.content,
                msg.role === "user" ? "user" : "bot"
            );

        });

    }

    catch (error) {

        console.error(error);

    }

}

// ==========================
// Delete Chat
// ==========================
async function deleteChat(id) {

    await fetch(`${API_URL}/conversation/${id}`, {

        method: "DELETE"

    });

    if (conversationId === id) {

        chatBox.innerHTML = ""

        conversationId = null;

    }

    await loadConversations();

}

// ==========================
// Clear All Chats
// ==========================
async function clearAllChats() {

    if (!conversationId) return;

    await fetch(`${API_URL}/conversation/${conversationId}/messages`,{
    method: "DELETE"
});
    chatBox.innerHTML = "";

}

// ==========================
// Events
// ==========================
sendBtn.addEventListener("click", function (e) {
    e.preventDefault();
    sendMessage();
});

messageInput.addEventListener("keydown", function (e) {

    if (e.key === "Enter" && !e.shiftKey) {

        e.preventDefault();

        sendMessage();

    }

});

newChatBtn.addEventListener("click", createNewChat);

clearBtn.addEventListener("click", clearAllChats);


// ==========================
// Start App
// ==========================
async function startApp() {

    await loadConversations();

    const response = await fetch(`${API_URL}/conversations`);

    const chats = await response.json();

    if (chats.length > 0) {

        conversationId = chats[0].id;

        await loadConversation(conversationId);

    } else {

        await createNewChat();

    }

}

startApp();