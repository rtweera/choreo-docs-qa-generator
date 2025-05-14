from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from .context_format import format_qa, load_summary

map_prompt = PromptTemplate.from_template(
    "Generate a summary from the given following content. Keep the headings as it is because they help with the organization of the document. You can summarize the other things but keep the data loss to a minimum. \n\n<context>\n{context}\n</context>"
)

reduce_prompt = PromptTemplate.from_template(
    "Combine the following summaries into a concise overall summary, focusing on key themes and insights:\n\n{context}"
)

question_prompt = PromptTemplate.from_template(
"""
Based on the following documentation about Choreo and the examples of existing questions and answers, generate 5 new questions that are relevant, informative, and follow the same style.

--- Context ---
{context}

--- Examples ---
{examples}

--- Task ---
Now generate 5 new relevant questions (no answers needed):
1.
2.
3.
4.
5.
"""
)

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

def generate_questions(summary: str = load_summary(), examples: str = format_qa(), prompt: PromptTemplate = question_prompt, llm = load_model()) -> str:
    if not summary.strip():
        return "No summary presented"
    if not examples.strip():
        return "No examples presented"
    
    chain = prompt | llm | StrOutputParser();

    try:
        response_with_questions = chain.invoke({"context": summary, "examples": examples})
        return response_with_questions.strip()
    except Exception as e:
        return f"Error getting response: {str(e)}"