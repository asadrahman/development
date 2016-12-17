#!/bin/env python

import unittest
from Capitals import Capitals

class processCapitals(unittest.TestCase):
    def setUp(self):
        self.Capitals = Capitals()

    def test_get_capitals(self):
        
    	self.assertEqual(self.Capitals.get_capitals(), self.Capitals.capitals)

if __name__ == '__main__':
    unittest.main()