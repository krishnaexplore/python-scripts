"""
Precondition
   setup
   connection
   api

Test
TEST

Assertion

Postcondition
  clean
  close

"""


import pytest

@pytest.fixture
def setup():
    print("Start browser")
    yield
    print("close browser")

def test_1(setup):
    print("Test1 executed")
    

def test_2(setup):
    print("Test2 executed")
    

def test_3(setup):
    print("Test3 executed")
    


