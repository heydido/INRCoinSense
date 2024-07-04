from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    remote_path: str
    local_path: Path
    unzip_dir: Path
