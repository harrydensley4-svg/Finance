import pytest
from client import Client

class TestClient:
    def test_client_id_type(self):
        with pytest.raises(TypeError):
            Client('1', 'Harry', 'email@gmail.com', '040404', 'Address')

    def test_client_id_value(self):
        with pytest.raises(ValueError):
            Client(0, 'Harry', 'email@gmail.com', '040404', 'Address')

    def test_client_email_empty(self):
        with pytest.raises(ValueError):
            Client(1, 'Harry', '', '040404', 'Address')

    def test_client_name_type(self):
        with pytest.raises(TypeError):
            Client(1, True, 'email@gmail.com', '040404', 'Address')

    def test_empty_client_name(self):
        with pytest.raises(ValueError):
            Client(1, '', 'email@gmail.com', '040404', 'Address')

    def test_client_phone_type(self):
        with pytest.raises(TypeError):
            Client(1, 'Harry', 'email@gmail.com', 40404, 'Address')

    def test_client_phone_whitespace(self):
        with pytest.raises(ValueError):
            Client(1, 'Harry', 'harry@gmail.com', '   ', 'Address')

    def test_client_email_type(self):
        with pytest.raises(TypeError):
            Client(1, 'Harry', 'email@gmail.com', '040404', False)

    def test_empty_client_email(self):
        with pytest.raises(ValueError):
            Client(1, 'Harry', 'email@gmail.com', '040404', '')

    def test_client_contact_method_type(self):
        with pytest.raises(TypeError):
            Client(1, 'Harry', 'email@gmail.com', '040404', 'Address', True)

    def test_empty_client_contact_method(self):
        with pytest.raises(ValueError):
            Client(1, 'Harry', 'email@gmail.com', '040404', 'Address', '')

    def test_client_is_active_type(self):
        with pytest.raises(TypeError):
            Client(1, 'Harry', 'email@gmail.com', '040404', 'Address', 'phone', 'yes')

    def test_client_add_valid_account(self, client, savings_account):
        assert client.add_account(savings_account) == True
        assert savings_account.client_id == client.client_id

    def test_client_add_invalid_account_type(self, client):
        assert client.add_account('Account') == False

    def test_client_add_existing_account(self, client, savings_account):
        client.add_account(savings_account)
        assert client.add_account(savings_account) == False

    def test_client_remove_account(self, client, savings_account):
        client.add_account(savings_account)
        client.remove_account(savings_account.account_id)
        assert savings_account not in client.accounts

    def test_client_remove_not_existing_account(self, client, savings_account):
        assert client.remove_account(savings_account.account_id) == None

    def test_set_preferred_branch(self, client, branch):
        assert client.set_preferred_branch(branch) == True

    def test_set_preffered_branch_invalid_type(self, client):
        assert client.set_preferred_branch('This Branch') == False
        assert client.preferred_branch == None

    def test_client_name_property(self, client):
        assert client.client_name == 'Harry'

    def test_client_id_property(self, client):
        assert client.client_id == 1

    def test_client_set_address(self, client):
        client.set_address('New address')
        assert client.client_address == 'New address'

    def test_client_set_phone(self, client):
        client.set_phone('0400505050')
        assert client.client_phone == '0400505050'

    def test_client_invalid_email_change(self, client):
        client.set_email(True)
        assert client.client_email == 'harry@gmail.com'

    def test_client_email_change(self, client):
        client.set_email('newemail@gmail.com')
        assert client.client_email == 'newemail@gmail.com'

    def test_find_nonexistent_account(self, client):
        assert client.find_account(1) == False

    def test_find_account(self, client, savings_account):
        client.add_account(savings_account)
        assert str(client.find_account(1)) == f'Account ID: {savings_account.account_id}, is a {savings_account.account_type} account with a balance of ${savings_account.balance}'

    def test_set_preferred_contact_method_phone(self, client):
        client.set_preferred_contact('Phone')
        assert client.contact_method == 'Phone'

    def test_set_preferred_contact_method_email(self, client):
        client.set_preferred_contact('Email')
        assert client.contact_method == 'Email'

    def test_set_incorrect_preferred_contact_method(self, client):
        client.set_preferred_contact('Carrier Pigeon')
        assert client.contact_method == 'Phone'

    def test_set_incorrect_type_contact_method(self, client):
        client.set_preferred_contact(True)
        assert client.contact_method == 'Phone' 

    def test_toggle_account_status(self, client):
        client.set_account_status(False)
        assert client.is_active == False

    def test_str_for_client_with_no_accounts(self, client):
        assert str(client) == f'{client.client_name} has a phone number {client.client_phone} and has a preferred contact method of {client.contact_method}. No current Accounts.'

    def test_str_for_client_with_account(self, client, savings_account):
        client.add_account(savings_account)
        assert str(client) == f'{client.client_name} has a phone number {client.client_phone} and has a preferred contact method of {client.contact_method}. Accounts: ' + '\n' + '- ' + str(savings_account)

    def test_client_repr(self, client):
        assert repr(client) == f'Client(Client ID = {client.client_id}, Client Name = {client.client_name}, is_active = {client.is_active}, Client Email = {client.client_email}, Client Phone = {client.client_phone}, Client Address = {client.client_address}, Preferred Contact Method = {client.contact_method}, Accounts: {client.accounts})'