import tools.calculator as cal


def test_calculate_addition():
    result = cal.calculate("8+8")
    assert result == 16

def test_calculate_substraction():
    result = cal.calculate("8-8")
    assert result == 0

def test_calculate_multiplication():
    result = cal.calculate("2*2")
    assert result == 4

def test_calculate_division():
    result = cal.calculate("4/2")
    assert result == 2

def test_calculate_error():
    result = cal.calculate("2/0")
    print(result)