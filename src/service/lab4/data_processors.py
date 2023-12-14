"""Module for processing data from text files."""
import os
from abc import ABC, abstractmethod
import re
from functools import reduce

from colorama import Fore

from shared.color_processor import colors


class DataProcessor(ABC):
    """Abstract base class for processing data from text files."""

    def __init__(self, file_path):
        if file_path is None:
            raise ValueError("File path should have a value")
        self.__file_path = file_path

    @abstractmethod
    def _get_all_data(self) -> None:
        """Abstract method to retrieve all data from the file."""

    @abstractmethod
    def retrieve(self, text, color_position, width) -> str:
        """Abstract method to retrieve formatted text representation."""

    def _read_file(self) -> str:
        """Read the contents of the file."""
        with open(self.__file_path, "r", encoding="utf-8") as file:
            return file.read()


class TxtProcessor(DataProcessor):
    """Implementation class for processing data from text files with a .txt extension."""
    __meta_data = {}
    __data = {}

    def __init__(self, file_path):
        """
        Raises:
            ValueError: If the file extension is incorrect, or the file_path is None
            FileNotFoundError: If the file does not exist in the file system
        """
        if not file_path.endswith(".txt") and os.path.exists(file_path):
            raise ValueError("File should be .txt file")
        super().__init__(file_path)
        self._get_all_data()

    def _get_all_data(self) -> None:
        """
        Retrieves all data from the file and stores it in the appropriate data structure.

        Returns:
            None
        Raises:
            ValueError: If the file has incorrect format.
        """
        file_data = str(self._read_file()).split("\n")
        is_data_annotation_found = False
        representation = ""
        symbol = None

        for line in file_data:
            if is_data_annotation_found:
                if re.match("^@symbol::.$", line):
                    if symbol is not None:
                        self.__data[symbol] = representation
                    symbol = line[9:]
                    representation = ""
                    length = 0
                    counter = 1
                elif re.match("^\\^.+\\$$", line) is not None:
                    if counter == 1:
                        length = line.__sizeof__()
                    if line.__sizeof__() != length:
                        raise ValueError("Length of the row has to be equal "
                                         "within a certain character in the file")
                    representation += (line[1:-1] +
                                       ("" if counter == self.__meta_data["height"] else "\n"))
                    counter += 1
                else:
                    raise ValueError("Data information has incorrect format")
            elif line == "@data":
                if "height" not in self.__meta_data:
                    raise ValueError("The file has to contain meta information such as height")
                is_data_annotation_found = True
            elif not is_data_annotation_found:
                if re.match("^\\w+::\\d+$", line) is not None:
                    parts = line.split("::")
                    self.__meta_data[parts[0]] = int(parts[1])
                else:
                    raise ValueError("Metadata has incorrect format")

    def retrieve(self, text, color_position, width) -> str:
        """
        Retrieve the text representation of the given input text by formatting
        it into rows with a maximum width.

        Args:
            text (str): The input text to be formatted.
            color_position (int): The index of the color in the `colors`
            list to be applied to the formatted text.
            width (int): The maximum width of each row in the formatted text.

        Returns:
            str: The formatted text representation of the input text, with
            the specified color applied.

        Raises:
            ValueError: If the width of the text is too small to fit within the specified width.
            KeyError: If the color position is not a valid index in the `colors` list,
            or if the symbol is absent
            in the file
        """
        result = {}
        all_needed_symbols = {}
        properties = {}
        row_count = 0
        current_position_in_row = 0

        for i in range(0, len(text)):
            representation = str(self.__data[text[i]]).split("\n")
            if current_position_in_row + len(representation[0]) > width:
                if len(representation[0]) > width:
                    raise ValueError("Width of the text is too small")
                row_count += 1
                current_position_in_row = 0
                current_position_in_row += len(representation[0])
                if row_count in properties:
                    properties[row_count] += 1
                else:
                    properties[row_count] = 1
            else:
                current_position_in_row += len(representation[0])
                if row_count in properties:
                    properties[row_count] += 1
                else:
                    properties[row_count] = 1
            all_needed_symbols.update({i: reduce((lambda x, y: x + "\n" + y), representation)})

        symbol_count = 0
        for i in properties:
            for _ in range(0, properties[i]):
                representation = all_needed_symbols[symbol_count].split("\n")
                symbol_count += 1
                for k in range(0, len(representation)):
                    if k + i * 6 in result:
                        result[k + i * 6] += representation[k]
                    else:
                        result[k + i * 6] = representation[k]

        return (getattr(Fore, colors[color_position]) +
                reduce(lambda x, y: x + "\n" + y, result.values()))
