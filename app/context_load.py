import pandas as pd
import os

def load_qa(*, data_dir: str = "private", data_file: str = "eval-dataset.csv", n: int = 10) -> str: 
    """
    Loads a specified number of question-answer pairs from a CSV file and formats them as a string.

    Args:
        data_dir (str): The directory where the data file is located. Defaults to "private".
        data_file (str): The name of the CSV file containing the dataset. Defaults to "eval-dataset.csv".
        n (int): The number of question-answer pairs to load from the dataset. Defaults to 10.

    Returns:
        str: A formatted string containing the loaded question-answer pairs, where each pair is 
             represented as:
             Q: <question>
             A: <ground_truth>
    """
    file_path = os.path.join(data_dir, data_file)
    df = pd.read_csv(file_path)
    examples = "\n".join([f"Q: {row['question']}\nA: {row['ground_truth']}" for _, row in df.head(n).iterrows()])
    return examples


def load_summary(*, data_dir: str = "docs", data_file: str = "final_summary.md") -> str:
    """
    Loads the content of a summary file from the specified directory.

    Args:
        data_dir (str): The directory where the summary file is located. Defaults to "docs".
        data_file (str): The name of the summary file to load. Defaults to "final_summary.md".

    Returns:
        str: The content of the summary file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error reading the file.
    """
    file_path = os.path.join(data_dir, data_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        summary = f.read()
    return summary