import unittest
from app.validators.inputvalidator import valid_input


class TestDataCapture(unittest.TestCase):
    def test_args(self):
        @valid_input()
        def custom_function(*args, **kwds):
            return True
        self.assertEqual(custom_function(3, x=3), True)
        self.assertRaises(ValueError, custom_function, None, '3')
        self.assertRaises(ValueError, custom_function, None, 1.1)
        self.assertRaises(ValueError, custom_function, None, 0)
        self.assertRaises(ValueError, custom_function, None, 1000)

        self.assertRaises(ValueError, custom_function, x='3')
        self.assertRaises(ValueError, custom_function, x=1.1)
        self.assertRaises(ValueError, custom_function, x=0)
        self.assertRaises(ValueError, custom_function, x=1000)
