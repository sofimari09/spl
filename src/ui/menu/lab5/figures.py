"""
Module: ui.menu.lab5.figures

A module for handling 3D figures and their representations.

Classes:
- FigureMenu: A menu class for managing 3D figures and their representations.
"""
from config.paths_config import FIGURE_2D, FIGURE_3D
from service.lab5.figures_service import Figure3D, Cube
from shared.color_processor import colors, ColorProcessor
from shared.file_processors import FileProcessor
from ui.menu_builder import Menu


class FigureMenu(Menu):
    """A menu class for managing 3D figures and their representations."""

    def __init__(self):
        """Initialize the FigureMenu."""
        self.__is_figure_available = False
        self.__is_2d_representation_available = False
        self.__is_3d_representation_available = False
        self.__figure = None
        self.__representation_2d_file = FIGURE_2D
        self.__representation_3d_file = FIGURE_3D

    @staticmethod
    def __get_character_input():
        """Get a character input for representing the shape."""
        while True:
            character = input("Enter a character to represent in the shape: ")
            if Figure3D.is_appropriate_character(character) is False:
                print("You should have entered one character!")
            else:
                return character

    @staticmethod
    def __get_color_position_input():
        """Get a color input for representing the shape."""
        while True:
            try:
                color = int(input("Enter a number of color: "))
                if color not in range(len(colors)):
                    print("You should have entered a color option which is available!")
                else:
                    return color
            except ValueError:
                print("You should have entered an integer number!")

    @staticmethod
    def __get_length_input():
        """Get a length input for creating a cube."""
        while True:
            try:
                length = int(input("Enter a length: "))
                if length <= 0:
                    print("You should have entered a length greater than 0!")
                else:
                    return length
            except ValueError:
                print("You should have entered an integer number!")

    @staticmethod
    def __get_scale_input():
        """Get a scale input for displaying 3D representations."""
        while True:
            try:
                scale = float(input("Enter a scale for figure: "))
                if scale <= 0:
                    print("You should have entered a scale greater than 0!")
                else:
                    return scale
            except ValueError:
                print("You should have entered a float number!")

    def __create_cube(self):
        """Create a cube based on user input."""
        character = self.__get_character_input()
        print("There are such colors available:")
        ColorProcessor.display_colors()
        color_position = self.__get_color_position_input()
        length = self.__get_length_input()
        try:
            self.__figure = Cube(length, character, color_position)
            self.__is_figure_available = True
        except ValueError as e:
            print(e)
            self.__is_figure_available = False

    def __display_2d(self):
        """Display the 2D representation of the figure."""
        if self.__is_figure_available is True:
            representation_2d = self.__figure.get_2d_representation()
            for item in representation_2d:
                print(item)
            self.__is_2d_representation_available = True
        else:
            print("There is no figure available!")

    def __display_3d(self):
        """Display the 3D representation of the figure."""
        if self.__is_figure_available is True:
            representation_3d = self.__figure.get_3d_representation(scale=self.__get_scale_input())
            print(representation_3d)
            self.__is_3d_representation_available = True
        else:
            print("There is no figure available!")

    def __save_2d_representation(self):
        """Save the 2D representation of the figure to a file."""
        if self.__is_2d_representation_available is True:
            try:
                FileProcessor.write_into_file(self.__representation_2d_file, ""
                                              .join(self.__figure.get_2d_representation()))
            except PermissionError:
                print("You do not have permission to write to the file!")
            except FileNotFoundError:
                print("The file does not exist!")
        else:
            print("There is no figure available!")

    def __save_3d_representation(self):
        """Save the 3D representation of the figure to a file."""
        if self.__is_3d_representation_available is True:
            try:
                FileProcessor.write_into_file(
                    self.__representation_3d_file,
                    self.__figure.get_3d_representation(scale=self.__get_scale_input()))
            except PermissionError:
                print("You do not have permission to write to the file!")
            except FileNotFoundError:
                print("The file does not exist!")
        else:
            print("There is no figure available!")

    def run(self):
        """Run the FigureMenu program."""
        while True:
            print("1 - Create a cube")
            print("2 - Display 2D")
            print("3 - Display 3D")
            print("4 - Save 2D")
            print("5 - Save 3D")
            print("0 - Exit")
            option = str(input("Enter an option: "))

            match option:
                case "1":
                    self.__create_cube()
                case "2":
                    self.__display_2d()
                case "3":
                    self.__display_3d()
                case "4":
                    self.__save_2d_representation()
                case "5":
                    self.__save_3d_representation()
                case "0":
                    break
                case _:
                    print("Invalid option!")
