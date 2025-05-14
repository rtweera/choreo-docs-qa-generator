import pandas as pd
import os

def format_qa(
    *, data_dir: str = "private", data_file: str = "eval-dataset.csv", n: int = 10
) -> str: 
    file_path = os.path.join(data_dir, data_file)
    df = pd.read_csv(file_path)
    examples = "\n".join([f"Q: {row['question']}\nA: {row['ground_truth']}" for _, row in df.head(n).iterrows()])
    return examples


def load_summary(*, data_dir: str = "docs", data_file: str = "final_summary.md") -> str:
    file_path = os.path.join(data_dir, data_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        summary = f.read()
    return summary