from main import calcul_string
def test_Add():
    assert calcul_string("") == 0
    assert calcul_string("1") == 1


test_Add()