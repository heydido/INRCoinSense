import os
import sys
import yaml

from pathlib import Path
from box import ConfigBox
from functools import wraps

from src.INRCoinSense.logger import logging
from src.INRCoinSense.exception import CustomException


def exception_handler(func: callable) -> callable:
    """
    This function is used to handle exceptions. It wraps the function and catches any exception raised by the function.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise CustomException(e, sys)
    return wrapper


def log_handler(func: callable) -> callable:
    """
    This function is used to log the function name, arguments and keyword arguments before and after the function is
    executed.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' executed successfully!")
        return result
    return wrapper


@log_handler
@exception_handler
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns ConfigBox type object

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox typ
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)


@log_handler
@exception_handler
def create_directories(path_to_directories: list[Path]):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path of directories

    Returns:
        None
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Directory created successfully: {path}")
        else:
            logging.info(f"Directory already exists: {path}. Skipping creating directory!")


@log_handler
@exception_handler
def get_size(path: Path) -> str:
    """
    Get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
