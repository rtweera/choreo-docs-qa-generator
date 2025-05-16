import argparse

from app import directory_sum, llm, qa_generator
from app.choreo import choreo_chat
from config import config
from app.logger import Logger

health_logger = Logger('health', "main_runs.log")
llm_logger = Logger('llm', 'llm_runs.log')
choreo_logger = Logger('choreo', 'choreo_chat.log')

def full_flow():
    directory_sum.sum(config.DOCS_DIR)
    directory_sum.summarize(config.DOCS_DIR)
    directory_sum.concat_summaries(config.DOCS_DIR)


def main():
    parser = argparse.ArgumentParser(description="Choreo Docs QA Generator")
    parser.add_argument("--health", action="store_true", help="Run the health check")
    parser.add_argument(
        "--concat", action="store_true", help="Run the final concatenation only"
    )
    parser.add_argument("--question", action="store_true", help="Run the question generation")
    parser.add_argument("-n", "--num-questions", type=int, default=1, help="Number of questions to generate")
    parser.add_argument("--chat", action="store_true", help="Run the choreo chat")
    parser.add_argument("--all", action="store_true", help="Run the entire flow")
    parser.add_argument("--answer", action="store_true", help="Run the answer generation from questions")
    args = parser.parse_args()

    if args.health:
        health_logger.info(llm.model_health_check())
    if args.concat:
        directory_sum.concat_summaries(config.DOCS_DIR)
    if args.question:
        health_logger.info('Question run: Question generation')
        qa_generator.run_generate_questions(n=args.num_questions)        
    if args.answer:
        health_logger.info('Answer run: Answer generation')
        qa_generator.find_answers()
    if args.chat:
        choreo_logger.info(choreo_chat.ask_question('what is choreo?'))
    if args.all:
        full_flow()


if __name__ == "__main__":
    main()
