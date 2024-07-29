def check_pwd(test_value):

	if len(test_value) == 0:
		return False
	if len(test_value) < 8 or len(test_value) > 20:
		return False

	lower_count = 0
	for char in test_value:
		if char.islower() == True:
			lower_count += 1

	if lower_count == 0:
		return False

	return True