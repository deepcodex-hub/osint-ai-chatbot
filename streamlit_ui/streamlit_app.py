
import streamlit as st
import requests
from streamlit_chat import message

# App Config
st.set_page_config(page_title="AI Defender Toolkit", layout="wide")
st.markdown("""
    <style>
    body {
        background-color: #0d0d0d;
        color: white;
    }
    .block-container {
        padding: 1rem 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1a1a1a;
        border-radius: 8px;
        padding: 8px;
        margin-right: 10px;
        color: #00ffcc;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #262626;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💻 AI Defender Cyber Intelligence Suite")

backend = "https://fcac-2409-408d-3ebf-a6e2-5c6b-c75a-d65a-ed73.ngrok-free.app"

def fetch(endpoint, params):
    try:
        response = requests.get(f"{backend}{endpoint}", params=params)
        return response.json()
    except:
        return {"error": "Backend not reachable"}

col1, col2 = st.columns([1, 2])

# Left Column - Chatbot UI
with col1:
    st.markdown("## 🤖 AI Chatbot")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", "", key="chat")

    if st.button("Send"):
        st.session_state.chat_history.append(("user", user_input))
        # Mock Rasa Response for now
        response = requests.post("https://1a26-2409-408d-3ebf-a6e2-5c6b-c75a-d65a-ed73.ngrok-free.app/webhooks/rest/webhook", json={"message": user_input})
        try:
            bot_reply = response.json()[0]['text']
        except:
            bot_reply = "Sorry, I didn't understand that."
        st.session_state.chat_history.append(("bot", bot_reply))

    for i, (role, msg) in enumerate(st.session_state.chat_history):
        message(msg, is_user=(role=="user"), key=f"{role}_{i}")


# Right Column - OSINT Tabs
with col2:
    tab1, tab2, tab3, tab4 = st.tabs(["🌐 Domain Tools", "📧 Email & IP", "📱 Social Scrapers", "🌑 Dark OSINT"])

    with tab1:
        st.subheader("🔍 WHOIS Lookup")
        domain = st.text_input("Domain for WHOIS", key="whois")
        if st.button("WHOIS Lookup"):
            st.json(fetch("/whois-lookup/", {"domain": domain}))

        st.subheader("🌐 DNS Lookup")
        domain2 = st.text_input("Domain for DNS", key="dns")
        if st.button("DNS Lookup"):
            st.json(fetch("/dns-lookup/", {"domain": domain2}))

        st.subheader("📌 IP Tracker")
        domain3 = st.text_input("Domain for IP Tracking", key="ip")
        if st.button("Track IP"):
            st.json(fetch("/ip-tracker/", {"domain": domain3}))

    with tab2:
        st.subheader("📧 Email Breach Checker (Simulated)")
        email = st.text_input("Email", key="email")
        if st.button("Check Breach"):
            st.json(fetch("/email-breach/", {"email": email}))

    with tab3:
        st.subheader("📷 Instagram Scraper (Mock)")
        insta = st.text_input("Instagram Username", key="insta")
        if st.button("Scrape Instagram"):
            st.json(fetch("/instagram-scraper/", {"username": insta}))

        st.subheader("🐦 Twitter Scraper (Mock)")
        twitter = st.text_input("Twitter Username", key="twitter")
        if st.button("Scrape Twitter"):
            st.json(fetch("/twitter-scraper/", {"username": twitter}))

        st.subheader("📲 Telegram Scraper (Mock)")
        telegram = st.text_input("Telegram Group", key="telegram")
        if st.button("Scrape Telegram"):
            st.json(fetch("/telegram-scraper/", {"groupname": telegram}))

    with tab4:
        st.subheader("🌑 Darkweb Search (Mock)")
        dark_query = st.text_input("Search Dark Web", key="darkweb")
        if st.button("Search Dark Web"):
            st.json(fetch("/darkweb-search/", {"query": dark_query}))

        st.subheader("🧵 Webforum Scanner (Mock)")
        forum_topic = st.text_input("Forum Topic", key="forum")
        if st.button("Scan Forum"):
            st.json(fetch("/webforum-scan/", {"topic": forum_topic}))
