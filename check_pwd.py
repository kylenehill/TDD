def check_pwd(test_value):

	if len(test_value) == 0:
		return False
	if len(test_value) < 8 or len(test_value) > 20:
		return False

	return True