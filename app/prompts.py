from langchain_core.prompts import PromptTemplate

map_prompt = PromptTemplate.from_template(
    "Generate a summary from the given following content. Keep the headings as it is because they help with the organization of the document. You can summarize the other things but keep the data loss to a minimum. \n\n<context>\n{context}\n</context>"
)

reduce_prompt = PromptTemplate.from_template(
    "Combine the following summaries into a concise overall summary, focusing on key themes and insights:\n\n{context}"
)

question_prompt = PromptTemplate.from_template(
    """
Based on the following documentation about Choreo and the examples of existing questions and answers, generate {n} new questions that are relevant, informative, and follow the same style.

--- Context ---
{context}

--- Examples ---
{examples}

--- Task ---
Now generate {n} new relevant questions (no answers needed). Do not provide any other texts. Only the questions, on question on each line:
<question1>
<question2>
<question3>
...
"""
)
