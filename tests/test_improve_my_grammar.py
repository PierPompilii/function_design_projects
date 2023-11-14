
from lib.improve_my_grammar import *

def test_without_capital_and_punctuation():
    result = improve_my_grammar("hello world")
    assert result == False

def test_with_capital_no_punctuation():
    result = improve_my_grammar ("Hello world")
    assert result == False
    
def test_with_capital_and_punctuation():
    result = improve_my_grammar ("Hello world!")
    assert result == True