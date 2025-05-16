from .llm import generate_questions
import os
from tqdm import tqdm
from .choreo.choreo_chat import ask_question
import csv


def run_generate_questions(
    n: int = 1, docs_dir: str = "qa", file_name: str = "questions.csv"
) -> None:
    """
    Generate questions and save them in a CSV file with one column 'question'.
    """
    os.makedirs(docs_dir, exist_ok=True)
    file_path = os.path.join(docs_dir, file_name)
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["question"])
        print("Generating questions...")
        q_block: str = generate_questions(n_questions=n)
        questions = [q.strip() for q in q_block.split("\n") if q.strip()]
        for question in tqdm(questions, desc="Writing questions"):
            writer.writerow([question])


def find_answers(
    docs_dir: str = "qa",
    input_file_name: str = "questions.csv",
    output_file_name: str = "qa.csv",
):
    input_path = os.path.join(docs_dir, input_file_name)
    output_path = os.path.join(docs_dir, output_file_name)
    with open(input_path, "r", encoding="utf-8", newline="") as f_in, open(
        output_path, "w", encoding="utf-8", newline=""
    ) as f_out:
        reader = list(csv.DictReader(f_in))  # making a list so tqdm can get the length
        writer = csv.DictWriter(f_out, fieldnames=["question", "answer"])
        writer.writeheader()
        for row in tqdm(reader, desc="Generating answers"):
            question = row["question"]
            answer = ask_question(question).replace("\n", "\\n")
            writer.writerow({"question": question, "answer": answer})
