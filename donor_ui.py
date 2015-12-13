from uinp import *
import donor_reg
import screeen_handler


class UIDonor(donor_reg.Donor):  # extending Donor class with user-input functions
    @classmethod
    def from_Donor(cls, donor):  # fast-creating object from normal Donor object
        pass

    def to_Donor(self):  # fast-transforming to normal Donor object
        pass

    def uinp_something(self):
        pass

    @classmethod
    def from_user(cls):  # creating object by getting all data from user
        pass
