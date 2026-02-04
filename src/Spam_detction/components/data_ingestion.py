import os
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from Spam_detction.entity.entity import DataIngestionConfig
from Spam_detction.logger import setup_logger

logger = setup_logger("data_ingestion")

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):

        logger.info("Starting data ingestion")

        try:
           
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Created root artifact directory at: {self.config.root_dir}")

            
            raw_file = Path(self.config.source_dir)
            if not raw_file.exists():
                msg = f"Source file not found at {raw_file}"
                logger.error(msg)
                raise FileNotFoundError(msg)

            
            df = pd.read_csv(raw_file)
            logger.info(f"Loaded raw data with shape: {df.shape}")

            
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            logger.info(f"Split data into train ({train_df.shape}) and test ({test_df.shape})")

            
            train_path = Path(self.config.train_dir)
            test_path = Path(self.config.test_dir)

            
            os.makedirs(train_path.parent, exist_ok=True)
            os.makedirs(test_path.parent, exist_ok=True)

            train_df.to_csv(train_path, index=False)
            test_df.to_csv(test_path, index=False)

            logger.info(f"Saved training data at: {train_path}")
            logger.info(f"Saved testing data at: {test_path}")

            logger.info("Data ingestion completed successfully")

            return train_path, test_path

        except Exception as e:
            logger.exception("Error occurred during data ingestion")
            raise e

