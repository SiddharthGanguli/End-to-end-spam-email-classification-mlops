
from pathlib import Path

from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.model_evalutation import ModelEvaluation
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="pipeline_model_evaluation",
    log_file="pipeline_model_evaluation.log"
)

def run_model_evaluation_pipeline():
    logger.info("MODEL EVALUATION PIPELINE STARTED")

    config = ConfigManager(Path("config/config.yaml"))
    evaluation_config = config.get_model_evaluation_config()

    ModelEvaluation(evaluation_config).initiate_model_evaluation()

    logger.info("MODEL EVALUATION PIPELINE COMPLETED")
