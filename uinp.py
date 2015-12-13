# general user-input function and its exception class


input_fcn = input  # change this if u wanna use your own input-function
err_print_fcn = print  # change this if u wanna use your own function to print error message


class UserInterrupt(Exception):
    pass


def usr_inp():
    pass  # while True
