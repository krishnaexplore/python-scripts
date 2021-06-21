import pytest

@pytest.mark.smoke
def test_login():
    print("login")

@pytest.mark.regression     
def test_addProduct():
    print("add product")
@pytest.mark.smoke
def test_logout():
    print("logout")

 #pytest test_markersdemo.py -m regression   