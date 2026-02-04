from pathlib import Path

from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.model_traning import ModelTrainer
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="pipeline_model_trainer",
    log_file="pipeline_model_trainer.log"
)

def run_model_training_pipeline():
    logger.info("MODEL TRAINING PIPELINE STARTED")

    config = ConfigManager(Path("config/config.yaml"))
    trainer_config = config.get_model_trainer_config()

    ModelTrainer(trainer_config).initiate_model_training()

    logger.info("MODEL TRAINING PIPELINE COMPLETED")
