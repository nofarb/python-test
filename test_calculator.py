# test_calculator.py
import pytest
import time
from calculator import Calculator

def test_add(): 
    calc = Calculator()
    assert calc.add(2, 4) == 6
    
def test_long_running_one():
    # Simulating a long process
    print("Test 1 is running, simulating a long process...")
    assert True  # Simulating a successful test
