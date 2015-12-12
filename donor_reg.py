from reg_err import *
from datetime import datetime, date, time, timedelta


class Something:  # classes with string-checker function as __init__
    def __init__(self, content: str):
        self.content = content  # validation necessary

    # def __str__(self):
    #     pass


class DonorData:  # data structure and basic validator logic
    # def __init__(self, data: dict):  # creating empty object or creating object from dictionary
    #     pass

    def set_something(self, something: Something):
        pass

    def get_dict(self):  # transforming object to dictionary
        pass

    # def __str__(self):  # transforming object to string (for printing object to screen)
    #     pass


class Donor(DonorData):  # string-parser functions
    def strp_something(self, something: str):
        # self.something = Something(something)
        pass

    @classmethod
    def from_str_dict(cls, str_dict: str):  # creating from dictionary of strings
        pass

    def to_str_dict(self):  # transforming to dictionary of strings
        pass
