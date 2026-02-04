import os
import logging 
from pathlib import Path


project_name="Spam_detction"
log_dir='logs'
log_file='project_setup.log'

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir,log_file),
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"

)
logger=logging.getLogger(__name__)

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/config.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/model_traning.py",
    f"src/{project_name}/components/model_validation.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/pipeline01_data_ingestion.py",
    f"src/{project_name}/pipeline/pipeline02_data_validation.py",
    f"src/{project_name}/pipeline/pipeline03_data_preprocessing.py",
    f"src/{project_name}/pipeline/pipeline04_model_training.py",
    f"src/{project_name}/pipeline/pipeline05_model_validation.py",
    f"src/logger.py",
    'config/config.yaml',
    'params.yaml',
    'main.py',
    'requirements.txt',
    '.gitignore',
    'setup.py',
    'app.py'
]

for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,filename=os.path.split(file_path)

    if file_dir:
        os.makedirs(file_dir,exist_ok=True)
        logger.info(f"Created directory : {file_dir}")

    if not file_path.exists():
        file_path.touch()
        logger.info(f"Created file : {file_path}")