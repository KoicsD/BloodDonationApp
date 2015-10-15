__author__ = 'KoicsD'


from donor_register import Donor
from location_register import Donation


if not __name__ == "__main__":
    print("This file should be __main__!!!")
else:
    my_donor = Donor()
    if my_donor.suitable:
        my_donation = Donation()
