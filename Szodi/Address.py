__author__ = 'KoicsD'


class Address():
    city = ""
    address = ""
    house = 0
    zip_code = 0000

    def __init__(self, city, address, house):
        self.city = city
        self.address = address
        self.house = house


codecool_address = Address("Miskolc", "Regi posta utca", 9)