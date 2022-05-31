# your User class goes here

class User:
    def __init__(self, name, email, address, license):
        self.name = name
        self.email = email
        self.address = address
        self.license = license



person1 = User('John', 'john@hotmail.com', '123 street name', '56789')
person2 = User('Sarah', 'sarah@hotmail.com', '897 street name', '92834')
person3 = User('Amy', 'amy@gmail.com', '456 street name', '0000')


print(person3.name)