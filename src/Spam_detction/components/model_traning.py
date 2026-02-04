import os
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from Spam_detction.entity.entity import ModelTrainerConfig
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="model_trainer",
    log_file="model_trainer.log"
)


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def load_data(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        X_train = train_df.drop(columns=[self.config.target_column])
        y_train = train_df[self.config.target_column]

        X_test = test_df.drop(columns=[self.config.target_column])
        y_test = test_df[self.config.target_column]

        return X_train, X_test, y_train, y_test

    @staticmethod
    def evaluate(y_true, y_pred):
        return {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred),
            "recall": recall_score(y_true, y_pred),
            "f1_score": f1_score(y_true, y_pred),
        }

    def initiate_model_training(self):
        logger.info("Starting model training with MLflow")

        mlflow.set_experiment(self.config.experiment_name)

        X_train, X_test, y_train, y_test = self.load_data()

        models = {
            "LogisticRegression": LogisticRegression(max_iter=1000),
            "MultinomialNB": MultinomialNB(),
            "LinearSVM": LinearSVC()
        }

        best_model = None
        best_f1 = 0.0

        for model_name, model in models.items():
            with mlflow.start_run(run_name=model_name):
                logger.info(f"Training model: {model_name}")

                model.fit(X_train, y_train)
                predictions = model.predict(X_test)

                metrics = self.evaluate(y_test, predictions)


                mlflow.log_metrics(metrics)
                mlflow.log_param("model_name", model_name)

                logger.info(f"{model_name} metrics: {metrics}")


                if metrics["f1_score"] > best_f1:
                    best_f1 = metrics["f1_score"]
                    best_model = model
                    best_model_name = model_name

  
        model_path = self.config.model_dir / f"{best_model_name}.pkl"
        joblib.dump(best_model, model_path)

        mlflow.sklearn.log_model(
            best_model,
            artifact_path="best_model",
            registered_model_name=best_model_name
        )

        logger.info(f"Best model: {best_model_name} with F1 score: {best_f1}")
        logger.info(f"Saved best model at: {model_path}")

        return model_path
