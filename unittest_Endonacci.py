# This code is an example of unittesting

import unittest

from Endonacci import *


class EndonacciTestCase(unittest.TestCase):
    def test_result(self):
        self.assertEqual(endonacci(4, 3), 1)

    def test_input(self):
        self.assertRaises(ValueError, endonacci, "hello", 2)
