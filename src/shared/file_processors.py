"""
Module docstring for service.lab8.diagrams_service

This module provides a service for creating various diagrams based on user data
using the `matplotlib` library.

Classes:
- DiagramService: Abstract base class for creating diagrams based on user data.
- DiagramServiceImpl: Implementation class for creating diagrams based on user data.
"""
import json
import pandas as pd

from config.logger_config import logger

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


class FileProcessor:
    """
    FileProcessor is a class which interacts with files. It is used for reading and writing
    """

    @staticmethod
    def write_into_file(file_path: str, text: str) -> None:
        """
        Write text into a file. May raise PermissionError or OSError.

        :param file_path:
        :param text:
        :raises PermissionError: If the user does not have permission to write to the file.
        :raises OSError: If the file is not a file.
        :raises FileNotFoundError: If the file does not exist.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            file.write(text)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Read text from a file. May raise FileNotFoundError, PermissionError, or OSError.

        :param file_path: The path to the file to read from.
        :return: The content of the file as a string.
        :raises FileNotFoundError: If the file does not exist.
        :raises PermissionError: If the user does not have permission to read the file.
        :raises OSError: If the file is not a file.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            logger.info("Reading from file %s", file_path)
            return file.read()

    @staticmethod
    def read_from_json(file_path: str) -> dict:
        """
        Read a JSON file. May raise FileNotFoundError, PermissionError, or OSError.

        :param file_path: The path to the file to read from.
        :return: The content of the file as a dictionary.
        :raises FileNotFoundError: If the file does not exist.
        :raises PermissionError: If the user does not have permission to read the file.
        :raises OSError: If the file is not a file.
        :raises JSONDecodeError: If the file is not a valid JSON file.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            return json.load(file)

    @staticmethod
    def write_into_json(file_path: str, jsons: list) -> None:
        """
        Write a JSON text into a file.

        :param jsons:
        :param file_path: The path to the file to read from.
        :raises FileNotFoundError: If the file does not exist.
        :raises PermissionError: If the user does not have permission to read the file.
        :raises OSError: If the file is not a file.
        :raises JSONDecodeError: If the file is not a valid JSON file.
        """
        if not isinstance(file_path, str):
            logger.critical("Wrong data type: %s. It has to be string!", type(file_path))
            raise TypeError("Type of file_path must be string")
        if not isinstance(jsons, list):
            logger.critical("Wrong data type: %s. It has to be list!", type(jsons))
            raise TypeError("Type of jsons must be list")

        jsons_text_representation = json.dumps(jsons, indent=4)
        json.loads(jsons_text_representation)

        with open(file_path, "w", encoding="utf-8") as file:
            logger.info("Writing into file %s", file_path)
            file.write(jsons_text_representation)


class CsvProcessor:
    """
    CsvProcessor is used to interact with csv-files
    """

    @staticmethod
    def read(file_path: str) -> pd.DataFrame:
        """
        Read a CSV file into a pandas DataFrame. May raise FileNotFoundError,
        PermissionError, or OSError.
        :param file_path:
        :return:
        """
        if not isinstance(file_path, str):
            logger.critical("Wrong data type: %s. It has to be string!",
                            type(file_path))
            raise TypeError("Type of file_path must be string")
        return pd.read_csv(file_path)
