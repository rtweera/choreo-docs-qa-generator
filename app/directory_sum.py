import os
from tqdm import tqdm

from .llm import summarize_by_llm

def sum(docs_dir: str) -> None:
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
    for item in tqdm(os.listdir(docs_dir), desc='Summarizing files'):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path):
            file_path = os.path.join(item_path, f'{item}_sum.md')
            # file_path = f'{item_path}_sum.md'
            with open(file_path, 'r', encoding='utf-8') as f:
                file_sum = f.read()
            summary = summarize_by_llm(file_sum)
            out_path = os.path.join(item_path, f'{item}_summary.md')
            with open(out_path, 'w', encoding='utf-8') as o:
                o.write(summary)

