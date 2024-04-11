from typing import Literal
import pytest
from unittest.mock import patch, MagicMock
from W06_Prove_Milestone_Student_Chosen_Project import roll_for_success  


class Character:
    def __init__(self, required_stat_value):
        self.dexterity = required_stat_value

# Define a fixture to create character instances
@pytest.fixture
def character(request):
    return Character(request.param)

@pytest.mark.parametrize("character, roll_value, expected", [
    (pytest.param(15, 10, True, id="success_case")),
    (pytest.param(15, 16, False, id="failure_case")),
], indirect=["character"])
def test_roll_for_success(character, roll_value, expected):
    with patch('W06_Prove_Milestone_Student_Chosen_Project.random.randint', return_value=roll_value):
        assert roll_for_success(character, 'dexterity') == expected

pytest.main(["-v", "--tb=line", "-rN", __file__])