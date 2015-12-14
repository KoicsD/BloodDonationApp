import uinp, menu
import event_ui, donor_ui
import data_handler
import screeen_handler

# uinp.input_fcn = screeen_handler.menu_input  # connecting usr_inp to screen_handler
# menu.print_fcn = screeen_handler.menu_print  # connecting menu print to screen_handler
# menu.cls_fcn = screeen_handler.menu_clear  # connecting menu clear to screen_handler


class Adder:
    @staticmethod
    def add_new_event():
        pass

    @staticmethod
    def add_new_donor():
        pass


class Exchanger:
    @staticmethod
    def modify_event_by_id():
        pass

    @staticmethod
    def modify_donor_by_id():
        pass

    @staticmethod
    def modify_any_by_id():
        pass


class Remover:
    @staticmethod
    def remove_event_by_id():
        pass

    @staticmethod
    def remove_donor_by_id():
        pass

    @staticmethod
    def remove_any_by_id():
        pass


class Lister:
    @staticmethod
    def list_events():
        pass

    @staticmethod
    def list_donors():
        pass

    @staticmethod
    def search_in_events():
        pass

    @staticmethod
    def search_in_donors():
        pass


def startup():  # module initializer
    data_handler.startup()
    pass


def shutdown():
    pass
