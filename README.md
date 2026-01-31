# 🤖 Convo-Pro — ChatGPT-like Conversational AI App

Convo-Pro is a **ChatGPT-style conversational AI application** built using **LangChain**, **Groq LLMs**, **Streamlit**, and **MongoDB**.  
It delivers a **real-time streaming chat experience**, supports **persistent conversation history**, and follows a **modular, production-ready architecture**.

---

## 🚀 Features

- ⚡ **Real-time token-level streaming responses** (ChatGPT-like typing)
- 🧠 **Groq-powered LLM inference** via LangChain
- 💬 **Persistent chat history** with MongoDB
- 🏷️ **Automatic chat title generation** using LLM prompts
- 🗑️ **Per-conversation delete functionality**
- 🔁 **Multiple conversations** with sidebar navigation
- 🎯 **System-prompt controlled formatting** (clean Markdown & LaTeX math)
- 🧩 **Modular and scalable backend design**

---

## 🛠️ Tech Stack

- **Language:** Python  
- **LLM Framework:** LangChain  
- **LLM Provider:** Groq (LLaMA models)  
- **UI Framework:** Streamlit  
- **Database:** MongoDB (PyMongo)  

**Core Concepts:**
- Streaming responses  
- Prompt engineering  
- Session state management  
- Clean architecture & separation of concerns  

---

## 📂 Project Structure
```
convo-pro/
│
├── config/
│ └── settings.py # Environment & config management
│
├── llm_factory/
│ └── get_llm.py # Groq LLM initialization & streaming
│
├── services/
│ ├── chat_utilities.py # Chat logic (streaming, formatting)
│ ├── get_title.py # Auto chat title generation
│ └── get_models_list.py # Available Groq models
│
├── db/
│ └── conversations.py # MongoDB conversation storage
│
├── main.py # Streamlit application
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/abhijeet-shakya/convopro-private-chatgpt.git
cd convo-pro
```

### 2️⃣ Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables
Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL="llama-3.1-8b-instant,groq/compound,openai/gpt-oss-120b"

MONGO_DB_URL=mongodb://localhost:27017
MONGO_DB_NAME=convo_pro
```
### 5️⃣ Run MongoDB
Make sure MongoDB is running locally or update the URI for a cloud instance.

### 6️⃣ Run the application
```bash
streamlit run main.py
```


## 🧠 How It Works (High-Level)
- User enters a message in the Streamlit UI
- Chat history is stored in `st.session_state`
- Messages are converted into LangChain `Message` objects
- Groq LLM streams tokens in real-time
- Responses are rendered incrementally in the UI
- Conversations and messages are persisted in MongoDB

## 🎯 Prompt Engineering
The app uses system prompts to control:
- Output length (token limits)
- Markdown formatting
- Concise, structured responses
This ensures clean, readable answers, especially for technical topics.


## 🚀 Future Enhancements
- 📚 RAG (PDF / document chat)
- 🔐 User authentication
- 🌐 Deployment
- 🐳 Docker support

## Author
**Abhijeet Shakya**
🔗 GitHub: https://github.com/abhijeet-shakya








