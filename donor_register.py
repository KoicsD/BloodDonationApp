__author__ = 'KoicsD'
from datetime import datetime
from datetime import timedelta
from random import randint
TestMethodsIndependently = False

# class Person as super?
# moving assistant functions to a separate module?
# __repr__?
# creating print functions for each fields and making .printdonor use these funs?
# set and get functions?
# parser and stringiser functions like datetime.strptime or .strmtime?


class Donor(object):
    # This class expresses a Blood Donor.
    # It contains a lot of methods handling user-input.
    # Initializer calls these methods to fill the object.
    #
    # You can set (initializer requests for):
    #   Name (First Name and Surname)
    #   Gender
    #   Date of Birth
    #   Unique Identifier
    #   Expiration Date of Unique ID
    #   Weight
    #   Blood Type
    #   Date of Last Donation
    #   E-mail Address
    #   Mobile Number
    #
    # And you can also generate a random integer
    # between 80 and 200 as a hemoglobin-level.
    #
    # Before starting, Initializer invokes a method,
    # which prints the donor-requirements and asks some questions to make sure:
    #   The new Donor has not donated blood for at least 90 days;
    #   The new Donor has not been sick for at least 30 days;
    #   The new Donor weights at least 50 kgs;
    #   The new Donor is at least 18 years old;
    #   The new Donor's Unique ID has not been expired.
    # The aim is simple: You do not have to fill the form
    # if you are surely unsuitable.
    #
    # After filling the form, Initializer invokes the method of
    # generating hemoglobin-level. The Donor is suitable only
    # if this number is at least 110.
    #
    # Of course there is a method to print the data stored in the object.
    #
    # Valid Formats:
    #   Date: YYYY.MM.DD
    #       Date of Birth must refer to at least 18 years ago
    #       Expiration Date of ID must be a future date
    #       Date of Last Donation must refer to at least 90 days ago
    #           or is "never"
    #   Weight: >= 50 integer
    #   Blood Type:
    #       "0+", "0-", "A+", "A-" etc.
    #       non case-sensitively
    #   Unique Identifier:
    #       either 6 digits and 2 letters
    #       or 6 letters and 2 digits
    #       no case-sensitivity (everything is converted to upper)
    #   E-mail Address:
    #       must contain exactly 1 occurance of character '@'
    #       must end with ".com" or ".hu"
    #       must contain at least one character:
    #           before '@'
    #           between "@" and ".com"/".hu"
    #   Mobile Number:
    #       must start with "06", "0036" or "+36"
    #       must continue with "20", "30" or "70"
    #       must contain 7 digits after predial
    #

    # Universal constants:
    hun_predials = ("06", "0036", "+36")
    mobile_predials = ("20", "30", "70")
    email_endings = (".com", ".hu")
    types_of_blood = ("0+", "0-", "A+", "A-", "B+", "B-", "AB+", "AB-")

    # assistant functions:
    @staticmethod
    def are_the_same(first, second):
        return first == second

    @staticmethod
    def first_true(fun, obj, lst):
        for index in range(len(lst)):
            if fun(obj, lst[index]):
                return index
        return -1

    @staticmethod
    def true_for_any(fun, obj, lst):
        for item in lst:
            if fun(obj, item):
                return True
        return False

    @staticmethod
    def listing(lst, prefix, delimiter, postfix):
        text = prefix
        for i in range(len(lst)):
            if i > 0:
                text += delimiter
            text += lst[i]
        text += postfix
        return text

    @staticmethod
    def print_mobile(str_number, to_print=False):
        ind = Donor.first_true(str.startswith, str_number, Donor.hun_predials)
        if ind >= 0:
            l_pred = len(Donor.hun_predials[ind])
            if len(str_number) == l_pred + 2 + 3 + 4:
                parsed = str_number[:l_pred] + " " + str_number[l_pred:l_pred+2] + " "
                parsed += str_number[l_pred+2:l_pred+2+3] + " " + str_number[l_pred+2+3:]
                if to_print:
                    print(parsed)
                return parsed
        if to_print:
            print(str_number)
        return str_number

    @staticmethod
    def errmsg(string="", to_print=True):
        msg = "Invalid Input"
        if string != "":
            msg += " " + string
        msg += "!"
        if to_print:
            print(msg)
        return msg

    # initializer:              # init              # init              # init              # init
    def __init__(self):

        # initial values before applying for user-input
        self.uinp_completed = False
        self.name = {"first": "", "sur": ""}
        self.weight = 0
        self.gender = 'n'
        self.date_of_birth = datetime(1, 1, 1).date()
        self.age = 0
        self.donated_ever = False
        self.last_donation = datetime(1, 1, 1).date()
        self.since_last_time = timedelta()
        self.unique_id = ""
        self.blood_type = "none"
        self.expiration_of_id = datetime(1, 1, 1).date()
        self.email_address = {"user": "", "server": ".none"}
        self.mobile_number = "+36000000000"
        self.hemoglobin = 0
        self.suitable = False

        # warning user and asking the most problematic questions
        if Donor.user_warning():
            return

        # applying for full user-input
        if self.input_name():
            return
        if self.input_gender():
            return
        if self.input_date_of_birth():
            return
        if self.input_unique_id():
            return
        if self.input_expiration_of_id():
            return
        if self.input_weight():
            return
        if self.input_blood_type():
            return
        if self.input_last_donation():
            return
        if self.input_email_address():
            return
        if self.input_mobile_number():
            return

        self.uinp_completed = True

        self.generate_hemoglobin()

    # pre-user-input method:
    @staticmethod
    def user_warning():                                         # warning user and asking the most problematic questions

        # printing donor requirements:
        print("A Suitable Donor:")
        print("\tHas not been to a Blood Donation for at least 3 months;")
        print("\tHas not been ill for at least one month;")
        print("\tWeights at least 50 kgs;")
        print("\tHas a hemoglobin level of at least 110;")
        print("\tIs at least 18 years old;")
        print("\tHas a valid unique identifier.")
        # starting input:
        uinp = ""
        luinp = ""
        while True:  # until input OK
            uinp = input("Has the new Donor been to a blood donation for less than 90 days? (y/n): ")
            luinp = uinp.lower()
            if luinp == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if luinp == 'y':
                print("The new Donor is not suitable.")
                return True  # input OK, donor surely not suitable
            elif luinp == 'n':
                break  # input OK, donor can be suitable
        while True:  # until input OK
            uinp = input("Has the new Donor been sick in the last 30 days? (y/n): ")
            luinp = uinp.lower()
            if luinp == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if luinp == 'y':
                print("The new Donor is not suitable.")
                return True  # input OK, donor surely not suitable
            elif luinp == 'n':
                break  # input OK, donor can be suitable
        while True:  # until input OK
            uinp = input("Does the new Donor weight at least 50 kgs? (y/n): ")
            luinp = uinp.lower()
            if luinp == "\quit":  # enabling user to quit
                print("Process aborted.")
                return True
            if luinp == 'y':
                break  # input OK, donor can be suitable
            elif luinp == 'n':
                print("The new Donor is not suitable.")
                return True  # input OK, donor surely not suitable
        while True:  # until input OK
            uinp = input("Is the new Donor at least 18 years old? (y/n): ")
            luinp = uinp.lower()
            if luinp == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if luinp == 'y':
                break  # input OK, donor can be suitable
            elif luinp == 'n':
                print("The new Donor is not suitable.")
                return True  # input OK, donor surely not suitable
        while True:  # until input OK
            uinp = input("Does the new Donor have a valid (not expired!) Unique Identifier? (y/n): ")
            luinp = uinp.lower()
            if luinp == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if luinp == 'y':
                print("We can fill the form.")
                print("You can stop at any time by typing '\quit'.")
                return False  # input OK, donor is suitable (unless hemoglobin-level turns out to be low)
            elif luinp == 'n':
                print("The new Donor is not suitable.")
                return True  # input OK, donor surely not suitable

    # user-input methods:
    def input_name(self):                                       # requesting for name
        first_name = ""
        surname = ""
        # requesting for First Name:
        while True:  # until input OK
            first_name = input("First Name: ")  # requesting
            if first_name.lower() == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if len(first_name) > 0 and "".join(first_name.split()).isalpha():  # testing
                break  # input OK
            else:
                print("It cannot be empty and can contain only letters and space.")
        # requesting for Surname:
        while True:  # until input OK
            surname = input("Surname:f ")  # requesting
            if first_name.lower() == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if len(surname) > 0 and "".join(surname.split()).isalpha():  # testing
                break  # input OK
            else:
                print("It cannot be empty and can contain only letters and space.")
        # saving:
        self.name["first"] = first_name
        self.name["sur"] = surname
        return False

    def input_weight(self):                                     # requesting for weight
        s_weight = ""
        i_weight = 0
        while True:
            s_weight = input("Weight[kg]: ")
            if s_weight.lower() == "\quit":  # enabling user to quit
                print("Process aborted.")
                return True
            try:
                i_weight = int(s_weight)
                if i_weight > 50:
                    break
                else:
                    print("Weight must be at least 50 kgs!")
            except ValueError:
                Donor.errmsg("for Integer")
        self.weight = i_weight
        return False

    def input_gender(self):                                     # requesting for gender
        r_gender = ""
        p_gender = 'n'
        while True:  # until input OK
            r_gender = input("Gender (m/f): ")  # requesting
            p_gender = r_gender.lower()
            if p_gender == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if p_gender == 'm' or p_gender == 'f':  # testing
                break  # input OK
            else:
                print("Invalid Gender!")
        self.gender = p_gender  # saving
        return False

    def input_date_of_birth(self):                              # requesting for date of birth
        s_date_of_birth = ""
        p_date_of_birth = datetime(1, 1, 1).date()
        age = 0
        while True:  # until User gives an appropriate input
            # firstly, input:
            s_date_of_birth = input("Date of Birth (yyyy.mm.dd): ")
            if s_date_of_birth == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            try:
                # secondly, parsing:
                p_date_of_birth = datetime.strptime(s_date_of_birth, "%Y.%m.%d").date()  # trynna convert str to date
                # thirdly, processing and checking validity:
                age = int((datetime.now().date() - p_date_of_birth).days // 365.25)
                if age >= 18:
                    break  # here breaks while, if input is appropriate
                else:
                    print("Age must be at least 18!")
            except ValueError:  # str to date conversion failed
                Donor.errmsg("for Date")
        # finally, saving:
        self.date_of_birth = p_date_of_birth
        self.age = age
        return False

    def input_last_donation(self):                              # requesting for date of last donation
        s_don_ever = ""
        s_last_donation = ""
        p_don_ever = ""
        p_last_donation = datetime(1, 1, 1).date()
        since_last_time = timedelta()
        # at first it's better to ask if he has ever been a donor
        while True:  # until input OK
            s_don_ever = input("Has the new Donor ever been a BloodDonor?: ")
            temp = s_don_ever.lower()
            if temp.lower() == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            if temp == 'y':
                p_don_ever = True
                break  # input OK
            elif temp == 'n':
                p_don_ever = False
                break  # input OK
        # and only if he has do we start requesting for date
        if p_don_ever:
            while True:  # until User gives an appropriate input
                # firstly, input:
                s_last_donation = input("Date of Last Donation (yyyy.mm.dd): ")
                temp = s_last_donation.lower()
                if temp == "\quit":  # enabling User to quit
                    print("Process aborted.")
                    return True
                elif temp == "\\never":  # enabling User to recognise, the new Donor has not been a donor yet
                    p_don_ever = False
                    break
                try:
                    # secondly, parsing:
                    p_last_donation = datetime.strptime(s_last_donation, "%Y.%m.%d").date()  # trynna conv str to date
                    # thirdly, processing and checking validity:
                    since_last_time = (datetime.now().date() - p_last_donation)
                    if since_last_time.days >= 30:
                        break  # here breaks while if input is appropriate
                    else:
                        print("Last Donation must be at least 30 days ago!")
                except ValueError:  # str to date conversion failed
                    Donor.errmsg("for Date")
            # finally, saving:
            self.last_donation = p_last_donation
            self.since_last_time = since_last_time
        self.donated_ever = p_don_ever
        return False

    def input_unique_id(self):                                  # requesting for unique id
        r_unique_id = ""
        u_unique_id = ""
        while True:  # until input OK
            r_unique_id = input("Unique Identifier: ")  # requesting
            u_unique_id = r_unique_id.upper()
            if u_unique_id == "\QUIT":  # enabling User to quit
                print("Process aborted.")
                return True
            msg = "Valid"  # checking validity
            if len(u_unique_id) != 8:
                msg = "ID must contain 8 characters!"
            elif u_unique_id[0].isnumeric():
                if not u_unique_id[0:6].isnumeric() or not u_unique_id[6:8].isalpha():
                    msg = "ID must consist of either 6 numbers and 2 letters or 6 letters and 2 numbers!"
            elif u_unique_id[0].isalpha():
                if not u_unique_id[0:6].isalpha() or not u_unique_id[6:8].isnumeric():
                    msg = "ID must consist of either 6 numbers and 2 letters or 6 letters and 2 numbers!"
            if msg == "Valid":
                break  # input OK
            else:
                print(msg)
        self.unique_id = u_unique_id  # saving
        return False

    def input_blood_type(self):                                 # requesting for blood type
        r_blood_type = ""
        u_blood_type = "none"
        while True:  # until input OK
            print(Donor.listing(Donor.types_of_blood, "Possible types of blood: ", ", ", ""))
            r_blood_type = input("Type of Blood: ")
            u_blood_type = r_blood_type.upper()
            if u_blood_type == "\QUIT":  # enabling User to quit
                print("Process aborted.")
                return True
            if u_blood_type in Donor.types_of_blood:
                break  # input OK
            else:
                print("Invalid Type of Blood!")
        self.blood_type = u_blood_type  # saving
        return False

    def input_expiration_of_id(self):                           # requesting for expiration of id
        s_expiration_of_id = ""
        p_expiration_of_id = datetime(1, 1, 1).date()
        while True:  # until User gives an appropriate input
            # firstly, input:
            s_expiration_of_id = input("Expiration Date of Unique Identifier (YYYY.MM.DD): ")
            if s_expiration_of_id == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            try:
                # secondly, parsing:
                p_expiration_of_id = datetime.strptime(s_expiration_of_id, "%Y.%m.%d").date()  # trynna conv str to date
                # thirdly, processing and checking validity:
                diff = p_expiration_of_id - datetime.now().date()
                if diff.days > 0:
                    break  # here breaks while if input is appropriate
                else:
                    print("Unique Identifier must be valid!")
            except ValueError:  # str to date conversion failed
                Donor.errmsg("for Date")
        # finally, saving:
        self.expiration_of_id = p_expiration_of_id
        return False

    def input_email_address(self):                              # requesting for email address
        s_email = ""
        p_email = ["", ""]
        while True:  # until input OK
            s_email = input("E-mail Address: ")
            if s_email == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            p_email = s_email.split('@')
            msg = "Valid"  # checking validity
            if len(p_email) != 2:
                msg = "E-mail Address must contain exactly 1 occourance of character '@'!"
            elif p_email[0] == "":
                msg = "E-mail Address must contain at least one character before '@'!"
            elif not Donor.true_for_any(str.endswith, p_email[1], Donor.email_endings):
                msg = Donor.listing(Donor.email_endings, "E-mail Address must end with \"", "\" or \"", "\"!")
            elif Donor.true_for_any(Donor.are_the_same, p_email[1], Donor.email_endings):
                msg = Donor.listing(Donor.email_endings,
                                    "E-mail Address must contain at least one character between \"@\" and \"",
                                    "\"/\"", "\"!")
            if msg == "Valid":
                break  # input OK
            else:
                print(msg)
        # saving:
        self.email_address["user"] = p_email[0]
        self.email_address["server"] = p_email[1]
        return False

    def input_mobile_number(self):                              # requesting for mobile number
        mobile_number = ""
        while True:  # until input OK
            mobile_number = input("Mobile Number: ")  # requesting
            if mobile_number == "\quit":  # enabling User to quit
                print("Process aborted.")
                return True
            msg = "Valid"  # checking validity
            l_pred = 0
            ind = Donor.first_true(str.startswith, mobile_number, Donor.hun_predials)
            if ind >= 0:
                l_pred = len(Donor.hun_predials[ind])
            elif mobile_number == "":
                msg = "Mobile Number cannot be empty!"
            else:
                msg = Donor.listing(Donor.hun_predials, "You must use the predial \"", "\" or \"",
                                    "\" to dial a hungarian number!")
            if l_pred > 0:
                if not Donor.true_for_any(str.startswith, mobile_number[l_pred:], Donor.mobile_predials):
                    msg = Donor.listing(Donor.mobile_predials, "You must dial \"", "\" or \"",
                                        "after country predial in case of a Mobile Number!")
                elif len(mobile_number) != l_pred + 2 + 7:
                    msg = "Mobile Number must have a length of 7 digits after predials!"
            if msg == "Valid":
                break  # input OK
            else:
                print(msg)
        self.mobile_number = mobile_number  # saving
        return False

    # post-user-input methods:
    def generate_hemoglobin(self):                              # generating hemoglobin-level
        self.hemoglobin = randint(80, 200)
        self.refresh_suitable()

    def refresh_suitable(self):                                 # refreshing suitability-bit after hem-lev generation
        if self.uinp_completed and self.hemoglobin >= 110:
            self.suitable = True
        else:
            self.suitable = False

    def print_donor(self, even_if_invalid=False):                                      # printing
        if not self.uinp_completed:
            print("Invalid Donor Object!")
            if not even_if_invalid:
                return
        print("Name: " + self.name["first"] + ", " + self.name["sur"])
        if self.gender == 'm':
            print("Gender: male")
        elif self.gender == 'f':
            print("Gender: female")
        else:
            print("Gender: <invalid>")
        print("Date of Birth: " + self.date_of_birth.strftime("%Y.%m.%d") + " - " + str(self.age) + " years old")
        print("Unique Identifier: " + self.unique_id)
        print("Expiration Date of Unique Identifier: " + self.expiration_of_id.strftime("%Y.%m.%d"))
        print("Weight: %d[kg]" % self.weight)
        print("Blood Type: " + self.blood_type)
        print("Date of Last Donation: ", end='')
        if self.donated_ever:
            print(self.last_donation.strftime("%Y.%m.%d") + " - " + str(self.since_last_time.days) + " days ago")
        else:
            print("<never>")
            if even_if_invalid:
                print("\t(Data in Donor Object: " + self.last_donation.strftime("%Y.%m.%d") + " - " +
                      str(self.since_last_time.days) + " days ago)")
        print("E-mail Address: " + self.email_address["user"] + "@" + self.email_address["server"])
        print("Mobile Number: " + Donor.print_mobile(self.mobile_number))
        print("Hemoglobin Level: %d" % self.hemoglobin)
        if self.suitable:
            print("Suitable for Donation: TRUE")
        else:
            print("Suitable for Donation: FALSE")


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
if __name__ == "__main__":  # test-code

    # fulfilling the task in 2 lines:
    my_donor = Donor()  # 1
    print()
    print('-' * 3)
    print()
    my_donor.print_donor(True)  # 2

    # code for testing class in details:
    if TestMethodsIndependently:
        print()
        print('-' * 9)
        print()
        from my_class_test import MethodToTest
        methods_to_test = (MethodToTest("__init__", Donor.__init__, False),
                           MethodToTest("user_warning", Donor.user_warning, True),
                           MethodToTest("input_name", Donor.input_name, False),
                           MethodToTest("input_weight", Donor.input_weight, False),
                           MethodToTest("input_gender", Donor.input_gender, False),
                           MethodToTest("input_last_donation", Donor.input_last_donation, False),
                           MethodToTest("input_unique_id", Donor.input_unique_id, False),
                           MethodToTest("input_blood_type", Donor.input_blood_type, False),
                           MethodToTest("input_expiration_of_id", Donor.input_expiration_of_id, False),
                           MethodToTest("input_email_address", Donor.input_email_address, False),
                           MethodToTest("input_mobile_number", Donor.input_mobile_number, False),
                           MethodToTest("generate_hemoglobin", Donor.generate_hemoglobin, False),
                           MethodToTest("refresh_suitable", Donor.refresh_suitable, False),
                           MethodToTest("print_donor", Donor.print_donor, False))

        while True:
            print("Commands:")
            print("\tExit: .")
            print("\tMethods:")
            for method in methods_to_test:
                print("\t\t" + method.name)
            print()
            uinp = input("Donor.")
            if uinp == ".":
                break
            elif uinp not in [method.name for method in methods_to_test]:
                print()
                print("Method not in list!")
            else:
                print()
                print('-' * 3)
                print()
                index = [method.name for method in methods_to_test].index(uinp)
                methods_to_test[index].invoke(my_donor)
            print()
            print('-' * 3)
            print()
