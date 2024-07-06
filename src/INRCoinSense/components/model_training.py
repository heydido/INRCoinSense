import os
import sys
import yaml

from src.INRCoinSense.utils.common import read_yaml
from src.INRCoinSense.entity.config_entity import ModelTrainingConfig
from src.INRCoinSense.config.configuration import ConfigurationManager

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train_model(self) -> None:
        try:
            logging.info("Reading dataset info:")
            dataset_info = read_yaml(self.config.dataset_info)
            num_classes = dataset_info.nc
            names = dataset_info.names
            logging.info(f"Number of classes in the dataset: {num_classes}. Names: {names}")

            with open(self.config.dataset_info, 'r') as f:
                dataset_info = yaml.safe_load(f)
            datasets = {
                "train": f"../artifacts/data_ingestion/dataset/train/images",
                "val": f"../artifacts/data_ingestion/dataset/valid/images",
                "test": f"../artifacts/data_ingestion/dataset/test/images"
            }
            for dataset in datasets:
                dataset_info[dataset] = datasets[dataset]
            with open(self.config.dataset_info, 'w') as f:
                yaml.dump(dataset_info, f, indent=4)

            logging.info(f"Creating custom_{self.config.model} config file for training:")
            with open(os.path.join("yolov5/models", f"{self.config.model}.yaml")) as f:
                model_config = yaml.safe_load(f)
            model_config["nc"] = num_classes
            with open(os.path.join("yolov5/models", f"custom_{self.config.model}.yaml"), 'w') as f:
                yaml.dump(model_config, f)
            logging.info(f"Config file: custom_{self.config.model}.yaml created successfully!")

            parameters = {
                "img_size": self.config.img_size,
                "batch_size": self.config.batch_size,
                "epochs": self.config.epochs,
                "weights": f"{self.config.model}.pt"
            }

            logging.info(f"Training model with parameters: {parameters}")

            os.system(
                f"""
                cd yolov5/ && python train.py 
                --img {self.config.img_size} 
                --batch {self.config.batch_size} 
                --epochs {self.config.epochs} 
                --data {self.config.dataset_info} 
                --cfg ./models/custom_{self.config.model}.yaml 
                --weights {self.config.model}.pt
                --name {self.config.model}_results 
                --cache True"
                """
            )

        except Exception as e:
            logging.error(f"Error occurred while training model!")
            raise CustomException(e, sys)

    def main(self):
        self.train_model()


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    model_training_config = config_manager.get_model_training_config()

    model_training = ModelTraining(model_training_config)
    model_training.main()
