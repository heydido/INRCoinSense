import sys

from src.INRCoinSense.pipeline.data_ingestion import DataIngestionPipeline
from src.INRCoinSense.pipeline.data_validation import DataValidationPipeline
from src.INRCoinSense.pipeline.model_training import ModelTrainingPipeline

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


logging.info(">>>>>> INRCoinSense Pipeline started <<<<<<\n")

STAGE_NAME = "Data Ingestion"

try:
    logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

    data_ingestor = DataIngestionPipeline()
    data_ingestor.main()

    logging.info(f">>>>>> stage '{STAGE_NAME}' completed <<<<<<\n")

except Exception as e:
    logging.error(f"Error occurred while running {STAGE_NAME}!")
    raise CustomException(e, sys)


STAGE_NAME = "Data Validation"

try:
    logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

    data_validator = DataValidationPipeline()
    data_validator.main()

    logging.info(f">>>>>> stage '{STAGE_NAME}' completed <<<<<<\n")

except Exception as e:
    logging.error(f"Error occurred while running {STAGE_NAME}!")
    raise CustomException(e, sys)


STAGE_NAME = "Model Training"

try:
    logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

    model_trainer = ModelTrainingPipeline()
    model_trainer.main()

    logging.info(f">>>>>> stage '{STAGE_NAME}' completed <<<<<<\n")

    logging.info(">>>>>> INRCoinSense Pipeline completed successfully <<<<<<")

except Exception as e:
    logging.error(f"Error occurred while running {STAGE_NAME}!")
    raise CustomException(e, sys)
