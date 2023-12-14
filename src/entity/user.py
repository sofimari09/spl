"""
User Entity Module

This module defines the `User` class representing a user with various attributes.

Attributes:
- index (int): The index of the user.
- user_id (str): The unique identifier for the user.
- first_name (str): The first name of the user.
- last_name (str): The last name of the user.
- sex (str): The gender of the user.
- email (str): The email address of the user.
- phone (str): The phone number of the user.
- date_of_birth (datetime.date): The date of birth of the user, parsed from
the specified format ("%Y-%m-%d").
- job_title (str): The job title of the user.

Methods:
- __init__.py(self, data): Initializes a User object with the given data.
- __str__(self): Returns a string representation of the User object.

Example:
```python
data = [1, '12345', 'John', 'Doe', 'Male', 'john.doe@example.com',
        '123-456-7890', '1990-01-01', 'Engineer']
user = User(data)
print(user)
# Output: 1 12345 John Doe Male john.doe@example.com 123-456-7890 1990-01-01 Engineer
"""
from shared.data_processor import DateProcessor


class User:
    """
    Represents a user with various attributes.

    Attributes:
    - index (int): The index of the user.
    - user_id (str): The unique identifier for the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    - sex (str): The gender of the user.
    - email (str): The email address of the user.
    - phone (str): The phone number of the user.
    - date_of_birth (datetime.date): The date of birth of
    the user, parsed from the specified format ("%Y-%m-%d").
    - job_title (str): The job title of the user.

    Methods:
    - __init__.py(self, data): Initializes a User object with the given data.
    - __str__(self): Returns a string representation of the User object.
    """

    def __init__(self, data):
        """
        Initialize User object with the given data.

        Parameters:
        - data (list): A list containing values for each attribute in the specified order.
        """
        self.__index = data[0]
        self.__user_id = data[1]
        self.__first_name = data[2]
        self.__last_name = data[3]
        self.__sex = data[4]
        self.__email = data[5]
        self.__phone = data[6]
        # parse the eighth value of the data list as a date in the format "%Y-%m-%d"
        # and assign it to the date_of_birth attribute
        self._date_of_birth = DateProcessor.parse_dateformat(data[7], "%Y-%m-%d").date()
        self.__job_title = data[8]

    @property
    def index(self):
        """
        Return the index of the user.

        Returns:
        - int: The index of the user.
        """
        return self.__index

    @property
    def user_id(self):
        """
        Return the unique identifier for the user.

        Returns:
        - str: The unique identifier for the user.
        """
        return self.__user_id

    @property
    def first_name(self):
        """
        Return the first name of the user.

        Returns:
        - str: The first name of the user.
        """
        return self.__first_name

    @property
    def last_name(self):
        """
        Return the last name of the user.

        Returns:
        - str: The last name of the user.
        """
        return self.__last_name

    @property
    def sex(self):
        """
        Return the gender of the user.

        Returns:
        - str: The gender of the user.
        """
        return self.__sex

    @property
    def email(self):
        """
        Return the email address of the user.

        Returns:
        - str: The email address of the user.
        """
        return self.__email

    @property
    def phone(self):
        """
        Return the phone number of the user.

        Returns:
        - str: The phone number of the user.
        """
        return self.__phone

    @property
    def date_of_birth(self):
        """
        Return the date of birth of the user.

        Returns:
        - datetime.date: The date of birth of the user.
        """
        return self._date_of_birth

    @property
    def job_title(self):
        """
        Return the job title of the user.

        Returns:
        - str: The job title of the user.
        """
        return self.__job_title

    def __str__(self):
        """
        Return a string representation of the User object.

        Returns:
        - str: A string containing user information.
        """
        return (f"{self.__index} {self.__user_id} {self.__first_name} {self.__last_name} "
                f"{self.__sex} "
                f"{self.__email} {self.__phone} {self.date_of_birth} {self.__job_title}")
