"""
LinkedIn User Service Module

This module provides methods for retrieving personal profiles and posts from
LinkedIn. It includes two classes:

1. `UserService`:
    - `get_personal_profile(linkedin_url: str) -> dict`: Fetches and returns
    personal profile data from LinkedIn.
    - `get_profiles_posts(linkedin_url: str) -> dict`: Fetches and returns
     posts data from LinkedIn.

2. `DisplayInTableService`:
    - `display_personal_profile(json_data: str) -> str`: Displays personal
    profile data in a table format.
    - `display_profiles_posts(json_data: str, result="") -> str`:
    Displays posts data in a table format.

Usage:
1. Import the module: `import service.lab7.user_service`
2. Use the classes and methods for fetching and displaying LinkedIn data.

Note: Ensure the required libraries (`requests`, `prettytable`, `regex`)
are installed before using this module.
You can install them using: `pip install requests prettytable regex`
"""
import pyfiglet
from colorama import Fore


from config.paths_config import ASCII_ART_GENERATOR
from shared.color_processor import colors, fonts, FontProcessor, ColorProcessor
from shared.file_processors import FileProcessor


class AsciiArtGeneratorService:
    """
    Provides a service for generating and displaying ASCII art.

    Attributes:
    - __file_processor (FileProcessor): An instance of FileProcessor for file processing.

    Methods:
    - __init__.py(self): Initializes an AsciiArtGeneratorService object.
    - __get_text(self, text, font, color_position, width) -> str: Generates
    formatted ASCII art text.
    - display_text(self): Takes user input to generate and display ASCII art,
     and writes it to a file.
    """

    def __init__(self):
        """
        Initializes an AsciiArtGeneratorService object.
        """
        self.__file_processor = FileProcessor()

    @staticmethod
    def __get_text(text, font, color_position, width) -> str:
        """
        Generates formatted ASCII art text.

        Parameters:
        - text (str): The input text for generating ASCII art.
        - font (str): The font style to be used for ASCII art.
        - color_position (int): The position of the color to be applied to the ASCII art.
        - width (int): The width of the ASCII art text.

        Returns:
        - str: The formatted ASCII art text.
        """
        fig = pyfiglet.Figlet(font)
        fig.width = width
        formatted_text = fig.renderText(text)
        return getattr(Fore, colors[color_position]) + formatted_text

    def display_text(self):
        """
        Takes user input to generate and display ASCII art, and writes it to a file.

        Raises:
        - ValueError: If input cannot be parsed into an integer.
        - KeyError: If an incorrect value is entered for the key of fonts or color.
        - pyfiglet.CharNotPrinted: If a character is not printable in ASCII art.
        """
        while True:
            try:
                initial_text = str(input("Enter text containing all ASCII characters "
                                         "in order to display: "))
                if not initial_text.isascii():
                    print("Text must contain only ASCII characters")
                    continue
                FontProcessor.display_fonts()
                font_position = int(input("Enter position of font you would like to use: "))
                ColorProcessor.display_colors()
                color_position = int(input("Enter position of color you would like to use: "))
                width = int(input("Enter width of text you "
                                  "would like to display: "))
                modified_text = self.__get_text(initial_text, fonts[font_position],
                                                color_position, width)
                print(modified_text)
                self.__file_processor.write_into_file(ASCII_ART_GENERATOR, modified_text)

                if input(
                        "Would you like to continue? Enter 'Y' or 'y' if you do, or "
                        "anything else if you don't. Your response is ").lower() != "y":
                    break
            except ValueError:
                print("Cannot be parsed into an int value")
            except KeyError:
                print("You have entered a wrong value for the key of fonts or color")
            except pyfiglet.CharNotPrinted as e:
                print(str(e))
