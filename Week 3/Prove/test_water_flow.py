from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    # This Function is used to test the water column height.
    column_height_result = water_column_height(0.00, 0.00)
    assert isinstance(column_height_result, float), "Water column height function must return a float value."

    assert water_column_height(0.0, 0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9
    
def test_pressure_gain_from_water_height():
    # This Function is used to test the pressure gained from the water height
    pressure_gain_result = pressure_gain_from_water_height(0.0)
    assert isinstance(pressure_gain_result, float), "Pressure gain from water function must return a float value."

    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe ():
    # This Function is used to test the pressure loss from pipes.

    #assert isinstance(value, float) ""

    pressure_loss_result = pressure_loss_from_pipe(0.048692, 0.0, 0.018, 1.75)
    assert isinstance(pressure_loss_result, float), "Pressure loss from pipe function must return a float value."

    assert pressure_loss_from_pipe(0.048692, 0.0, 0.018, 1.75) == approx(0.0000, abs=.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs= 0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx( -61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)






# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])