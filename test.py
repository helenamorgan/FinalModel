# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:07:58 2021

@author: helena
"""
"""
Unit testing framework to ensure the model is correctly 
calculating distance between the agents 
"""

# Import the test module and the source code that will be checked
import unittest
import agentframework


class TestAgent(unittest.TestCase): # identifies this class is to be tested 
        
    def test_distance(self):
        """
        This function tests the agentframework distance function 
        to ensure the correct values are being calculated between two sets of coordinates.

        Returns
        -------
        None.

        """
        environment = [] # create an empty list 
        agents = [] # create an empty list 
        a = agentframework.Agent(environment, agents, 0, 0) # define a through introducing the agent class and setting values for the x and y variables 
        b = agentframework.Agent(environment, agents, 3, 4) # define b through introducing the agent class and setting values for the x and y variables
        print("ax", a.getx()) # check the value of ax
        print("ay", a.gety()) # check the value of ay
        print("bx", b.getx()) # check the value of bx
        print("by", b.gety()) # check the value of by
        d = a.distance_between(b) # d calculates the distance between the x and y variables of a and b 
        print("Distance between these agents is " + str(d)) # prints the distance 
        self.assertEqual(d, 5, "should be 5") # checks the distance function produces the same values as the test values 

if __name__ == '__main__': # the class runs within framework within the unittest library 
    unittest.main() # tests functions by scanning for subclasses of unittest.TestCase 