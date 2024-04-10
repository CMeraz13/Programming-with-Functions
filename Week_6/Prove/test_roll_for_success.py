import pytest
from unittest.mock import patch, MagicMock

# Assume your_module.roll_for_success is the function you want to test
from W06_Prove_Milestone_Student_Chosen_Project import roll_for_success

@pytest.fixture
def mock_character():
    # Create a mock character with a dexterity attribute
    character = MagicMock()
    character.dexterity = 10
    return character

@patch("your_module.random.randint", return_value=10)
def test_roll_for_success_success(mock_randint, mock_character):
    assert roll_for_success(mock_character, 'dexterity') is True

@patch("your_module.random.randint", return_value=11)
def test_roll_for_success_failure(mock_randint, mock_character):
    assert roll_for_success(mock_character, 'dexterity') is False