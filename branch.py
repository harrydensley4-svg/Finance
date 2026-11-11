class AlreadyOpenError(Exception):
    def __init__(self, message='The branch is already open'):
        super().__init__(message)


class AlreadyClosedError(Exception):
    def __init__(self, message='The branch is already closed'):
        super().__init__(message)


class Branch:
    """
    A class to represent a bank branch by storing branch information,
    and managing its operating status (open/closed).

    Attributes:
    -----------
    number (int): A unique identifier for each branch.
    name (str): The name of the branch.
    location (str): The location of the branch.
    phone (str): The Phone number corresponding to the branch.
    is_open (bool): Indicates whether the branch is open.

    Methods:
    --------
    get_number()
        Returns the branch number.
    get_name()
        Returns the name of the branch.
    get_location()
        Returns the location of the branch.
    get_phone()
        Returns the branch phone number.
    get_is_open()
        Returns whether the branch is open or not.
    open_branch()
        If the branch is closed, open the branch.
    close_branch()
        If the branch is opened, close the branch.
    set_phone()
        Update the branch phone number.
    """

    def __init__(self, number, name, location, phone, is_open=False):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('Branch number should be an integer')
        if number <= 0:
            raise ValueError('Branch number should be positive')

        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if name.strip() == '':
            raise ValueError('Name should not be empty')

        if not isinstance(location, str):
            raise TypeError('Location must be a string')
        if location.strip() == '':
            raise ValueError('Location must not be left empty')

        if not isinstance(phone, str):
            raise TypeError('Phone should be a string')
        if phone.strip() == '':
            raise ValueError('Phone should not be left empty')

        if not isinstance(is_open, bool):
            raise TypeError('Opening status must be represented by a bool')

        self.__number = number
        self.__name = name
        self.__location = location
        self.__phone = phone
        self.__is_open = is_open

    def get_number(self):
        """ Returns the branch number."""
        return self.__number

    def get_name(self):
        """ Returns the branch name."""
        return self.__name

    def get_location(self):
        """ Returns the location of the branch."""
        return self.__location

    def get_phone(self):
        """ Returns the phone number of the branch."""
        return self.__phone

    def get_is_open(self):
        """ Returns the current opening status of the branch."""
        return self.__is_open

    def open_branch(self):
        """ If the branch is currently closed, it opens the branch."""
        try:
            if self.__is_open != False:
                raise AlreadyOpenError()
            else:
                self.__is_open = True
                return self.__is_open
        except Exception as e:
            print(f'{e.__class__.__name__}:{e}')
            return None

    def close_branch(self):
        """ If the branch is currently open, it closes the branch."""
        try:
            if self.__is_open != True:
                raise AlreadyClosedError()
            else:
                self.__is_open = False
                return self.__is_open
        except Exception as e:
            print(f'{e.__class__.__name__}:{e}')
            return None

    def set_phone(self, phone):
        """
        Update the phone number of the branch

        Parameters: 
        -----------
        phone : str
            The new phone number of the branch

        Returns
        -------
        bool
            Returns true if the new phone number passes the validation checks.
            Otherwise, it returns false.

        """
        try:
            if not isinstance(phone, str):
                raise TypeError('Phone should be a string')
            if phone.strip() == '':
                raise ValueError('Phone should not be empty')
            phone = phone.replace(" ", "")
            if phone.isdigit():
                self.__phone = phone
            return True
        except Exception as e:
            print(f'{e.__class__.__name__}:{e}')
            return False

    number = property(get_number)
    name = property(get_name)
    location = property(get_location)
    phone = property(get_phone, set_phone)
    is_open = property(get_is_open)

    def __str__(self):
        """A readable string description."""
        return f'Branch {self.__number} {self.__name} can be contacted by calling the number {self.__phone} or going to {self.__location}. Open? = {self.__is_open}'

    def __repr__(self):
        """A developer friendly string representation of the branch."""
        return f'Branch(Branch Number = {self.__number}, Name = {self.__name}, Location = {self.__location}, Phone = {self.__phone}, Open? = {self.__is_open})'
