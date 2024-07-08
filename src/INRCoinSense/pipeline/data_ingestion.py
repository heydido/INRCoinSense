import sys

from src.INRCoinSense.components.data_ingestion import DataIngestion
from src.INRCoinSense.config.configuration import ConfigurationManager

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


STAGE_NAME = "Data Ingestion"


class DataIngestionPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.main()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

        data_ingestor = DataIngestionPipeline()
        data_ingestor.main()

        logging.info(f">>>>>> stage '{STAGE_NAME}' completed <<<<<<")

    except Exception as e:
        logging.error(f"Error occurred while running {STAGE_NAME}!")
        raise CustomException(e, sys)
