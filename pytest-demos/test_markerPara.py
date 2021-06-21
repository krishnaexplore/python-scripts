import pytest

@pytest.mark.parametrize("username, password", 
    [
        ("Selenium","WebDriver"),
        ("Python", "Pytest"),
        ("Krishna","G")
    ]
)
def test_login(username,password):
    print(username)
    print(password)