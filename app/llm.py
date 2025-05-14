from google import genai
from dotenv import load_dotenv
import os

prompt = """
Generate a summary from the given content. Keep the headings as it is because they
help with the organization of the document. You can summarize the other things but keep
the data loss to a minimum.
"""

def summarize_by_llm(text: str, prompt: str = prompt, client = genai.Client) -> str:
    return text

def model_health_check(prompt='Hello world'):
    model = load_model()
    return model.invoke(prompt)

def load_model():
    _load_api_key()
    from langchain.chat_models import init_chat_model
    model = init_chat_model(model='gemini-2.0-flash', model_provider='google_genai')
    return model

def _load_api_key():
    load_dotenv()
    _key = os.getenv('GOOGLE_API_KEY')
    if _key is not None:
        del _key
    else:
        del _key
        raise ValueError('LLM API key is not defined')