from lib.estimate_reading_time import *

def test_estimate_reading_time_for_00words():
    texto = " "
    assert estimate_reading_time (texto) == 0

def test_estimate_reading_time_for_200words():
    texto = " ".join(map(str, range(200)))
    assert estimate_reading_time(texto) == 1

def test_estimate_reading_time_for_100words():
    texto = " ".join(map(str, range(100)))
    assert estimate_reading_time(texto) == 0.5

def test_estimate_reading_time_for_450words():
    texto = " ".join(map(str, range(450)))
    assert estimate_reading_time(texto) == 2.25