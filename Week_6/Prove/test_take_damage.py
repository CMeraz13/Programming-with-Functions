import pytest
from W06_Prove_Milestone_Student_Chosen_Project import Character

@pytest.fixture
def character_with_health(request):
    # Create a Character instance with the specified health
    return Character(health=request.param)

@pytest.mark.parametrize("character_with_health, damage, expected_health", [
    (pytest.param(100, 20, 80, id="damage_below_current_health")),
    (pytest.param(100, 120, 0, id="damage_above_current_health")),
    (pytest.param(100, 100, 0, id="damage_equal_to_current_health")),
], indirect=["character_with_health"])
def test_take_damage(character_with_health, damage, expected_health):
    # Call the take_damage method on the character_with_health instance
    character_with_health.take_damage(damage)
    # Check if the character's health is updated correctly
    assert character_with_health.health == expected_health


pytest.main(["-v", "--tb=line", "-rN", __file__])