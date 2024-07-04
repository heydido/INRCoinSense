import os
import sys
import zipfile

from pathlib import Path

from src.INRCoinSense.utils.common import get_size
from src.INRCoinSense.utils.dagshub_storage import DagsHubUtility
from src.INRCoinSense.entity.config_entity import DataIngestionConfig
from src.INRCoinSense.config.configuration import ConfigurationManager

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_path):
                logging.info("Downloading data file from source URL:")

                dagshub_client = DagsHubUtility()
                dagshub_client.download_file(
                    local_path=self.config.local_path,
                    remote_path=self.config.remote_path
                )

                logging.info(f"Zip file downloaded and saved as: {self.config.local_path}")

            else:
                logging.info(f"Zip file already exists of size: {get_size(Path(self.config.local_path))}")

        except Exception as e:
            logging.error(f"Error occurred while downloading data file!")
            raise CustomException(e, sys)

    def unzip_file(self):
        try:
            os.makedirs(self.config.unzip_dir, exist_ok=True)

            if not os.listdir(self.config.unzip_dir):
                logging.info("Unzipping data file:")

                with zipfile.ZipFile(self.config.local_path, 'r') as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)

                logging.info(f"Data unzipped successfully at: {self.config.unzip_dir}")

            else:
                logging.info(f"Dataset already present at: {self.config.unzip_dir}")

        except Exception as e:
            logging.error(f"Error occurred while unzipping data!")
            raise CustomException(e, sys)

    def main(self):
        self.download_file()
        self.unzip_file()


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()

    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.main()
