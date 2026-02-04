from Spam_detction.logger import setup_logger
from Spam_detction.pipeline.pipeline01_data_ingestion import run_data_ingestion_pipeline
from Spam_detction.pipeline.pipeline02_data_validation import run_data_validation_pipeline
from Spam_detction.pipeline.pipeline03_data_preprocessing import run_data_preprocessing_pipeline
from Spam_detction.pipeline.pipeline04_model_training import run_model_training_pipeline


logger = setup_logger("main", "main.log")

def main():
    logger.info("ML PIPELINE STARTED")

    run_data_ingestion_pipeline()
    run_data_validation_pipeline()
    run_data_preprocessing_pipeline()
    run_model_training_pipeline()

    logger.info("ML PIPELINE FINISHED")

if __name__ == "__main__":
    main()
