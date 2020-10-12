import unittest

from Module7.fun_with_collections.basic_list_exception import make_list()


class MyTestCase(unittest.TestCase):

    def test_measurements_rectangle(self):
        self.assertEqual(make_list()([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(make_list()([3.5]), "Perimeter = 14.0 Area = 12.25")


if __name__ == '__main__':
    unittest.main()
