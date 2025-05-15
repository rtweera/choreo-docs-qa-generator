import requests
import json
from dotenv import load_dotenv
import os
from config import API_URL, HEADERS
from datetime import datetime

load_dotenv()

def ask_question(question):
    payload = json.dumps({
        "question": question,
        "version": "v2.0",
        "current_datetime": datetime.now().isoformat(),
        "perspective": "dev"
    })

    print("awaiting response")
    response = requests.request("POST", API_URL, headers=HEADERS, data=payload, stream=True)
    print(f"response arrived:\n{response}")

    full_text = ""
    for line in response.iter_lines(decode_unicode=True):
        if line and line.startswith("data:"):
            try:
                data = json.loads(line[5:].strip())
                if data.get("type") == "STREAM":
                    full_text += data.get("content", "")
            except Exception as e:
                print(f'Exception: {e}')
                continue
    print(full_text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = "Hey yo!"
    ask_question(question)
