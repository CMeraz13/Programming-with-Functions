
from chemistry import make_periodic_table
import pytest

def test_make_periodic_table():

    table = make_periodic_table(" Actinium", "227")
    assert isinstance(table, str), "Make Periodic Table must return two strings"


    assert make_periodic_table ("Actinium, 227") == "Actinum 227"

