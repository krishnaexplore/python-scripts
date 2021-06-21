def test_1():
    x = 10
    y = 10
    assert x == y

def test_2():
    name = "Selinium"
    title = "Selinium is a web automation tool"
    assert name in title

def test_3():
    name = "Jenkins"    
    title = "Jenkins is CI server"
    assert name in title, "Title does not match"

#pytest -rA    


#pytest test_second.py
#pytest test_second.py -rA -k login
#pytest -rA -k login
# -fE
# pytest -rA --junitxml="report1.xml"

#pytest markers
#