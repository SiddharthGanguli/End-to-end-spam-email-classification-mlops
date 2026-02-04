from pathlib import Path
from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.data_ingestion import DataIngestion
from Spam_detction.logger import setup_logger

logger = setup_logger("pipeline_data_ingestion", "pipeline_data_ingestion.log")

def run_data_ingestion_pipeline():
    logger.info("DATA INGESTION PIPELINE STARTED")

    config = ConfigManager(Path("config/config.yaml"))
    ingestion_config = config.get_data_ingestion_config()

    DataIngestion(ingestion_config).initiate_data_ingestion()

    logger.info("DATA INGESTION PIPELINE COMPLETED")
