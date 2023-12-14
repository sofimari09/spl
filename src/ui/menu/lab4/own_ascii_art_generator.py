"""
Module: own_ascii_art_generator

This module contains the OwnAsciiArtGeneratorMenu class, which is a menu for
an ASCII art generator program.
"""
from config.paths_config import ASCII_ART_GENERATOR_OUTPUT, OWN_ASCII_ART_GENERATOR_OUTPUT_FONT
from service.lab4.data_processors import TxtProcessor
from shared.color_processor import ColorProcessor
from shared.file_processors import FileProcessor
from ui.menu_builder import Menu


class OwnAsciiArtGeneratorMenu(Menu):
    """Menu class for Own ASCII Art Generator."""

    def run(self):
        """Run the Own ASCII Art Generator program."""
        try:
            initial_text = str(input("Enter text in order to display: "))
            ColorProcessor.display_colors()
            color_position = int(input("Enter position of color you would like to use: "))
            width = int(input("Enter width of text you would like to display: "))
            txt_processor = TxtProcessor(OWN_ASCII_ART_GENERATOR_OUTPUT_FONT)
            text = txt_processor.retrieve(initial_text, color_position, width)
            print(text)
            FileProcessor.write_into_file(ASCII_ART_GENERATOR_OUTPUT, text)
        except KeyError:
            print("Key error! You have entered a wrong value for key of colors, "
                  "or symbols are absent in the file which contains alphabet")
        except ValueError as e:
            print(e)
        except FileNotFoundError:
            print("File not found! Please, check the path to the file")
