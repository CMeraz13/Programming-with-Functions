import pytest
from W06_Prove_Milestone_Student_Chosen_Project import roll_for_success  # Adjust the import path as needed
from unittest.mock import patch

class MockCharacter:
    def __init__(self, dexterity):
        self.dexterity = dexterity

@pytest.mark.parametrize("roll, dexterity, expected", [
    (1, 5, True),  # Test case where roll is less than dexterity, expecting success
    (20, 10, False),  # Test case where roll is higher than dexterity, expecting failure
    (10, 10, True),  # Edge case where roll equals dexterity, expecting success
])
def test_roll_for_success(roll, dexterity, expected):
    character = MockCharacter(dexterity=dexterity)
    with patch("your_module.random.randint", return_value=roll):
        assert roll_for_success(character, "dexterity") == expected