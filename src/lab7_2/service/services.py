import json

import requests
from prettytable import PrettyTable

import src.lab7_1.config as config
import regex


class UserService:
    @staticmethod
    def get_personal_profile(linkedin_url: str):
        if linkedin_url is None or not isinstance(linkedin_url, str):
            raise ValueError("URL has to be a string and nonempty!")
        elif regex.match("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b(["
                         "-a-zA-Z0-9@:%._\\+~#?&//=]*)$", linkedin_url) is None:
            raise ValueError("URL doesn't match the pattern!")
        querystring = {"linkedin_url": linkedin_url, "include_skills": "false"}

        headers = {
            "X-RapidAPI-Key": config.X_RapidAPI_Key,
            "X-RapidAPI-Host": config.X_RapidAPI_Host
        }
        response = requests.get(config.get_personal_profile, headers=headers, params=querystring)
        if response.status_code != 200:
            message: str = response.json()['message']
            raise ValueError(f"Error occurred! {message}")
        else:
            return response.json()

    @staticmethod
    def get_profiles_posts(linkedin_url: str):
        if linkedin_url is None or not isinstance(linkedin_url, str):
            raise ValueError("URL has to be a string and nonempty!")
        elif regex.match("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b(["
                         "-a-zA-Z0-9@:%._\\+~#?&//=]*)$", linkedin_url) is None:
            raise ValueError("URL doesn't match the pattern!")

        querystring = {"linkedin_url": linkedin_url, "type": "posts"}

        headers = {
            "X-RapidAPI-Key": config.X_RapidAPI_Key,
            "X-RapidAPI-Host": config.X_RapidAPI_Host
        }
        response = requests.get(config.get_profiles_posts, headers=headers, params=querystring)
        if response.status_code != 200:
            message: str = response.json()['message']
            raise ValueError(f"Error occurred! {message}")
        else:
            return response.json()


class DisplayInTableService:
    @staticmethod
    def display_personal_profile(json_data: str):
        data = json.loads(json_data)
        isExpereinces = False
        isEducations = False

        # Create an outer PrettyTable
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        # Add simple attributes to the outer table
        for key, value in data['data'].items():
            if key not in ['educations', 'experiences']:
                outer_table.add_row([key, value])

        # Create an inner PrettyTable for educations if present
        if 'educations' in data['data']:
            inner_educations_table = PrettyTable()
            inner_educations_table.field_names = ["School", "Degree", "Date Range"]

            # Add educations to the inner table
            for education in data['data']['educations']:
                isEducations = True
                inner_educations_table.add_row(
                    [education.get('school', ''), education.get('degree', ''), education.get('date_range', '')])

            if isEducations:
                outer_table.add_row(["Educations", inner_educations_table.get_string()])

        # Create an inner PrettyTable for experiences if present
        if 'experiences' in data['data']:
            inner_experiences_table = PrettyTable()
            inner_experiences_table.field_names = ["Company", "Title", "Duration"]

            # Add experiences to the inner table
            for experience in data['data']['experiences']:
                inner_experiences_table.add_row([experience.get('company', ''), experience.get('title', ''),
                                                 experience.get('duration', '')])

            if isExpereinces:
                outer_table.add_row(["Experiences", inner_experiences_table.get_string()])

        return outer_table.get_string()

    @staticmethod
    def display_profiles_posts(json_data: str, result=""):
        data = json.loads(json_data)

        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        # Create a table for each post
        for post in data['data']:
            post_table = PrettyTable()
            post_table.field_names = ["Attribute", "Value"]

            for key, value in post.items():
                if isinstance(value, str) and len(value) > 50:
                    # Truncate long strings for better display
                    value = value[:50] + '...'

                post_table.add_row([key, value])

            result +="\nPost:\n"
            result+=post_table.get_string()
        return result