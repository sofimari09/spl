"""
Module: UserMenu

This module defines a menu class for interacting with user data. It includes options to display
personal profile data, display profiles posts, save data in JSON format, show history, and exit.

Classes:
- UserMenu: A menu class for interacting with user data.

Usage:
- Instantiate the UserMenu class and call the run method to start the user data interaction program.

Example:
```python
menu = UserMenu()
menu.run()
"""
import json

from config.paths_config import JSON_FILE_PATH
from service.lab7.user_service import DisplayInTableService, UserService
from shared.color_processor import ColorProcessor
from shared.file_processors import FileProcessor
from shared.json_processor import JSONProcessor
from ui.menu_builder import Menu


class UserMenu(Menu):
    """A menu class for interacting with user data."""

    def run(self):
        """Run the user data interaction program."""
        history: list = []
        successful_result: bool = False
        jsons: list = []

        while True:
            print("Choose an option:")
            print("1. Display user info")
            print("2. Display channel info")
            print("3. Save data in JSON format")
            print("4 - Show history")
            print("0 - Exit")

            option = input("Your choice: ")
            match option:
                case "1":
                    jsons = []
                    linkedin_url = input("Enter LinkedIn URL: ")
                    try:
                        jsons = UserService.get_personal_profile(linkedin_url)
                        print("Choose an option:")
                        print("1. Display data in a flattened way")
                        print("2. Display data in JSON format")
                        print("3. Display data in a table")
                        while True:
                            option = input("Your choice: ")
                            match option:
                                case "1":
                                    ColorProcessor.display_colors()
                                    color_position = int(input("Enter a color position: "))
                                    JSONProcessor.display_flattened_json(jsons, color_position)
                                    break
                                case "2":
                                    print(json.dumps(jsons, indent=4))
                                    break
                                case "3":
                                    print(DisplayInTableService.display_personal_profile(
                                        json.dumps(jsons, indent=4)))
                                    break
                                case _:
                                    print("Invalid option. Enter again!")
                        history.append(
                            f"Data of a personal profile where URL is "
                            f"{linkedin_url}:\n{json.dumps(jsons, indent=4)}")
                        successful_result = True
                    except ValueError as e:
                        print(e)
                        successful_result = False

                case "2":
                    jsons = []
                    linkedin_url = input("Enter LinkedIn URL: ")
                    try:
                        jsons = UserService.get_profiles_posts(linkedin_url)
                        print("Choose an option:")
                        print("1. Display data in a flattened way")
                        print("2. Display data in JSON format")
                        print("3. Display data in a table")
                        while True:
                            option = input("Your choice: ")
                            match option:
                                case "1":
                                    ColorProcessor.display_colors()
                                    color_position = int(input("Enter a color position: "))
                                    JSONProcessor.display_flattened_json(jsons, color_position)
                                    break
                                case "2":
                                    print(json.dumps(jsons, indent=4))
                                    break
                                case "3":
                                    print(DisplayInTableService.display_profiles_posts(
                                        json.dumps(jsons, indent=4)))
                                    break
                                case _:
                                    print("Invalid option. Enter again!")
                        history.append(
                            f"Data of a personal profile where URL is "
                            f"{linkedin_url}:\n{json.dumps(jsons, indent=4)}")
                        successful_result = True
                    except ValueError as e:
                        print(e)
                        successful_result = False
                case "3":
                    if successful_result:
                        try:
                            FileProcessor.write_into_json(JSON_FILE_PATH, jsons)
                        except Exception as e:
                            print(e)
                    else:
                        print("No data to save!")
                case "4":
                    if len(history) == 0:
                        print("No history!")
                    else:
                        for counter, item in enumerate(history):
                            print(f"{counter + 1}: {item}")
                case "0":
                    break
                case _:
                    print("Invalid option. Enter again!")
