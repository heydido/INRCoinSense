from pathlib import Path
from dagshub import get_repo_bucket_client

from src.INRCoinSense.utils.common import exception_handler, log_handler


class DagsHubUtility:
    def __init__(self):
        self.bucket_name = "INRCoinSense"
        self.s3 = get_repo_bucket_client("heydido/INRCoinSense")

    @log_handler
    @exception_handler
    def upload_file(self, local_path: Path, remote_path: Path) -> None:
        self.s3.upload_file(
            Bucket=self.bucket_name,
            Filename=local_path,
            Key=remote_path,
        )

    @log_handler
    @exception_handler
    def download_file(self, local_path: Path, remote_path: Path) -> None:
        self.s3.download_file(
            Bucket=self.bucket_name,
            Key=remote_path,
            Filename=local_path,
        )
