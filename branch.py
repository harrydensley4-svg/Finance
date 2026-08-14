class Branch:
    def __init__(self, number, name, location, phone, is_open=False):
        self.number = number
        self.name = name
        self.location = location
        self.phone = phone
        self.is_open = is_open

    def open_branch(self):
        if self.is_open == False:
            self.is_open = True
            print(f'{self.name} is Open')
        else:
            print(f'{self.name} is already open')

    def close_branch(self):
        if self.is_open == True:
            self.is_open = False
            print(f'{self.name} is Closed')
        else:
            print(f'{self.name} is already closed')

    def update_phone(self, phone):
        print(f'Original Phone Number: {self.phone}')
        self.phone = phone
        print(f'The Phone Number has been Updated to: {self.phone}')

    def __str__(self):
        return f'Branch {self.number} {self.name} can be contacted by calling the number {self.phone} or going to {self.location}. Open? = {self.is_open}'

    def __repr__(self):
        return f'Branch(Branch Number = {self.number}, Name = {self.name}, Location = {self.location}, Phone = {self.phone}, Open? = {self.is_open})'
