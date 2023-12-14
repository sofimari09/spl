"""
Figures Service Module

This module provides a service for working with 3D figures. It includes two classes:

- `Figure3D` (abstract class):
  - Attributes:
    - `_character (str)`: The character representing the figure.
    - `_color_position (int)`: The position of the color to be
    applied to the figure.
  - Methods:
    - `__init__.py(self, character: str, color_position: int)`:
    Initializes a Figure3D object.
    - `get_2d_representation(self) -> list`: Abstract method
    to get the 2D representation of the figure.
    - `get_3d_representation(self) -> str`: Abstract method
    to get the 3D representation of the figure.
    - `is_appropriate_character(character: str) -> bool`:
    Static method to check if the character is appropriate.

- `Cube` (inherits from `Figure3D`):
  - Attributes:
    - `__length (int)`: The length of the cube.
  - Methods:
    - `__init__.py(self, length: int, character: str, color_position: int)`:
    Initializes a Cube object.
    - `get_2d_representation(self) -> list`: Gets the 2D representation
    of the cube.
    - `get_3d_representation(self, scale: float = 1.0) -> str`: Gets the
    3D representation of the cube.

Usage:
1. Import the module: `import service.lab5.figures_service`
2. Create an instance of `Cube` or a custom class that inherits from `Figure3D`.
3. Use the provided methods to work with 3D figures.

Note: Ensure the required libraries (`colorama`) are installed
before using this module.
You can install it using: `pip install colorama`
"""
from abc import ABC, abstractmethod

from colorama import Fore

from shared.color_processor import colors


class Figure3D(ABC):
    """
    An abstract class for 3D figures.

    Attributes:
    - _character (str): The character representing the figure.
    - _color_position (int): The position of the color to be applied to the figure.

    Methods:
    - __init__.py(self, character: str, color_position: int): Initializes
    a Figure3D object.
    - get_2d_representation(self) -> list: Abstract method to get the 2D
    representation of the figure.
    - get_3d_representation(self) -> str: Abstract method to get the 3D
    representation of the figure.
    - is_appropriate_character(character: str) -> bool: Static
    method to check if the character is appropriate.
    """

    def __init__(self, character: str, color_position: int):
        """
        Initializes a Figure3D object.

        Parameters:
        - character (str): The character representing the figure.
        - color_position (int): The position of the color to be applied to the figure.
        """
        if not colors.__contains__(color_position):
            raise ValueError("Color position must be in range of available colors")
        if self.is_appropriate_character(character) is False:
            raise ValueError("It supposed to be only one character instead")
        self._character = character
        self._color_position = color_position

    @abstractmethod
    def get_2d_representation(self) -> list:
        """
        Abstract method to get the 2D representation of the figure.

        Returns:
        - list: A list containing the 2D representation of the figure.
        """
        pass  # pylint: disable=unnecessary-pass

    @abstractmethod
    def get_3d_representation(self) -> str:
        """
       Abstract method to get the 3D representation of the figure.

       Returns:
       - str: The 3D representation of the figure.
       """
        pass  # pylint: disable=unnecessary-pass

    @staticmethod
    def is_appropriate_character(character: str) -> bool:
        """
       Static method to check if the character is appropriate.

       Parameters:
       - character (str): The character to be checked.

       Returns:
       - bool: True if the character is appropriate, False otherwise.
       """
        return len(character) == 1


class Cube(Figure3D):
    """
    Represents a 3D cube.

    Attributes:
    - __length (int): The length of the cube.
    - __offset (int): The offset for cube representation.

    Methods:
    - __init__.py(self, length: int, character: str, color_position: int):
    Initializes a Cube object.
    - get_2d_representation(self) -> list: Gets the 2D representation of the cube.
    - get_3d_representation(self, scale: float = 1.0) -> str:
     Gets the 3D representation of the cube.

    Example:
    >>> cube = Cube(3, "*", 1)
    >>> cube.get_3d_representation()
    '3D representation of the cube with color applied.'

    """

    def __init__(self, length: int, character: str, color_position: int):
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        super().__init__(character, color_position)
        self.__length = length

    def get_2d_representation(self) -> list:
        """
        Gets the 2D representation of the cube.

        Returns:
        - list: A list of 2D representations of the cube.
        """
        result = ""
        for row in range(self.__length):
            for col in range(self.__length):
                if row == 0 or row == self.__length - 1:
                    result += f"{self._character}  "
                elif col == 0 or col == self.__length - 1:
                    result += f"{self._character}  "
                else:
                    result += "   "
            result += "\n"

        return [getattr(Fore, colors[self._color_position]) + "\n" + result for _ in range(6)]

    def get_3d_representation(self, scale: float = 1.0) -> str:
        """
        Gets the 3D representation of the cube.

        Parameters:
        - scale (float): The scaling factor for the cube representation.

        Returns:
        - str: The 3D representation of the cube with color applied.
        """
        modified_length = int(self.__length * scale) \
            if self.__length * scale >= 2 else self.__length
        modified_offset = int(modified_length / 2 + 1)
        result = ""

        for row in range(modified_offset - 1):
            for col in range(modified_length + modified_offset - 1):
                if (row + col == modified_offset - 1) or (row == 0 and col > modified_offset - 1):
                    result += f"{self._character}" + (
                        "" if col == modified_length + modified_offset - 2 and row == 0 else "  ")
                elif modified_length + modified_offset - row == col + 2:
                    result += f"{self._character}"
                elif col == modified_length + modified_offset - 2:
                    result += f"  {self._character}"
                else:
                    result += "   "
            result += "\n"

        for row in range(modified_length):
            for col in range(modified_length + modified_offset):
                if ((row == 0 or row == modified_length - 1) and col < modified_length or (
                        col == 0 or col == modified_length - 1) and
                        row < modified_length and col < modified_length):
                    result += f"{self._character}" + (
                        "" if row == modified_length - 1
                              and col == modified_length - 1 else "  ")
                elif (row + col == (modified_length - 1) * 2 and col < modified_length
                      + modified_offset - 1):
                    result += "   " * (modified_length - row - 2) + f"{self._character}"
                elif col < modified_length and row < modified_length:
                    result += "   "
                elif row < modified_length - modified_offset and col > modified_length:
                    if col == modified_offset + modified_length - 1:
                        result += f"{self._character}"
                    else:
                        result += "   "

            result += "\n"

        return getattr(Fore, colors[self._color_position]) + "\n" + result
