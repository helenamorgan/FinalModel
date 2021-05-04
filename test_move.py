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


class TestAgent(unittest.TestCase):

    
    def test_move(self):
        """
        The function tests the move function in agentframework. 
        This test is dependent on the seed being set. 

        Returns
        -------
        None.

        """
        environment = [] # create an empty list 
        agents = [] # an empty list  
        a = agentframework.Agent(environment, agents, None, 35) # defines a by introduce the agent class and defines the x and y variables
        print("x", a.getx()) # check the value of x
        print("y", a.gety()) # check the value of y
        agents.append(a) # adds these  to the empty agents class
        a.move() # moves the x and y coordinates
        print("x", a.getx()) # check the value of x 
        print("y", a.gety()) # check the value of y
        self.assertEqual(a.gety(), 36, "should be 36") # test the value has moved correctly 
        
    def test_distance(self):
        """
        

        Returns
        -------
        None.

        """
        environment = [] # create an empty list for the complete text file data
        agents = [] # an empty list for the pairs of coordinate data 
        a = agentframework.Agent(environment, agents, 0, 0)
        b = agentframework.Agent(environment, agents, 3, 4)
        print("ax", a.getx())
        print("ay", a.gety())
        print("bx", b.getx())
        print("by", b.gety())
        d = a.distance_between(b) # adds these coordinates to the Agent class
        self.assertEqual(d, 5, "should be 5")

if __name__ == '__main__':
    unittest.main()