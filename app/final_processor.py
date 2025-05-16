import pandas as pd
import json
import os
from tqdm import tqdm


def process(
    docs_dir: str = "qa",
    input_file_name: str = "qa.csv",
    output_file_name: str = "final.jsonl",
):
    """
    Processes a CSV file containing questions and answers, and converts it into a JSONL file
    with a specific format for each entry.
    Args:
        docs_dir (str): The directory where the input and output files are located.
                        Defaults to 'qa'.
        input_file_name (str): The name of the input CSV file containing the data.
                                Defaults to 'qa.csv'.
        output_file_name (str): The name of the output JSONL file to be generated.
                                Defaults to 'final.jsonl'.
    The input CSV file is expected to have the following columns:
        - 'question': The question text.
        - 'answer': The corresponding answer text.
    The output JSONL file will contain one JSON object per line with the following structure:
        {
            "instruction": "Answer the following question about choreo",
            "input": <question>,
            "output": <answer>
        }
    Raises:
        FileNotFoundError: If the input file does not exist.
        KeyError: If the required columns ('question', 'answer') are missing in the input file.
        Exception: For any other errors encountered during processing.
    """

    input_file_path = os.path.join(docs_dir, input_file_name)
    output_file_path = os.path.join(docs_dir, output_file_name)
    df = pd.read_csv(input_file_path)
    with open(output_file_path) as f:
        for row_index, row in tqdm(df.iterrows(), desc="Processing data"):
            entry = {
                "instruction": "Answer the following question about choreo",
                "input": row["question"],
                "output": row["answer"],
            }
            f.write(json.dumps(entry) + "\n")
