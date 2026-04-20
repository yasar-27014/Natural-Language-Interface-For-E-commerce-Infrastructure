import streamlit as st
from responses import get_response

# ── Page config ──────────────────────────────────────────
st.set_page_config(
    page_title="ShopEase Chatbot",
    page_icon="🛒",
    layout="centered"
)

# ── Custom CSS ───────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #f0f2f5;
    }

    /* Chat message bubbles */
    .user-bubble {
        background-color: #dcf8c6;
        padding: 10px 16px;
        border-radius: 12px 12px 2px 12px;
        margin: 6px 0;
        margin-left: 20%;
        font-size: 15px;
        color: #212121;
    }

    .bot-bubble {
        background-color: #ffffff;
        padding: 10px 16px;
        border-radius: 12px 12px 12px 2px;
        margin: 6px 0;
        margin-right: 20%;
        font-size: 15px;
        color: #212121;
        border: 1px solid #e0e0e0;
    }

    /* Header */
    .chat-header {
        background-color: #075e54;
        color: white;
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 16px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────
st.markdown("""
<div class="chat-header">
    <h2 style="margin:0; color:white;">🛒 ShopEase Assistant</h2>
    <p style="margin:0; color:#25d366; font-size:13px;">● Online — Always here to help</p>
</div>
""", unsafe_allow_html=True)

# ── Quick buttons ────────────────────────────────────────
st.write("**Quick Commands:**")
col1, col2, col3, col4, col5 = st.columns(5)

quick_query = None

with col1:
    if st.button("📦 Order"):
        quick_query = "show order status"
with col2:
    if st.button("💳 Payment"):
        quick_query = "payment options"
with col3:
    if st.button("🎁 Offers"):
        quick_query = "any offers"
with col4:
    if st.button("🚚 Shipping"):
        quick_query = "shipping info"
with col5:
    if st.button("🎧 Support"):
        quick_query = "customer support"

st.divider()

# ── Chat history ─────────────────────────────────────────
# st.session_state stores data between reruns
# This is how Streamlit remembers previous messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message on first load
    st.session_state.messages.append({
        "role": "bot",
        "text": "👋 Hello! Welcome to ShopEase!\n\nI can help you with orders, payments, shipping, offers, and more. What can I help you with today?"
    })

# ── Display chat history ──────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-bubble">{msg["text"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-bubble">{msg["text"]}</div>',
            unsafe_allow_html=True
        )

# ── Handle quick button clicks ────────────────────────────
if quick_query:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "text": quick_query
    })
    # Get and add bot response
    response = get_response(quick_query)
    st.session_state.messages.append({
        "role": "bot",
        "text": response
    })
    st.rerun()  # refresh the page to show new messages

# ── Text input at bottom ──────────────────────────────────
with st.form("chat_form", clear_on_submit=True):
    col_input, col_send = st.columns([5, 1])
    with col_input:
        user_input = st.text_input(
            label="Message",
            placeholder="Type your message here...",
            label_visibility="collapsed"
        )
    with col_send:
        submitted = st.form_submit_button("Send ➤")

# ── Process the message ───────────────────────────────────
if submitted and user_input.strip():
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "text": user_input
    })
    # Get bot reply using your existing get_response()
    response = get_response(user_input)
    # Save bot reply
    st.session_state.messages.append({
        "role": "bot",
        "text": response
    })
    # Rerun to refresh the chat
    st.rerun()

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🛒 ShopEase Chatbot")
    st.markdown("---")
    st.markdown("**Available Commands:**")
    commands = [
        "📦 order status",
        "❌ cancel order",
        "↩️ return / refund",
        "💳 payment options",
        "🚚 shipping info",
        "🎁 offers / discounts",
        "🎧 support / contact",
        "❓ help",
    ]
    for cmd in commands:
        st.markdown(f"• {cmd}")

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "bot",
            "text": "Chat cleared! How can I help you?"
        })
        st.rerun()

    st.markdown("---")
    st.markdown("*Built with Python + Streamlit*")