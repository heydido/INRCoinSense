import sys

from dagshub import get_repo_bucket_client

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


def upload_file(local_path, remote_path):
    try:
        logging.info("Getting S3 client")

        s3 = get_repo_bucket_client("heydido/INRCoinSense")

        logging.info("S3 client obtained successfully")

        logging.info(f"Uploading file from {local_path} to {remote_path}")

        s3.upload_file(
            Bucket="INRCoinSense",  # name of the repo
            Filename=local_path,  # local path of file to upload
            Key=remote_path,  # remote path where to upload the file
        )

        logging.info(f"File uploaded successfully from {local_path} to {remote_path}")

    except Exception as e:
        logging.error(f"Error uploading file from {local_path} to {remote_path}")
        raise CustomException(e, sys)


def download_file(local_path, remote_path):
    try:
        logging.info("Getting S3 client")

        s3 = get_repo_bucket_client("heydido/INRCoinSense")

        logging.info("S3 client obtained successfully")

        logging.info(f"Downloading file from {remote_path} to {local_path}")

        s3.download_file(
            Bucket="INRCoinSense",  # name of the repo
            Key=remote_path,  # remote path from where to download the file
            Filename=local_path,  # local path where to download the file
        )

        logging.info(f"File downloaded successfully from {remote_path} to {local_path}")

    except Exception as e:
        logging.error(f"Error downloading file from {remote_path} to {local_path}")
        raise CustomException(e, sys)


if __name__ == "__main__":
    pass
