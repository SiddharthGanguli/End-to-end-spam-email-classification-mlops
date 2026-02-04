from pathlib import Path

from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.data_validation import DataValidation
from Spam_detction.logger import setup_logger

logger = setup_logger("pipeline_data_validation")

def run_data_validation_pipeline():
    try:
        logger.info("========== DATA VALIDATION PIPELINE STARTED ==========")

        config = ConfigManager(Path("config.yaml"))
        validation_config = config.get_data_validation_config()

        validator = DataValidation(validation_config)
        validator.initiate_data_validation()

        logger.info("========== DATA VALIDATION PIPELINE COMPLETED ==========")

    except Exception as e:
        logger.exception("Data validation pipeline failed")
        raise e


if __name__ == "__main__":
    run_data_validation_pipeline()
