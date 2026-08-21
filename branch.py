class Branch:
    def __init__(self, number, name, location, phone, is_open=False):
        self.__number = number
        self.__name = name
        self.__location = location
        self.__phone = phone
        self.__is_open = is_open

    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_phone(self):
        return self.__phone

    def get_is_open(self):
        return self.__is_open

    def open_branch(self):
        if self.__is_open == False:
            self.__is_open = True
            print(f'{self.__name} is Open')
        else:
            print(f'{self.__name} is already open')

    def close_branch(self):
        if self.__is_open == True:
            self.__is_open = False
            print(f'{self.__name} is Closed')
        else:
            print(f'{self.__name} is already closed')

    def set_phone(self, phone):
        print(f'Original Phone Number: {self.__phone}')
        self.__phone = phone
        print(f'The Phone Number has been Updated to: {self.__phone}')

    def __str__(self):
        return f'Branch {self.__number} {self.__name} can be contacted by calling the number {self.__phone} or going to {self.__location}. Open? = {self.__is_open}'

    def __repr__(self):
        return f'Branch(Branch Number = {self.__number}, Name = {self.__name}, Location = {self.__location}, Phone = {self.__phone}, Open? = {self.__is_open})'
