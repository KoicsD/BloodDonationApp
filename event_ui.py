from time import sleep
from uinp import *
import event_reg


class UIEvent(event_reg.Event):  # extending Event class with user-input functions
    @classmethod
    def from_Event(cls, event: event_reg.Event):  # fast-creating object from normal Event object
        pass

    def to_Event(self):  # fast-transforming object to normal Event object
        pass

    def uinp_date(self):
        pass

    def uinp_start_time(self):
        pass

    def uinp_end_time(self):
        pass

    def uinp_zip_code(self):
        pass

    def uinp_city(self):
        pass

    def uinp_address(self):
        pass

    def uinp_n_beds(self):
        pass

    def uinp_planned_n_dons(self):
        pass

    def uinp_final_n_dons(self):
        pass

    @classmethod
    def from_user(cls):  # creating object by getting all data from user
        pass

