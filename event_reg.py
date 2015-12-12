from reg_err import *
from datetime import datetime, date, time, timedelta


class City:  # class with string-checker function as __init__
    def __init__(self, city: str):
        self.city = city  # validating necessary!

    # def __str__(self):
    #     pass


class EventData:  # data structure and basic validator logic
    # def __init__(self, data: dict):  # creating empty object or creating object from dictionary
    #     pass

    def set_date(self, date_of_event: date):
        pass

    def set_start_time(self, start_time: time):
        pass

    def set_end_time(self, end_time: time):
        pass

    def set_zip_code(self, zip_code: str):
        pass

    def set_city(self, city: City):
        pass

    def set_address(self, address: str):
        pass

    def set_n_beds(self, n_beds: int):
        pass

    def set_planned_n_dons(self, planned_n_dons: int):
        pass

    def set_final_n_dons(self, final_n_dons: int):
        pass

    def get_dict(self):  # transforming object to dictionary
        pass

    # def __str__(self):  # transforming object to string (for printing object on screen)
    #     pass


class Event(EventData):  # string-parser functions
    def strp_date(self, date_of_event: date):
        pass

    def strp_start_time(self, start_time: time):
        pass

    def strp_end_time(self, end_time: time):
        pass

    def strp_zip_code(self, zip_code: str):
        pass

    def strp_city(self, city: City):
        pass

    def strp_address(self, address: str):
        pass

    def strp_n_beds(self, n_beds: int):
        pass

    def strp_planned_n_dons(self, planned_n_dons: int):
        pass

    def strp_final_n_dons(self, final_n_dons: int):
        pass

    @classmethod
    def from_str_dict(cls, str_dict: dict):  # creating from dictionary of strings
        pass

    def to_str_dict(self):  # transforming to dictionary of strings
        pass
