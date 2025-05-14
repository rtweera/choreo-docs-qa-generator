from app import directory_sum
from config import config
from app.llm import model_health_check

# directory_sum.sum(config.DOCS_DIR)

# directory_sum.summarize(config.DOCS_DIR)

print(model_health_check())