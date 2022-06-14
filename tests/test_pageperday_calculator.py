from pageperday_calculator import __version__
from pageperday_calculator import app

def test_version():
    assert __version__ == '0.1.0'

def test_calculate_pages_for_small_amount():
    expected = 5.0
    results  = app.calculate_pages(20,5,3)
    assert expected == results

def test_calculate_pages_for_extreme_amount():
    expected = 100
    results = app.calculate_pages(300, 100, 2)
    assert expected == results