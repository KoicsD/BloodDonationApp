import csv
import event_reg
import donor_reg


default_event_file_path = "DATA/Events.csv"
default_donor_file_path = "DATA/Donors.csv"


donors_in_db = {}
events_in_db = {}


class FileHandler:  # functions to handle csv files
    event_file_path = ""
    donor_file_path = ""

    @staticmethod
    def load_events():
        pass

    @staticmethod
    def load_donors():
        pass

    @staticmethod
    def store_events():
        pass

    @staticmethod
    def store_donors():
        pass


class Modifier:  # functions to manipulate data in database
    @staticmethod
    def add_event(event: event_reg.Event):
        pass

    @staticmethod
    def add_donor(donor: donor_reg.Donor):
        pass

    @staticmethod
    def exch_event(id: int, new_ev: event_reg.Event):
        pass

    @staticmethod
    def exch_donor(id: str, new_don: donor_reg.Donor):
        pass

    @staticmethod
    def rm_event(id: int):
        pass

    @staticmethod
    def rm_donor(id: str):
        pass


class Querier:  # functions to query data from database
    @staticmethod
    def ls_events(field_to_ord="date_of_event", desc=False):
        pass

    @staticmethod
    def ls_donors(field_to_ord="name", desc=False):
        pass

    @staticmethod
    def search_in_evs(search_key, field_to_ord="date_of_event", desc=False):
        pass

    @staticmethod
    def search_in_dons(search_key, field_to_ord="name", desc=False):
        pass


def startup(event_file_path=default_event_file_path, donor_file_path=default_donor_file_path):  # module-initializer
    pass


def shutdown():
    pass
