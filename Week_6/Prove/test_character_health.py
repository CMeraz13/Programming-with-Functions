import pytest
from W06_Prove_Milestone_Student_Chosen_Project import character_health  

@pytest.mark.parametrize("health,encounters_result,expected", [
    (10, "You fought bravely.", ("You fought bravely.")),
    (0, "You encountered a dragon.", ("You Died", "Thank you for playing Fantasy Adventure!")),
])
def test_character_health(health, encounters_result, expected):
    assert character_health(health, encounters_result) == expected


pytest.main(["-v", "--tb=line", "-rN", __file__])