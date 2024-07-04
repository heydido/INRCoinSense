import sys

from src.INRCoinSense.constants import *
from src.INRCoinSense.entity.config_entity import DataIngestionConfig
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
