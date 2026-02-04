from pathlib import Path

from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.data_preprocessing import DataPreprocessing
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="pipeline_data_preprocessing",
    log_file="pipeline_data_preprocessing.log"
)

def run_data_preprocessing_pipeline():
    logger.info("DATA PREPROCESSING PIPELINE STARTED")

    config = ConfigManager(Path("config/config.yaml"))
    preprocessing_config = config.get_data_preprocessing_config()

    DataPreprocessing(preprocessing_config).initiate_data_preprocessing()

    logger.info("DATA PREPROCESSING PIPELINE COMPLETED")
