import unittest
from Module7.fun_with_collections.add_two_numbers import new_function


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(new_function(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
