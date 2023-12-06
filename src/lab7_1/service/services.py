import json
import requests
from prettytable import PrettyTable

import src.lab7_1.config as config
import regex


class UserService:
    @staticmethod
    def get_telegram_user_info(telegram_username: str):
        if telegram_username is None or not isinstance(telegram_username, str):
            raise ValueError('Username has to be a string and nonempty!')

        # Replace the following with Telegram API endpoints
        querystring = {"username": telegram_username}

        headers = {
            "X-RapidAPI-Key": config.X_RapidAPI_Key,
            "X-RapidAPI-Host": config.X_RapidAPI_Host
        }

        # Replace with the Telegram API endpoint for user info
        response = requests.get(config.get_telegram_user_info, headers=headers, params=querystring)

        if response.status_code != 200:
            message: str = response.json()['message']
            raise ValueError(f"Error occurred! {message}")
        else:
            return response.json()

    @staticmethod
    def get_telegram_channel_info(telegram_channel_id: str):
        if telegram_channel_id is None or not isinstance(telegram_channel_id, str):
            raise ValueError("channel ID has to be a string and nonempty!")

        # Replace the following with Telegram API endpoints
        querystring = {"channel": telegram_channel_id}

        headers = {
            "X-RapidAPI-Key": config.X_RapidAPI_Key,
            "X-RapidAPI-Host": config.X_RapidAPI_Host
        }

        # Replace with the Telegram API endpoint for channel info
        response = requests.get(config.get_telegram_channel_info, headers=headers, params=querystring)

        if response.status_code != 200:
            message: str = response.json()['message']
            raise ValueError(f"Error occurred! {message}")
        else:
            return response.json()


class DisplayInTableService:
    @staticmethod
    def display_user_info(json_data: str):
        data = json.loads(json_data)

        # Create an outer PrettyTable
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        # Add simple attributes to the outer table
        for key, value in data.items():
            outer_table.add_row([key, value])

        return outer_table.get_string()

    @staticmethod
    def display_channel_info(json_data: str):
        data = json.loads(json_data)

        # Create an outer PrettyTable
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        # Add simple attributes to the outer table
        for key, value in data.items():
            outer_table.add_row([key, value])

        return outer_table.get_string()
