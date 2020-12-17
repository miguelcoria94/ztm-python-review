import unittest

import test

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = test.do_stuff(num)
        self.assertEqual(result, 15)

unittest.main()