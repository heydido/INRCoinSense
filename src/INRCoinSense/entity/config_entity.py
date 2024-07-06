from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    remote_path: str
    local_path: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    dataset_dir: Path
    dataset_info: Path
    datasets: list[str]
    data: list[str]
    validation_status: Path
