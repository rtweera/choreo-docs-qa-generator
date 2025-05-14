import argparse

from app import directory_sum
from config import config
from app.llm import model_health_check
from app.logger import Logger

logger = Logger(__name__, 'main_runs.log')

def default_flow():
    directory_sum.sum(config.DOCS_DIR)
    directory_sum.summarize(config.DOCS_DIR)

def main():
    parser = argparse.ArgumentParser(description="Choreo Docs QA Generator")
    parser.add_argument("--health", action="store_true", help="Run the health check")
    args = parser.parse_args()

    if args.health:
        logger.info(model_health_check())
    if not (args.health):
        default_flow()

if __name__ == '__main__':
    main()