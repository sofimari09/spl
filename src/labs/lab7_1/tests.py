import unittest

from src.labs.lab7_1.service.services import UserService


class UserServiceCalculator(unittest.TestCase):
    def test_get_profile_posts(self):
        with self.assertRaises(ValueError):
            #checking according to the correct format of URL
            UserService.get_profiles_posts("www.linkedin.com/in/andrei-alexandru-ungureanu-8a0a3a1a5/")
            UserService.get_profiles_posts("https://www.nonexistent.com")
            #checking according to the incorrect input data
            UserService.get_profiles_posts(None)
            UserService.get_profiles_posts(13)
            #checking that the profile doesn't exist
            UserService().get_profiles_posts("https://www.linkedin.com/in/andrei-alexandru-ungureanu-0000000000000/")

    def test_get_personal_profile(self):
        with self.assertRaises(ValueError):
            # checking according to the correct format of URL
            UserService.get_profiles_posts("www.linkedin.com/in/andrei-alexandru-ungureanu-8a0a3a1a5/")
            UserService.get_profiles_posts("https://www.nonexistent.com")
            # checking according to the incorrect input data
            UserService.get_profiles_posts(None)
            UserService.get_profiles_posts(13)
            # checking if the profile exists
        #checking if the profile exists and the result is not None
        self.assertIsNone(UserService().get_personal_profile("https://www.linkedin.com/in/andrei-alexandru-ungureanu-8a0a3a1a5/"))




