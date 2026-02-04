import yaml
import os 
from pathlib import Path

from Spam_detction.entity.entity import( 
    DataIngestionConfig,
    DataValidationConfig
    )

class ConfigManager :

    def __init__(self,config_fileapath :Path):
        self.config=self._read_yaml(config_fileapath)

    def _read_yaml(self,file_path:Path)->dict:
        if not file_path.exists():
            raise FileNotFoundError(f"Config file not found {file_path}")
        with open(file_path,"r") as f:
            config=yaml.safe_load(f)

        if config is None:
            raise ValueError("Config file is empty")
        return config
    
    def get_data_ingestin_config(self)->DataIngestionConfig:
        ingestion=self.config['data_ingestion']
        os.makedirs(ingestion["root"],exist_ok=True)

        return DataIngestionConfig(
            root_dir=ingestion["root"],
            source_dir=ingestion['source_dir'],
            train_dir=ingestion['train_dir'],
            test_dir=ingestion['test_dir']

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