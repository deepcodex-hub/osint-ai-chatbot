
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import whois
import dns.resolver
import requests
import socket

app = FastAPI()

# CORS setup for frontend (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "✅ AI Defender Backend Live!"}

@app.get("/whois-lookup/")
def whois_lookup(domain: str):
    try:
        data = whois.whois(domain)
        return {"result": str(data)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/dns-lookup/")
def dns_lookup(domain: str):
    try:
        result = dns.resolver.resolve(domain, 'A')
        ip_list = [ip.to_text() for ip in result]
        return {"ip_addresses": ip_list}
    except Exception as e:
        return {"error": str(e)}

@app.get("/ip-tracker/")
def ip_tracker(domain: str):
    try:
        ip_address = socket.gethostbyname(domain)
        response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        return response
    except Exception as e:
        return {"error": str(e)}

def check_email_breach_simulated(email):
    demo_breached = ["test@gmail.com", "abc123@gmail.com", "pattu@itgirl.com"]
    if email.lower() in demo_breached:
        return {"breached": True, "sources": ["BreachDB", "DarkWebSim"]}
    else:
        return {"breached": False, "sources": []}

@app.get("/email-breach/")
def email_breach(email: str = Query(...)):
    try:
        return check_email_breach_simulated(email)
    except Exception as e:
        return {"error": str(e)}

@app.get("/instagram-scraper/")
def instagram_scraper(username: str):
    return {
        "profile": username,
        "followers": "15.2k",
        "bio": "Techie | AI | Cybersec",
        "posts": 120
    }

@app.get("/twitter-scraper/")
def twitter_scraper(username: str):
    return {
        "profile": username,
        "followers": "9.3k",
        "tweets": 2345,
        "bio": "Python enthusiast 🚀"
    }

@app.get("/telegram-scraper/")
def telegram_scraper(groupname: str):
    return {
        "group": groupname,
        "members": "3.2k",
        "recent_posts": [
            "Phishing alert on xyz domain.",
            "Cybercrime update: India #CERT issued new guidelines."
        ]
    }

@app.get("/darkweb-search/")
def darkweb_search(query: str):
    return {
        "query": query,
        "results": [
            {"title": "Leaked Credentials Dump", "source": "darkforums.onion"},
            {"title": "CC Data Marketplace", "source": "marketxyz.onion"}
        ]
    }

@app.get("/webforum-scan/")
def webforum_scan(topic: str):
    return {
        "topic": topic,
        "posts_found": [
            "Discussion on scammy payment gateway",
            "Malware behavior of certain cracked apps"
        ]
    }
