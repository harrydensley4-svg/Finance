class Branch:
    """
    A class to represent a bank branch by storing branch information,
    and managing its operating status (open/closed).

    Attributes:
        number: int
        name: str
        location: str
        phone: str
        is_open: bool

    """
    def __init__(self, number, name, location, phone, is_open=False):
        if isinstance(number, int) and not isinstance(number, bool) and number > 0:
            self.__number = number
        else:
            self.__number = 0
        if isinstance(name, str) and name.strip() != '':
            self.__name = name
        else:
            self.__name = 'Unknown'
        if isinstance(location, str) and location.strip() != '':
            self.__location = location
        else:
            self.__location = 'Unknown'
        if isinstance(phone, str) and phone.strip() != '':
            self.__phone = phone
        else:
            self.__phone = 'Unknown'
        if isinstance(is_open, bool):
            self.__is_open = is_open
        else:
            self.__is_open=False

    def get_number(self):
    # Returns the branch number.
        return self.__number

    def get_name(self):
    # Returns the branch name.
        return self.__name

    def get_location(self):
    # Returns the location of the branch.
        return self.__location

    def get_phone(self):
    # Returns the phone number of the branch.
        return self.__phone

    def get_is_open(self):
    # Returns the current opening status of the branch.
        return self.__is_open

    def open_branch(self):
    # If the branch is currently closed, it opens the branch. 
        if self.__is_open == False:
            self.__is_open = True
            print(f'{self.__name} is Open')
        else:
            print(f'{self.__name} is already open')

    def close_branch(self):
    # If the branch is currently open, it closes the branch.
        if self.__is_open == True:
            self.__is_open = False
            print(f'{self.__name} is Closed')
        else:
            print(f'{self.__name} is already closed')

    def set_phone(self, phone):
    # Update the phone number of the branch
    # Parameters: phone (str)
        print(f'Original Phone Number: {self.__phone}')
        if isinstance(phone, str) and phone.strip() != '':
            phone = phone.replace(" ", "")
            if phone.isdigit():
                self.__phone = phone
        print(f'The Phone Number has been Updated to: {self.__phone}')

    def __str__(self):
        return f'Branch {self.__number} {self.__name} can be contacted by calling the number {self.__phone} or going to {self.__location}. Open? = {self.__is_open}'

    def __repr__(self):
        return f'Branch(Branch Number = {self.__number}, Name = {self.__name}, Location = {self.__location}, Phone = {self.__phone}, Open? = {self.__is_open})'
