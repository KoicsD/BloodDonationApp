__author__ = 'KoicsD'
import MyAssistants as MAs
from datetime import datetime
from datetime import timedelta
TestMethodsIndependently = False

# making it contain a list of Donors?
# using class Address for city, address and zipcode?
# moving assistant functions to a separate module?                                          Done.
# __repr__?
# creating print functions for each fields and making .printdonation use these funs?
# set and get functions?
# parser and stringiser functions like datetime.strptime or .strftime?


def errmsg(string="", to_print=True):
    msg = "Invalid Input"
    if string != "":
        msg += " " + string
    msg += "!"
    if to_print:
        print(msg)
    return msg


class Donation(object):
    # This class expresses the event of blood donation.
    # It contains a lot of methods handling user input.
    # Initializer calls these methods to fill the object.
    #
    # You can set (initializer requests for):
    #   Date of Donation
    #   Starting Time
    #   Finishing Time
    #   Zip Code
    #   City (from a given list)
    #   Address (Street Name and House Number)
    #   Number of Beds Available
    #   Planned Number of Donors
    #
    # Independently from the calling order
    # input methods make sure if:
    #   User used the correct format:
    #       Dates: YYY.MM.DD
    #       Times: HH:MM
    #       Zip Code: 4 digits, not beginning with 0
    #       City: One of the cities in the built-in list (not case-sensitively)
    #       Street Name: Maximum 25 characters, contains only letters and spaces
    #   [Date] is not on weekday and is not in 10 days
    #   [Duration] is greater than [Time of one Donation]
    #       (or at least greater than zero)
    #   [Planned Number of Donors] does not exceed the limit given by the formula:
    #       [Duration] - [Time of one Preparation] / ([Number of Beds] * [Time of one Donation])
    #
    # This class has an evaluating method, which:
    #   requests for the Number of Successful Donations
    #   and evaluates how efficient the event was.
    #
    # And also there is a printer function to make the event and its attributes visible on screen.
    #
    # Built-in Constants:
    #   [Cities Available]: Miskolc, Szerencs, Kazincbarcika, Sarospatak
    #   [Preparation Time]: 30 min
    #   [Time of one Donation]: 30 min
    #

    # universal constants:
    cities_available = ("Miskolc", "Szerencs", "Kazincbarcika", "Sarospatak")
    preparation_time = 30
    donation_time = 30

    # assistant function:
    @staticmethod
    def max_don_num(t_duration, n_beds):
        return t_duration - Donation.preparation_time / (n_beds * Donation.donation_time)

    # initializer:
    def __init__(self):

        # booleans signing nothing initialized yet:
        self.initialized = False
        self.date_set = False
        self.start_time_set = False
        self.end_time_set = False
        self.beds_available_set = False

        # initializing member variables with default values:
        self.date = datetime(1, 1, 1).date()
        self.start_time = datetime(1, 1, 1).time()
        self.end_time = datetime(1, 1, 1).time()
        self.duration = 0
        self.zip_code = "0000"
        self.city = "None"
        self.address = {"street": "", "number": 0}
        self.beds_available = 0
        self.max_number_of_donors = 0
        self.number_of_donors = 0  # 0 can refer to "not set" without troubles, no need of using boolean

        self.evaluated = False
        self.number_of_success = 0
        self.ratio_of_success = 0
        self.conclusion = ""

        # calling user-input functions
        #   (for testing try to scramble the order):
        self.input_date()
        self.input_start_time()
        self.input_end_time()
        self.input_zip_code()
        self.input_city()
        self.input_address()
        self.input_beds_available()
        self.input_number_of_donors()

        # finally signing initialization ready:
        self.initialized = True

    # input methods:
    def input_date(self):                                                   # requesting for Date
        date = ""
        p_date = datetime(1, 1, 1).date()
        while True:  # until User gives an appropriate input
            # firstly, input:
            date = input("Date of Donation (YYYY.MM.DD): ")
            # then testing:
            try:
                p_date = datetime.strptime(date, "%Y.%m.%d").date()  # trynna convert str to date
                weekday = p_date.isoweekday()
                days_till_date = (p_date - datetime.now().date()).days
                if weekday <= 5 and days_till_date >= 10:
                    break  # here breaks while if input is OK
                else:
                    print("Date in 10 days or on weekday or expired!")
            except ValueError:  # str to date conversion failed
                errmsg("for Date")
        # finally, saving modifications:
        self.date = p_date
        self.date_set = True

    def input_start_time(self):                                             # requesting for StartTime
        time = ""
        p_time = datetime(1, 1, 1).time()
        duration = 0
        max_number_of_donors = 0
        while True:  # until User gives an appropriate input
            # firstly, input:
            time = input("Start Time: (HH:MM): ")
            # then testing:
            try:
                p_time = datetime.strptime(time, "%H:%M").time()  # trynna convert str to time
                msg = "Valid"  # checking validity
                if self.end_time_set:  # if we know the EndTime, we can check Duration
                    end_datetime = datetime.combine(datetime.now().date(), self.end_time)
                    start_datetime = datetime.combine(datetime.now().date(), p_time)
                    duration = int((end_datetime - start_datetime).total_seconds() // 60)
                    if duration < 0:
                        msg = "Negative Duration!"
                    elif duration < Donation.donation_time:
                        msg = "Duration < Time of one Donation!"
                    elif self.beds_available_set:  # if we know even the Number of Beds, we can use the formula
                        max_number_of_donors = Donation.max_don_num(duration, self.beds_available)
                        if max_number_of_donors <= 0:
                            msg = "Maximum Number of Donors <= 0!"
                        elif self.number_of_donors > max_number_of_donors:
                            msg = "Planned Number of Donors > Maximum Number of Donors!"
                if msg == "Valid":
                    break  # here breaks while if input is OK
                else:
                    print(msg)
            except ValueError:  # str to time conversion failed
                errmsg("for Time")
        # finally, saving:
        self.start_time = p_time
        if self.end_time_set:
            self.duration = duration
            if self.beds_available_set:
                self.max_number_of_donors = max_number_of_donors
        self.start_time_set = True  # signing StartTime set

    def input_end_time(self):                                               # requesting for EndTime
        time = ""
        p_time = datetime(1, 1, 1).time()
        duration = 0
        max_number_of_donors = 0
        while True:  # until User gives an appropriate input
            # firstly, input>
            time = input("End Time: (HH:MM): ")
            # then testing:
            try:
                p_time = datetime.strptime(time, "%H:%M").time()  # trynna convert str to time
                msg = "Valid"  # checking validity
                if self.start_time_set:  # if we know the StartTime, we can check Duration
                    start_datetime = datetime.combine(datetime.now().date(), self.start_time)
                    end_datetime = datetime.combine(datetime.now().date(), p_time)
                    duration = int((end_datetime - start_datetime).total_seconds() // 60)
                    if duration < 0:
                        msg = "Negative Duration!"
                    elif duration < Donation.donation_time:
                        msg = "Duration < Time of one Donation!"
                    elif self.beds_available_set:  # if we know even the Number of Beds, we can use the formula
                        max_number_of_donors = Donation.max_don_num(duration, self.beds_available)
                        if max_number_of_donors <= 0:
                            msg = "Max Number of Donors <= 0!"
                        elif self.number_of_donors > max_number_of_donors:
                            msg = "Planned Number of Donors > Maximum Number of Donors!"
                if msg == "Valid":
                    break  # here breaks while if input is appropriate
                else:
                    print(msg)
            except ValueError:  # str to time conversion failed
                errmsg("for Time")
        # finally, saving:
        self.end_time = p_time
        if self.start_time_set:
            self.duration = duration
            if self.beds_available_set:
                self.max_number_of_donors = max_number_of_donors
        self.end_time_set = True  # signing EndTime set

    def input_zip_code(self):                                               # requesting for Zip Code
        zip_code = ""
        while True:  # until input OK
            zip_code = input("Zip Code: ")  # requesting
            if len(zip_code) == 4 and not zip_code.startswith("0"):  # testing
                break  # input OK
            else:
                errmsg()
        self.zip_code = zip_code  # saving

    def input_city(self):                                                   # requesting  for City
        city = ""
        p_city = "none"
        while True:  # until User gives an appropriate input
            # firstly, printing the List of Cities Available:
            print(MAs.listing(Donation.cities_available, "Cities Available: ", ", ", ""))
            # secondly, input:
            city = input("City: ")
            # then testing:
            p_city = ""
            for i in range(len(city)):  # let 1st letter be capital
                if i == 0:
                    p_city += city[i].upper()
                else:
                    p_city += city[i].lower()
            if p_city in self.cities_available:  # is it in the list?
                break  # here breaks while if input is OK
            else:
                print("City not in the List!")
        # finally, saving:
        self.city = p_city

    def input_address(self):                                                # requesting for Address
        street = ""
        number = 0
        p_street = ""
        p_number = 0
        # requesting for Street Name:
        while True:  # until input is OK
            street = input("Street Name: ")  # input
            p_street = street
            length = len(p_street)
            if 0 < length <= 25 and "".join(p_street.split(" ")).isalpha():  # checking
                break  # input is OK
            else:
                errmsg()
        # requesting for House Number
        while True:  # until input is OK
            number = input("House Number: ")  # input
            try:
                p_number = int(number)  # converting str to int
                if p_number > 0:  # checking
                    break  # input OK
                else:
                    print("House Number must be positive!")
            except ValueError:  # str to int conversion failed
                errmsg("for Integer")
        self.address["street"] = p_street
        self.address["number"] = p_number

    def input_beds_available(self):                                         # requesting for Number of Beds
        beds_available = ""
        p_beds_available = 0
        max_number_of_donors = 0
        while True:  # until User gives an appropriate input
            # first, input:
            beds_available = input("Number of Beds Available: ")
            # then testing:
            try:
                p_beds_available = int(beds_available)  # trynna convert str to int
                msg = "Valid"  # checking validity
                if p_beds_available <= 0:
                    msg = "Number of Beds Available must be Positive!"
                elif self.start_time_set and self.end_time_set:  # if we know the duration, we can use the formula
                    max_number_of_donors = Donation.max_don_num(self.duration, p_beds_available)
                    if max_number_of_donors <= 0:
                        msg = "Maximum Number of Donors <= 0!"
                    elif self.number_of_donors > max_number_of_donors:
                        msg = "Planned Number of Donors > Maximum Number of Donors!"
                if msg == "Valid":
                    break  # here breaks while if input is appropriate
                else:
                    print(msg)
            except ValueError:  # str to int conversion failed
                errmsg("for Integer")
        # finally, saving:
        self.beds_available = p_beds_available
        if self.start_time_set and self.end_time_set:
            self.max_number_of_donors = max_number_of_donors
        self.beds_available_set = True  # signing Number of Beds set

    def input_number_of_donors(self):                                       # requesting for Planned Number of Donors
        number_of_donors = ""
        p_number_of_donors = 0
        while True:  # until user gives an appropriate input
            # firstly, input:
            number_of_donors = input("Planned Number of Donors: ")
            # then testing:
            try:
                p_number_of_donors = int(number_of_donors)  # trynna convert str to int
                msg = "Valid"  # checking validity
                if p_number_of_donors <= 0:
                    msg = "Planned Number of Donors must be Positive!"
                elif p_number_of_donors > self.max_number_of_donors:
                    msg = "Planned Number of Donors > Maximum Number of Donors!"
                if msg == "Valid":
                    break  # here breaks while if input is appropriate
                else:
                    print(msg)
            except ValueError:  # str to int conversion failed
                errmsg("for Integer")
        # finally, saving:
        self.number_of_donors = p_number_of_donors

    # evaluating function:
    def evaluate_donation(self):

        # firstly, checking date and time, and initialization:
        msg = "Valid"
        if not self.initialized:
            msg = "Object Not Initialized Yet!"
        elif (datetime.now() - datetime.combine(self.date, self.start_time)).days < 0:
            msg = "Donation Not Begun Yet!"
        elif (datetime.now() - datetime.combine(self.date, self.end_time)).days < 0:
            msg = "Donation Not Finished Yet!"
        if msg != "Valid":
            print(msg)
            return

        # if everything is OK, requesting for Number of Successful Donation:
        p_number_of_success = 0
        while True:  # until input is OK
            number_of_success = input("Number of Successful Donation: ")
            try:
                p_number_of_success = int(number_of_success)  # trynna convert
                if p_number_of_success < 0:  # checking validity
                    print("Number of Successful Donation must not be Negative!")
                else:
                    break  # input is OK
            except ValueError:  # conversion failed
                errmsg("for Integer")

        # then processing and printing:
        ratio_of_success = int(100 * p_number_of_success / self.number_of_donors)
        print("This is %d%% of the Planned Number of Donors." % ratio_of_success)
        conclusion = ""
        if ratio_of_success < 20:
            conclusion = "UNSUCCESSFUL"
        elif 20 <= ratio_of_success < 75:
            conclusion = "NORMAL"
        elif 75 <= ratio_of_success < 110:
            conclusion = "SUCCESSFUL"
        elif 75 <= ratio_of_success:
            conclusion = "OUTSTANDING"
        print("This Donation was " + conclusion + ".")

        # finally, saving:
        self.number_of_success = p_number_of_success
        self.ratio_of_success = ratio_of_success
        self.conclusion = conclusion
        self.evaluated = True  # signing evaluation has happened

    # printer function:
    def print_donation(self):
        print("Date of Donation: " + self.date.strftime("%Y.%m.%d"))
        print("Start Time: " + self.start_time.strftime("%H:%M"))
        print("End Time: " + self.end_time.strftime("%H:%M"))
        print("Zip Code: " + self.zip_code)
        print("City: " + self.city)
        print("Street Name: " + self.address["street"])
        print("House Number: %d" % self.address["number"])
        print("Number of Beds Available: %d" % self.beds_available)
        print("Planned Number of Donors: %d" % self.number_of_donors)
        if self.evaluated:  # only if evaluation has already happened
            print("Number of Successful Donations: %d" % self.number_of_success)
            print("Ratio of Successful Donations and Planned Donors: %d%%" % self.ratio_of_success)
            print("Conclusion: " + self.conclusion)


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
if __name__ == "__main__":  # test-code

    # Let's fulfill the task in 5 lines:
    # Construct, print, evaluate, print
    our_donation = Donation()  # 1
    print("-" * 30)
    our_donation.print_donation()  # 2
    print("-" * 30)
    our_donation.date = (datetime.now() - timedelta(days=1)).date()         # 3: we need to cheat a bit
    our_donation.evaluate_donation()  # 4
    print("-" * 30)
    our_donation.print_donation()  # 5

    # code for testing class in details:
    if TestMethodsIndependently:
        print()
        print('-' * 9)
        print()
        from MyClassTest import MethodToTest
        methods_to_test = (MethodToTest("__init__", Donation.__init__, False),
                           MethodToTest("input_date", Donation.input_date, False),
                           MethodToTest("input_start_time", Donation.input_start_time, False),
                           MethodToTest("input_end_time", Donation.input_end_time, False),
                           MethodToTest("input_zip_code", Donation.input_zip_code, False),
                           MethodToTest("input_city", Donation.input_city, False),
                           MethodToTest("input_address", Donation.input_address, False),
                           MethodToTest("input_beds_available", Donation.input_beds_available, False),
                           MethodToTest("input_number_of_donors", Donation.input_number_of_donors, False),
                           MethodToTest("evaluate_donation", Donation.evaluate_donation, False),
                           MethodToTest("print_donation", Donation.print_donation, False))

        while True:
            print("Commands:")
            print("\tExit: .")
            print("\tMethods:")
            for method in methods_to_test:
                print("\t\t" + method.name)
            print()
            uinp = input("Donation.")
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
                methods_to_test[index].invoke(our_donation)
            print()
            print('-' * 3)
            print()
