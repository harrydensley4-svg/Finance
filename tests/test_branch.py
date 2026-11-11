import pytest
from branch import Branch

class TestBranch:
    def test_branch_number_incorrect_type(self):
        with pytest.raises(TypeError):
            Branch('1', 'Name', 'location', '04010000')

    def test_branch_number_incorrect_value(self):
        with pytest.raises(ValueError):
            Branch(-1, 'Name', 'location', '04010000')

    def test_branch_name_type(self):
        with pytest.raises(TypeError):
            Branch(1, 10, 'location', '04010000')

    def test_branch_name_not_empty(self):
        with pytest.raises(ValueError):
            Branch(1, '', 'location', '04010000')

    def test_branch_location_type(self):
        with pytest.raises(TypeError):
            Branch(1, 'Name', True, '04010000')

    def test_branch_location_not_empty(self):
        with pytest.raises(ValueError):
            Branch(1, 'Name', '', '04010000')

    def test_branch_phone_type(self):
        with pytest.raises(TypeError):
            Branch(1, 'Name', 'location', 4010000)

    def test_branch_phone_not_empty(self):
        with pytest.raises(ValueError):
            Branch(1, 'Name', 'location', '')

    def test_branch_is_open_type(self):
        with pytest.raises(TypeError):
            Branch(1, 'Name', 'location', '04010000', 'Open')

    def test_branch_phone_property(self, branch):
        assert branch.phone == '0401660716'

    def test_opening_branch(self, branch):
        assert branch.open_branch() == True

    def test_opening_an_open_branch(self, branch):
        branch.open_branch()
        assert branch.open_branch() == None

    def test_closing_branch(self, branch):
        branch.open_branch()
        assert branch.close_branch() == False

    def test_closing_closed_branch(self, branch):
        assert branch.close_branch() == None

    def test_set_phone(self, branch):
        assert branch.set_phone('04013330') == True
        assert branch.phone == '04013330'

    def test_set_invalid_phone(self, branch):
        assert branch.set_phone(404040) == False

    def test_set_empty_phone(self, branch):
        assert branch.set_phone('') == False

    def test_name_property(self, branch):
        assert branch.name == 'Adelaide'

    def test_location_property(self, branch):
        assert branch.location == 'Adelaide'

    def test_is_open_property(self, branch):
        assert branch.is_open == False

    def test_branch_string(self, branch):
        assert str(branch) == f'Branch {branch.number} {branch.name} can be contacted by calling the number {branch.phone} or going to {branch.location}. Open? = {branch.is_open}'

    def test_branch_repr(self, branch):
        assert repr(branch) == f'Branch(Branch Number = {branch.number}, Name = {branch.name}, Location = {branch.location}, Phone = {branch.phone}, Open? = {branch.is_open})'

