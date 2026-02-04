import yaml
import os
from pathlib import Path

from Spam_detction.entity.entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataPreprocessingConfig,
    ModelTrainerConfig
)

class ConfigManager:

    def __init__(self, config_filepath: Path):
        self.config = self._read_yaml(config_filepath)

    def _read_yaml(self, file_path: Path) -> dict:
        if not file_path.exists():
            raise FileNotFoundError(f"Config file not found: {file_path}")
        with open(file_path, "r") as f:
            config = yaml.safe_load(f)
        if config is None:
            raise ValueError("Config file is empty")
        return config

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        ingestion = self.config["data_ingestion"]
        os.makedirs(ingestion["root"], exist_ok=True)

        return DataIngestionConfig(
            root_dir=Path(ingestion["root"]),
            source_dir=Path(ingestion["source_dir"]),
            train_dir=Path(ingestion["train_dir"]),
            test_dir=Path(ingestion["test_dir"])
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        validation = self.config["data_validation"]
        os.makedirs(validation["root"], exist_ok=True)

        return DataValidationConfig(
            root_dir=Path(validation["root"]),
            train_data_path=Path(validation["train_data_path"]),
            test_data_path=Path(validation["test_data_path"]),
            required_columns=validation["required_columns"],
            target_column=validation["target_column"]
        )


    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        preprocessing = self.config["data_preprocessing"]
        os.makedirs(preprocessing["root"], exist_ok=True)

        return DataPreprocessingConfig(
            root_dir=Path(preprocessing["root"]),
            train_data_path=Path(preprocessing["train_data_path"]),
            test_data_path=Path(preprocessing["test_data_path"]),
            processed_train_path=Path(preprocessing["processed_train_path"]),
            processed_test_path=Path(preprocessing["processed_test_path"]),
            vectorizer_path=Path(preprocessing["vectorizer_path"]),
            text_column=preprocessing["text_column"],
            target_column=preprocessing["target_column"]
        )
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        trainer = self.config["model_trainer"]
        os.makedirs(trainer["root"], exist_ok=True)
        os.makedirs(trainer["model_dir"], exist_ok=True)

        return ModelTrainerConfig(
            root_dir=Path(trainer["root"]),
            train_data_path=Path(trainer["train_data_path"]),
            test_data_path=Path(trainer["test_data_path"]),
            model_dir=Path(trainer["model_dir"]),
            target_column=trainer["target_column"],
            experiment_name=trainer["experiment_name"]
        )