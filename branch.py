class Branch:
    def __init__(self, number, name, location, phone, isOpen=False):
        self.number = number
        self.name = name
        self.location = location
        self.phone = phone
        self.isOpen = isOpen

    def open_branch(self):
        if self.isOpen == False:
            self.isOpen = True
            print(f'{self.name} is Open')
        else:
            print(f'{self.name} is already open')

    def close_branch(self):
        if self.isOpen == True:
            self.isOpen = False
            print(f'{self.name} is Closed')
        else:
            print(f'{self.name} is already closed')

    def update_phone(self, phone):
        print(f'Original Phone Number: {self.phone}')
        self.phone = phone
        print(f'The Phone Number has been Updated to: {self.phone}')
