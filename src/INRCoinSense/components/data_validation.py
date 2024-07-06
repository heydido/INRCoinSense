import os
import sys

from datetime import datetime

from src.INRCoinSense.entity.config_entity import DataValidationConfig
from src.INRCoinSense.config.configuration import ConfigurationManager

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            logging.info("Checking if datasets are present in the dataset directory:")

            validated = False

            expected_datasets = [
                os.path.join(self.config.dataset_dir, dataset) for dataset in self.config.datasets
            ]
            expected_data = [
                os.path.join(expected_dataset, data) for expected_dataset in expected_datasets for data in
                self.config.data
            ]

            all_expected = sorted(expected_datasets + expected_data + [str(self.config.dataset_info)])
            all_available = sorted(
                [root for root, dirs, files in os.walk(self.config.dataset_dir)][1:] + (
                    [str(self.config.dataset_info)] if os.path.exists(self.config.dataset_info) else []
                )
            )

            missing = list(set(all_expected) - set(all_available))

            if not missing:
                validated = True
                logging.info("All datasets are present in the dataset directory!")
                with open(str(self.config.validation_status), 'w') as f:
                    status = (
                        f"Data Validated Successfully at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
                        f"Validation Status: {validated}"
                    )
                    f.write(status)

            else:
                validated = False
                logging.error(f"Some Datasets are missing in the dataset directory! Missing Datasets: {missing}")
                with open(str(self.config.validation_status), 'w') as f:
                    status = (
                        f"Data Validation Failed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
                        f"These datasets are missing: {missing} \n"
                        f"Validation Status: {validated}"
                    )
                    f.write(status)

            return validated

        except Exception as e:
            logging.error(f"Error occurred while validating data!")
            raise CustomException(e, sys)

    def main(self) -> None:
        self.validate_data()


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    data_validation_config = config_manager.get_data_validation_config()

    data_validation = DataValidation(data_validation_config)
    data_validation.main()
