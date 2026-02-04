
import json
import joblib
import pandas as pd
from pathlib import Path

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from Spam_detction.entity.entity import ModelEvaluationConfig
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="model_evaluation",
    log_file="model_evaluation.log"
)


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def initiate_model_evaluation(self):
        logger.info("Starting model evaluation")


        if not self.config.model_path.exists():
            raise FileNotFoundError(f"Model not found: {self.config.model_path}")

        model = joblib.load(self.config.model_path)
        logger.info(f"Loaded model from {self.config.model_path}")


        test_df = pd.read_csv(self.config.test_data_path)

        if self.config.target_column not in test_df.columns:
            raise ValueError("Target column missing in test data")

        X_test = test_df.drop(columns=[self.config.target_column])
        y_test = test_df[self.config.target_column]


        y_pred = model.predict(X_test)


        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred)
        }

        logger.info(f"Evaluation metrics: {metrics}")


        self.config.metrics_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config.metrics_path, "w") as f:
            json.dump(metrics, f, indent=4)

        logger.info(f"Saved metrics at: {self.config.metrics_path}")

        return metrics
