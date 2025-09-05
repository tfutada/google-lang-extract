import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")  # make sure it's set
MODEL = "gemini-2.5-flash"

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# Chat-style conversation: role + message
payload = {
    "contents": [
        {"role": "user", "parts": [{"text": "Hello, who are you?"}]}
    ]
}

headers = {"Content-Type": "application/json"}

resp = requests.post(url, headers=headers, json=payload)

if resp.status_code == 200:
    data = resp.json()
    reply = data["candidates"][0]["content"]["parts"][0]["text"]
    print("Gemini:", reply)
else:
    print("Error:", resp.status_code, resp.text)
