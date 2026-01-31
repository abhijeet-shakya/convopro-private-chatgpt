import streamlit as st

from services.get_models_list import get_groq_model_list
from services.get_title import get_chat_title
from services.chat_utilities import get_answer
from db.conversations import (
    create_new_conversation,
    add_message,
    get_conversation,
    get_all_conversations,
    delete_conversation
)

st.set_page_config(page_title="ChatGPT Clone (Groq)", page_icon="💬", layout="centered")
st.markdown(
    """
    <style>
    /* Hide delete icon by default */
    div[data-testid="column"]:has(button[aria-label="Delete"]) {
        opacity: 0;
        transition: opacity 0.15s ease-in-out;
    }

    /* Show delete icon when row is hovered */
    div[data-testid="horizontal-block"]:hover
    div[data-testid="column"]:has(button[aria-label="Delete"]) {
        opacity: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🤖 ChatGPT Clone (Groq)")



# ---- Models ----
if "GROQ_MODELS" not in st.session_state:
    st.session_state.GROQ_MODELS = get_groq_model_list()

selected_model = st.selectbox("Select Model", st.session_state.GROQ_MODELS)

# ---- Session state ----
st.session_state.setdefault("conversation_id", None)
st.session_state.setdefault("conversation_title", None)
st.session_state.setdefault("chat_history", [])  # [{role, content}]

# ---- Sidebar: conversations ----
with st.sidebar:
    st.header("💬 Chat History")
    conversations = get_all_conversations()  # {conv_id: title}

    if st.button("➕ New Chat"):
        st.session_state.conversation_id = None
        st.session_state.conversation_title = None
        st.session_state.chat_history = []
        st.rerun()

    for cid, title in conversations.items():
        col1, col2 = st.columns([0.85,0.15])
        
        # ---- Chat title button ----
        with col1:
            is_current = cid == st.session_state.conversation_id
            label = f"**{title}**" if is_current else title

            if st.button(label, key=f"conv_{cid}"):
                doc = get_conversation(cid) or {}
                st.session_state.conversation_id = cid
                st.session_state.conversation_title = doc.get("title", "Untitled")
                st.session_state.chat_history = [
                    {"role": m["role"], "content": m["content"]}
                    for m in doc.get("messages", [])
                ]
                st.rerun()
        
        with col2:
            st.markdown('<div class="delete-btn">', unsafe_allow_html=True)
            if st.button("", icon="🗑️", key=f"delete_{cid}"):
                delete_conversation(cid)

                if st.session_state.conversation_id == cid:
                    st.session_state.conversation_id = None
                    st.session_state.conversation_title = None
                    st.session_state.chat_history = []

                st.rerun()


# ---- Show chat so far ----
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- Chat input ----
user_query = st.chat_input("Ask AI...")
if user_query:
    # 1️⃣ Show + store user message
    st.chat_message("user").markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # 2️⃣ Persist user message
    if st.session_state.conversation_id is None:
        try:
            title = get_chat_title(selected_model, user_query) or "New Chat"
        except Exception:
            title = "New Chat"

        conv_id = create_new_conversation(
            title=title,
            role="user",
            content=user_query,
        )
        st.session_state.conversation_id = conv_id
        st.session_state.conversation_title = title
        
    else:
        add_message(st.session_state.conversation_id, "user", user_query)

    # 3️⃣ Get assistant response (Groq)
    try: 
        with st.chat_message("assistant"):
            assistant_text= st.write_stream(
                get_answer(
                    selected_model,
                    st.session_state.chat_history
                )
            )
    except Exception as e:
        assitant_text = f"[Error getting response: {e}]"
        with st.chat_message("assistant"):
            st.markdown(assistant_text)

    # 4️⃣ Store assistant message in session
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_text}
    )

    # 5️⃣ Persist assistant message
    if st.session_state.conversation_id:
        add_message(
            st.session_state.conversation_id,
            "assistant",
            assistant_text,
        )
    st.rerun()
