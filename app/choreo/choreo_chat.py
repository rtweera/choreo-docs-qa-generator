import requests
import json
from dotenv import load_dotenv
import os
from .choreo_config import API_URL, HEADERS
from datetime import datetime

load_dotenv()


def ask_question(question):
    """
    Ask a question from the choreo copilot, get the answer as a full text.
    """
    payload = json.dumps(
        {
            "question": question,
            "version": "v2.0",
            "current_datetime": datetime.now().isoformat(),
            "perspective": "dev",
        }
    )

    # print("awaiting response")
    response = requests.request(
        "POST", API_URL, headers=HEADERS, data=payload, stream=True
    )

    if response.status_code == 401:
        print(f"request failed\nResponse:{response.text}")
        return

    # print(f"response arrived:\n{response}")

    full_answer = ""
    for line in response.iter_lines(decode_unicode=True):
        if line and line.startswith("data:"):
            try:
                data = json.loads(line[5:].strip())
                if data.get("type") == "STREAM":
                    full_answer += data.get("content", "")
            except Exception as e:
                print(f"Exception: {e}")
                continue
    return full_answer


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = "Hey yo!"
    print(ask_question(question))
