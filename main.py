def sum_of_squares(a):
	result = 0
	for element in a:
		result += element**2
	return result

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
	assert sum_of_squares([2,2,2]) == 12


test_one()
test_two()
