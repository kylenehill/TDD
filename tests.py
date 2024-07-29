import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    
    def test1(self):
        test_value = ''
        message = "Test did NOT pass: {}".format(test_value)
        self.assertFalse(check_pwd(test_value), message)

    def test2(self):
    	test_value = 'testpwd'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test3(self):
    	test_value = 'testpasswordtoolongoftext'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test4(self):
    	test_value = 'TEST4LOWERCASE'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test5(self):
    	test_value = '1234567890'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test6(self):
    	test_value = 'test4uppercasechar'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test7(self):
    	test_value = 'test4withoutupper1'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test8(self):
    	test_value = 'checkFORanyDIGIT'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test9(self):
    	test_value = 'checkAgainForDIGIT'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)

    def test10(self):
    	test_value = 'checkFORanySymbo1'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)


if __name__ == '__main__':
    unittest.main()