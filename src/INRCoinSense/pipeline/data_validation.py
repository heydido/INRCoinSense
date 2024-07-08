import sys


from src.INRCoinSense.config.configuration import ConfigurationManager
from src.INRCoinSense.components.data_validation import DataValidation

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


STAGE_NAME = "Data Validation"


class DataValidationPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)
        data_validation.main()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

        data_validator = DataValidationPipeline()
        data_validator.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

    except Exception as e:
        logging.error(f"Error occurred while running {STAGE_NAME}!")
        raise CustomException(e, sys)
