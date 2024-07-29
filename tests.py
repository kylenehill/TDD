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


if __name__ == '__main__':
    unittest.main()