import os
import pandas as pd

from Spam_detction.entity.entity import DataValidationConfig
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="data_validaion",
    log_file="data_validation.log"
)

class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_dataset(self, path):
        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {path}")

        df = pd.read_csv(path)
        logger.info(f"Loaded dataset {path} with shape {df.shape}")

        
        missing_cols = set(self.config.required_columns) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns in {path}: {missing_cols}")

        
        null_counts = df[self.config.required_columns].isnull().sum()
        if null_counts.any():
            logger.warning(f"Null values found in {path}:\n{null_counts}")

        
        if self.config.target_column not in df.columns:
            raise ValueError("Target column missing")

        logger.info(f"Validation passed for {path}")
        return True

    def initiate_data_validation(self):
        logger.info("Starting data validation")

        self.validate_dataset(self.config.train_data_path)
        self.validate_dataset(self.config.test_data_path)

        logger.info("Data validation completed successfully")
        return True
