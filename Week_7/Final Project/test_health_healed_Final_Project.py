import pytest
from W06_Prove_Milestone_Student_Chosen_Project import Character

@pytest.fixture
def character_with_health(request):
    # Create a Character instance with the specified health
    return Character(health=request.param)

@pytest.mark.parametrize("character_with_health, heal_amount, expected_health", [
    (pytest.param(50, 30, 80, id="heal_below_max_health")),
    (pytest.param(50, 50, 100, id="heal_equal_to_max_health")),
], indirect=["character_with_health"])
def test_health_healed(character_with_health, heal_amount, expected_health):
    # Call the health_healed method on the character_with_health instance
    character_with_health.health_healed(heal_amount)
    # Check if the character's health is updated correctly
    assert character_with_health.health == expected_health











pytest.main(["-v", "--tb=line", "-rN", __file__])