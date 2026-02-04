from pathlib import Path

from Spam_detction.configuration.config import ConfigManager
from Spam_detction.components.data_ingestion import DataIngestion
from Spam_detction.logger import setup_logger

logger = setup_logger("pipeline_data_ingestion")


def run_data_ingestion_pipeline():

    try:
        logger.info("========== DATA INGESTION PIPELINE STARTED ==========")

        config_path = Path("config.yaml")
        config_manager = ConfigManager(config_path)

        data_ingestion_config = config_manager.get_data_ingestin_config()
        logger.info("Data ingestion configuration loaded successfully")

        data_ingestion = DataIngestion(data_ingestion_config)
        train_path, test_path = data_ingestion.initiate_data_ingestion()

        logger.info(f"Training data saved at: {train_path}")
        logger.info(f"Testing data saved at: {test_path}")

        logger.info("========== DATA INGESTION PIPELINE COMPLETED ==========")

    except Exception as e:
        logger.exception("Data ingestion pipeline failed")
        raise e


if __name__ == "__main__":
    run_data_ingestion_pipeline()
