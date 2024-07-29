import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):
    
    def test1(self):
        test_value = ''
        message = "Test did NOT pass: {}".format(test_value)
        self.assertFalse(check_pwd(test_value), message)

    def test2(self):
    	test_value = 'testpassword123'
    	message = "Test did NOT pass: {}".format(test_value)
    	self.assertFalse(check_pwd(test_value), message)


if __name__ == '__main__':
    unittest.main()