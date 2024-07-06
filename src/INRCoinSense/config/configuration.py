import sys

from src.INRCoinSense.constants import *
from src.INRCoinSense.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    ModelTrainingConfig
)
from src.INRCoinSense.utils.common import read_yaml, create_directories

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH):

        self.config = read_yaml(config_filepath)

        # Artifact root directory
        create_directories(
            [
                Path(self.config.root.artifact)
            ]
        )

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            logging.info("Getting data ingestion configuration:")

            config = self.config.data_ingestion

            create_directories(
                [
                    Path(config.root_dir)
                ]
            )

            data_ingestion_config = DataIngestionConfig(
                root_dir=Path(config.root_dir),
                remote_path=config.remote_path,
                local_path=Path(config.local_path),
                unzip_dir=Path(config.unzip_dir),
            )

            logging.info("Data ingestion configuration loaded successfully!")

            return data_ingestion_config

        except Exception as e:
            logging.error(f"Error occurred while getting data ingestion configuration!")
            raise CustomException(e, sys)

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            logging.info("Getting data validation configuration:")

            config = self.config.data_validation

            create_directories(
                [
                    Path(config.root_dir)
                ]
            )

            data_validation_config = DataValidationConfig(
                root_dir=Path(config.root_dir),
                dataset_dir=Path(config.dataset_dir),
                dataset_info=Path(config.dataset_info),
                datasets=config.datasets,
                data=config.data,
                validation_status=Path(config.validation_status)
            )

            logging.info("Data validation configuration loaded successfully!")

            return data_validation_config

        except Exception as e:
            logging.error(f"Error occurred while getting data validation configuration!")
            raise CustomException(e, sys)

    def get_model_training_config(self) -> ModelTrainingConfig:
        try:
            logging.info("Getting model training configuration:")

            config = self.config.model_training

            create_directories(
                [
                    Path(config.root_dir),
                    Path(config.trained_weights_dir)
                ]
            )

            model_training_config = ModelTrainingConfig(
                root_dir=Path(config.root_dir),
                dataset_dir=Path(config.dataset_dir),
                dataset_info=Path(config.dataset_info),
                model=config.model,
                img_size=config.img_size,
                batch_size=config.batch_size,
                epochs=config.epochs,
                trained_weights_dir=Path(config.trained_weights_dir)
            )

            logging.info("Model training configuration loaded successfully!")

            return model_training_config

        except Exception as e:
            logging.error(f"Error occurred while getting model training configuration!")
            raise CustomException(e, sys)
