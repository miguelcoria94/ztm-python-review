import unittest

import test

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = test.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        num = 'asdfds'
        result = test.do_stuff(num)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = test.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

unittest.main()
