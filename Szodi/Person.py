__author__ = 'KoicsD'
import address


class Person():
    name = ""
    weight = 0
    birth_date = ""
    unique_id = ""
    phone_number = ""
    email = ""
    is_male = False
    address = None

    def __init__(self, name, weight, birth_date, unique_id, is_male):
        self.name = name
        self.weight = weight
        self.birth_date = birth_date
        self.unique_id = unique_id
        self.is_male = is_male

    def set_address(self, address):
        self.address = address

    def __repr__(self):
        return self.name + "(" + self.unique_id + ")"


daniel = Person("Daniel", 80, "1990.11.20", "601506MA", True)
print(daniel)
print(address.codecool_address.city)
