from pathlib import Path
from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.data_validation import DataValidation
from Spam_detction.logger import setup_logger

logger = setup_logger("pipeline_data_validation", "pipeline_data_validation.log")

def run_data_validation_pipeline():
    logger.info("DATA VALIDATION PIPELINE STARTED")

    config = ConfigManager(Path("config/config.yaml"))
    validation_config = config.get_data_validation_config()

    DataValidation(validation_config).initiate_data_validation()

    logger.info("DATA VALIDATION PIPELINE COMPLETED")
