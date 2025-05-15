from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from .context_load import load_qa, load_summary
from .prompts import question_prompt, map_prompt


def model_health_check(prompt="Hello world"):
    model = load_model()
    return model.invoke(prompt)


def load_model():
    _load_api_key()
    model = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")
    return model


def _load_api_key():
    load_dotenv()
    _key = os.getenv("GOOGLE_API_KEY")
    if _key is not None:
        del _key
    else:
        del _key
        raise ValueError("LLM API key is not defined")


def summarize_by_llm(
    doc_content: str, prompt: PromptTemplate = map_prompt, llm=load_model()
) -> str:
    if not doc_content.strip():
        return "No content to summarize."

    chain = prompt | llm | StrOutputParser()

    try:
        summary = chain.invoke({"context": doc_content})
        return summary.strip()
    except Exception as e:
        return f"Error summarising content: {str(e)}"

def generate_questions(summary: str = load_summary(), examples: str = load_qa(n=100), prompt: PromptTemplate = question_prompt, llm = load_model()) -> str:
    if not summary.strip():
        return "No summary presented"
    if not examples.strip():
        return "No examples presented"
    
    chain = prompt | llm | StrOutputParser();

    try:
        response_with_questions = chain.invoke({"context": summary, "examples": examples, "n": 10})
        return response_with_questions.strip() + '\n'
    except Exception as e:
        return f"Error getting response: {str(e)}"