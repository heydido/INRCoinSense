import sys

from src.INRCoinSense.components.model_training import ModelTraining
from src.INRCoinSense.config.configuration import ConfigurationManager

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_trainer = ModelTraining(config=model_training_config)
        model_trainer.main()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

        model_training = ModelTrainingPipeline()
        model_training.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

    except Exception as e:
        logging.error(f"Error occurred while running {STAGE_NAME}!")
        raise CustomException(e, sys)
