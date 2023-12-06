import requests

from src.lab7_1.service.services import UserService as user_service, DisplayInTableService
import src.utility.JsonProcessor as json_processor
import src.utility.ColorProcessor as color_processor
import json
import src.utility.FileProcessor as file_processor


def main():
    json_file_path = "./files/result.json"
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
                telegram_username = input("Enter username: ")
                try:
                    jsons = user_service.get_telegram_user_info(telegram_username)
                    print("Choose an option:")
                    print("1. Display data in a flattened way")
                    print("2. Display data in JSON format")
                    print("3. Display data in a table")
                    while True:
                        option = input("Your choice: ")
                        match option:
                            case "1":
                                color_processor.display_colors()
                                color_position = int(input("Enter a color position: "))
                                json_processor.display_flattened_json(jsons, color_position)
                                break
                            case "2":
                                print(json.dumps(jsons, indent=4))
                                break
                            case "3":
                                print(DisplayInTableService.display_user_info(json.dumps(jsons, indent=4)))
                                break
                            case _:
                                print("Invalid option. Enter again!")
                    history.append(
                        f"Data of a personal profile where username is {telegram_username}:\n{json.dumps(jsons, indent=4)}")
                    successful_result = True
                except ValueError as e:
                    print(e)
                    successful_result = False

            case "2":
                jsons = []
                telegram_channel_id = input("Enter Channel name: ")
                try:
                    jsons = user_service.get_telegram_channel_info(telegram_channel_id)
                    print("Choose an option:")
                    print("1. Display data in a flattened way")
                    print("2. Display data in JSON format")
                    print("3. Display data in a table")
                    while True:
                        option = input("Your choice: ")
                        match option:
                            case "1":
                                color_processor.display_colors()
                                color_position = int(input("Enter a color position: "))
                                json_processor.display_flattened_json(jsons, color_position)
                                break
                            case "2":
                                print(json.dumps(jsons, indent=4))
                                break
                            case "3":
                                print(DisplayInTableService.display_channel_info(json.dumps(jsons, indent=4)))
                                break
                            case _:
                                print("Invalid option. Enter again!")
                    history.append(
                        f"Data of a personal profile where username is {telegram_channel_id}:\n{json.dumps(jsons, indent=4)}")
                    successful_result = True
                except ValueError as e:
                    print(e)
                    successful_result = False
            case "3":
                if successful_result:
                    try:
                        file_processor.write_into_json(json_file_path, jsons)
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
                exit(0)
            case _:
                print("Invalid option. Enter again!")


if __name__ == '__main__':
    main()