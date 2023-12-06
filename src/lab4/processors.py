import os
from abc import ABC, abstractmethod
import colorama
from colorama import Fore
import re
from functools import reduce

colorama.init(autoreset=True)
colors = dict(enumerate(sorted(Fore.__dict__.keys())))


class DataProcessor(ABC):

    def __init__(self, file_path):
        if file_path is None:
            raise ValueError("File path should have a value")
        self.__file_path = file_path

    @abstractmethod
    def _get_all_data(self) -> None:
        pass

    @abstractmethod
    def retrieve(self, text, color, width) -> str:
        pass

    def _read_file(self) -> str:
        with open(self.__file_path, "r") as file:
            return file.read()

    @staticmethod
    def display_colors() -> None:
        for i in colors:
            print(str(i) + ". " + colors[i])


class TxtProcessor(DataProcessor):
    __meta_data = dict()
    __data = dict()

    """
    Raises:
        ValueError: If the file extension is incorrect, or the file_path is None
        FileNotFoundError: If the file does not exist in the file system
    """

    def __init__(self, file_path):
        if not file_path.endswith(".txt") and os.path.exists(file_path) is True:
            raise ValueError("File should be .txt file")
        super().__init__(file_path)
        self._get_all_data()

    """
    Retrieves all data from the file and stores it in the appropriate data structure.

    Returns:
        None
    Raises:
        ValueError: If the file has incorrect format.
    """

    def _get_all_data(self) -> None:
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
                        raise ValueError("Length of the row has to be equal within a certain character in the file")
                    representation += line[1:-1] + ("" if counter == self.__meta_data["height"] else "\n")
                    counter += 1
                else:
                    raise ValueError("Data information has incorrect format")
            elif line == "@data":
                if not self.__meta_data.__contains__("height"):
                    raise ValueError("The file has to contain meta information such as height")
                is_data_annotation_found = True
            elif not is_data_annotation_found:
                if re.match("^\\w+::\\d+$", line) is not None:
                    parts = line.split("::")
                    self.__meta_data[parts[0]] = int(parts[1])
                else:
                    raise ValueError("Metadata has incorrect format")

    """
    Retrieve the text representation of the given input text by formatting it into rows with a maximum width.

    Args:
        text (str): The input text to be formatted.
        color_position (int): The index of the color in the `colors` list to be applied to the formatted text.
        width (int): The maximum width of each row in the formatted text.

    Returns:
        str: The formatted text representation of the input text, with the specified color applied.

    Raises:
        ValueError: If the width of the text is too small to fit within the specified width.
        KeyError: If the color position is not a valid index in the `colors` list, or if the symbol is absent in the file
    """

    def retrieve(self, text, color_position, width) -> str:
        result = dict()
        all_needed_symbols = dict()
        properties = dict()
        row_count = 0
        current_position_in_row = 0

        for i in range(0, len(text)):
            representation = str(self.__data[text[i]]).split("\n")
            if current_position_in_row + representation[0].__len__() > width:
                if representation[0].__len__() > width:
                    raise ValueError("Width of the text is too small")
                row_count += 1
                current_position_in_row = 0
                current_position_in_row += representation[0].__len__()
                if properties.__contains__(row_count):
                    properties[row_count] += 1
                else:
                    properties[row_count] = 1
            else:
                current_position_in_row += representation[0].__len__()
                if properties.__contains__(row_count):
                    properties[row_count] += 1
                else:
                    properties[row_count] = 1
            all_needed_symbols.update({i: reduce((lambda x, y: x + "\n" + y), representation)})

        symbol_count = 0
        for i in properties.keys():
            for j in range(0, properties[i]):
                representation = all_needed_symbols[symbol_count].split("\n")
                symbol_count += 1
                for k in range(0, len(representation)):
                    if result.__contains__(k + i * 6):
                        result[k + i * 6] += representation[k]
                    else:
                        result[k + i * 6] = representation[k]

        return Fore.__getattribute__(colors[color_position]) + reduce(lambda x, y: x + "\n" + y, result.values())
