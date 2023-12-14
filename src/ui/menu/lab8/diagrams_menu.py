"""
Diagrams Menu Module

This module defines the `DiagramMenu` class, representing a
 menu for displaying diagrams.

Attributes:
- USERS_DATA: Constant variable for the path to user data.

Methods:
- run(self): Run the diagram menu, allowing the user to
choose different types of diagrams.
- display_diagram(diagram_function): Display a diagram
based on user input.

Usage:
1. Import the module: `import ui.menu.lab8.diagrams_menu`
2. Create an instance of `DiagramMenu`.
3. Run the menu using the `run` method.

Note: Ensure the required libraries (`sys`) are
installed before using this module.
"""

from config.paths_config import USERS_DATA
from service.lab8.diagrams_service import DiagramServiceImpl
from ui.menu_builder import Menu


class DiagramMenu(Menu):
    """
    Class representing a menu for displaying diagrams.

    Methods:
        run: Run the diagram menu, allowing the user to
        choose different types of diagrams.
        display_diagram(diagram_function): Display a
        diagram based on user input.
    """

    def run(self):
        """
        Run the diagram menu.

        The menu allows the user to choose different types of diagrams
        to display and provides an option to exit the program.
        """
        service = DiagramServiceImpl(USERS_DATA)

        while True:
            print(
                "1. Display difference in years histogram\n"
                "2. Display sex pie chart\n"
                "3. Display job bar chart\n"
                "4. Display complicated diagram\n"
                "0. Exit\n"
            )

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.display_diagram(service.create_difference_in_years_histogram)
                case "2":
                    self.display_diagram(service.create_sex_pie_chart)
                case "3":
                    self.display_diagram(service.create_job_bar_chart)
                case "4":
                    self.display_diagram(service.create_combined_diagram)
                case "0":
                    break
                case _:
                    print("Invalid choice. Enter again!")

    @staticmethod
    def display_diagram(diagram_function):
        """
        Display a diagram based on user input.

        Args:
            diagram_function (function): The function to create
            and display the diagram.

        Returns:
            None
        """
        has_to_be_downloaded = input(
            "Do you want to download the diagram? Enter 'y' or "
            "anything else not to download: ") == "y"

        diagram_function(has_to_be_downloaded)
