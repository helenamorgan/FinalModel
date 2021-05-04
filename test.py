# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:07:58 2021

@author: helena
"""

# test.py
import unittest
import agentframework
import model
import tkinter

root = tkinter.Tk()
root.quit()

class TestAgent(unittest.TestCase):

    def test_move(self):
        self._y = 35
        a = agentframework.Agent
        a.move(self._y)
        self.assertEqual(a.move(), 36, "should be 36")

if __name__ == '__main__':
    unittest.main()