import unittest
from Module7.fun_with_collections.ask_ok import ask_ok
import unittest.mock as mock


class FunctionTestCase(unittest.TestCase):

    def test_no_response(self):
        with mock.patch('builtins.input', side_effect=['n']):
            assert ask_ok('Do you really want to quit?') == False 
    def test_yes_response(self):
        with mock.patch('builtins.input', side_effect=['y']):
            assert ask_ok('Do you really want to quit?') == True            
    def test_invalid_default_response(self):
        with mock.patch('builtins.input', side_effect=['nah']):
            assert ask_ok('Do you really want to quit?') == 'Please try again!' 
    def test_invalid_custom_response(self):
        with mock.patch('builtins.input', side_effect=['nah']):
            assert ask_ok(prompt='Do you really want to quit?', reminder='Come on, only yes or no!') == 'Come on, only yes or no!' 
if __name__ == '__main__':
    unittest.main()
    

