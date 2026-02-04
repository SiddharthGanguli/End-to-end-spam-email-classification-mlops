from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataIngestionConfig :
    root_dir : Path
    source_dir :Path
    train_dir :Path
    test_dir : Path
@dataclass
class DataValidationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    required_columns: list
    target_column: str