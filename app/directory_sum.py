import os
from tqdm import tqdm

from .llm import summarize_by_llm

def sum(docs_dir: str) -> None:
    """
    Generates summary Markdown files for each subdirectory in the given directory.
    This function iterates through all subdirectories in the specified directory,
    reads the content of all Markdown (.md) files within each subdirectory, and
    concatenates their content into a single summary file. The summary file is
    saved in the respective subdirectory with the name `<subdirectory_name>_sum.md`.
    Args:
        docs_dir (str): The path to the directory containing subdirectories with Markdown files.
    Returns:
        None
    """
    
    for item in tqdm(os.listdir(docs_dir), desc='Summing files'):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path):
            sum_content = """ """
            for root, dirs, files in os.walk(item_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.endswith('.md'):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            sum_content += f.read() + '\n\n'

            sum_filename = f"{item}_sum.md"
            sum_path = os.path.join(item_path, sum_filename)
            with open(sum_path, 'w', encoding='utf-8') as f:
                f.write(sum_content)


def summarize(docs_dir: str) -> None:
    """
    Summarizes the content of files within subdirectories of the given directory.

    This function iterates through the subdirectories of the specified directory,
    reads the content of a markdown file named '<subdirectory_name>_sum.md', 
    generates a summary using a language model, and writes the summary to a new 
    markdown file named '<subdirectory_name>_summary.md' within the same subdirectory.

    Args:
        docs_dir (str): The path to the directory containing subdirectories with files to summarize.

    Returns:
        None
    """
    for item in tqdm(os.listdir(docs_dir), desc='Summarizing files'):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path):
            file_path = os.path.join(item_path, f'{item}_sum.md')
            with open(file_path, 'r', encoding='utf-8') as f:
                file_sum = f.read()
            summary = summarize_by_llm(file_sum)
            out_path = os.path.join(item_path, f'{item}_summary.md')
            with open(out_path, 'w', encoding='utf-8') as o:
                o.write(summary)

