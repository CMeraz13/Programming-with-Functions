import pytest
from W06_Prove_Milestone_Student_Chosen_Project import beginning_story  # replace your_module with the actual name of your Python file

@pytest.mark.parametrize("situation,expected", [
    (1, "Story 1"),
    (2, "Story 2"),
    (3, "Story 3"),
    (4, "Story 4"),
    (5, "Story 5"),
    (6, "Unknown Story"),  # Testing an out-of-bounds situation
])
def test_beginning_story(situation, expected):
    assert beginning_story(situation) == expected

pytest.main(["-v", "--tb=line", "-rN", __file__])