import os
import re
import joblib
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

from Spam_detction.entity.entity import DataPreprocessingConfig
from Spam_detction.logger import setup_logger

logger = setup_logger(
    name="data_preprocessing",
    log_file="data_preprocessing.log"
)


class DataPreprocessing:

    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    @staticmethod
    def clean_text(text: str) -> str:
        if not isinstance(text, str):
            return ""

        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^a-z\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text


    def load_data(self, path: Path) -> pd.DataFrame:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        df = pd.read_csv(path)

        if self.config.text_column not in df.columns:
            raise ValueError(f"Missing column: {self.config.text_column}")

        if self.config.target_column not in df.columns:
            raise ValueError(f"Missing column: {self.config.target_column}")

        df = df[[self.config.text_column, self.config.target_column]]
        df.dropna(inplace=True)

        logger.info(f"Loaded data from {path} with shape {df.shape}")
        return df

    @staticmethod
    def encode_labels(series: pd.Series):
        mapping = {"ham": 0, "spam": 1}

        if not set(series.unique()).issubset(mapping.keys()):
            raise ValueError(
                f"Unexpected label values: {series.unique()}"
            )

        encoded = series.map(mapping)
        return encoded, mapping

    def initiate_data_preprocessing(self):
        logger.info("Starting data preprocessing")

       
        train_df = self.load_data(self.config.train_data_path)
        test_df = self.load_data(self.config.test_data_path)


        train_df[self.config.text_column] = train_df[self.config.text_column].apply(self.clean_text)
        test_df[self.config.text_column] = test_df[self.config.text_column].apply(self.clean_text)

 
        y_train, label_mapping = self.encode_labels(train_df[self.config.target_column])
        y_test, _ = self.encode_labels(test_df[self.config.target_column])

        logger.info(f"Label encoding mapping used: {label_mapping}")

   
        vectorizer = TfidfVectorizer(
            max_features=5000,
            ngram_range=(1, 2),
            stop_words="english"
        )

        X_train = vectorizer.fit_transform(train_df[self.config.text_column])
        X_test = vectorizer.transform(test_df[self.config.text_column])


        os.makedirs(self.config.root_dir, exist_ok=True)

        train_processed = pd.DataFrame(X_train.toarray())
        train_processed[self.config.target_column] = y_train.values

        test_processed = pd.DataFrame(X_test.toarray())
        test_processed[self.config.target_column] = y_test.values

        train_processed.to_csv(self.config.processed_train_path, index=False)
        test_processed.to_csv(self.config.processed_test_path, index=False)

        joblib.dump(vectorizer, self.config.vectorizer_path)


        label_map_path = self.config.root_dir / "label_mapping.json"
        pd.Series(label_mapping).to_json(label_map_path)

        logger.info(f"Saved processed train data: {self.config.processed_train_path}")
        logger.info(f"Saved processed test data: {self.config.processed_test_path}")
        logger.info(f"Saved TF-IDF vectorizer: {self.config.vectorizer_path}")
        logger.info(f"Saved label mapping at: {label_map_path}")

        logger.info("Data preprocessing completed successfully")

        return (
            self.config.processed_train_path,
            self.config.processed_test_path,
            self.config.vectorizer_path,
            label_map_path
        )
