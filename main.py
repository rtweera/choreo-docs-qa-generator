import argparse

from app import directory_sum, llm
from config import config
from app.logger import Logger

logger = Logger(__name__, "main_runs.log")


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
    parser.add_argument("--all", action="store_true", help="Run the entire flow")

    args = parser.parse_args()

    if args.health:
        logger.info(llm.model_health_check())
    if args.concat:
        directory_sum.concat_summaries(config.DOCS_DIR)
    if args.question:
        print(llm.generate_questions())
    if args.all:
        full_flow()


if __name__ == "__main__":
    main()
