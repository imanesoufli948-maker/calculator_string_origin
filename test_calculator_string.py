from main import calcul_string
def test_Add():
    assert calcul_string("") == 0
    assert calcul_string("1") == 1
    assert calcul_string("1,2") == 3


test_Add()