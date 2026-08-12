#client
#Attributes: clientID, clientName, clientEmail, clientPhone, clientAdddres (?), is_active
#Methods: update_phone, update_email, update_address, cancel_account()

class Client:
    def __init__(self, clientID, clientName, clientEmail, clientPhone, clientAddress, is_active=True):
        self.clientID = clientID
        self.clientName = clientName
        self.clientEmail = clientEmail
        self.clientPhone = clientPhone
        self.clientAddress = clientAddress
        self.is_active = is_active

    def client_info(self):
        print(f'{self.clientID}:{self.clientName}')
        print(f'Phone:{self.clientPhone}')
        print(f'Email:{self.clientEmail}')
        print(f'Address:{self.clientAddress}')
        print(f'Active:{self.is_active}')

    def update_phone(self, clientPhone):
        self.clientPhone = clientPhone
        print(f'New Phone: {self.clientPhone}')

    def update_email(self, clientEmail):
        self.clientEmail = clientEmail
        print(f'New Email: {self.clientEmail}')

    def update_address(self, clientAddress):
        self.clientAddress = clientAddress
        print(f'New Address: {self.clientAddress}')

    def update_account_status(self):
        if self.is_active == True:
            self.is_active= False
            print('Not Active')
        else:
            self.is_active = True
            print('Active')