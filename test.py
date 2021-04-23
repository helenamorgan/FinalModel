# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:07:58 2021

@author: helena
"""

# test.py
import unittest
import model

class TestDocs(unittest.TestCase):

    def test_agent(self):
        a = model.Calc()
        self.assertEqual(a.add(1,2), 3)


if __name__ == '__main__':
    unittest.main()