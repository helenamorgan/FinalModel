# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:41:19 2021

@author: helena
"""

import random

class Agent(): 
    """
    Class declaration for the Agent class. Provides method for moving and interacting 
    coordinates within a set environment. 
    """

    """
    Implementing property attributes for the coordinates
    """
    def setx(self, x):
        self._x = x
        
    def getx(self, x):
        return self._x
    
    def sety(self, y):
        self._y = y
        
    def gety(self, y):
        return self._y
        
    def __init__(self, environment, agents, x=None, y=None):
        """
        This constructor function initialises the attributes of the Agent class. 
        

        Parameters
        ----------
        environment : list of integers
            A list of data from the in.text file  
        agents : list of integers
            A list of the x and y coordinates
        x : integer
            Coordinate data scraped from a web page
        y : integer
            Coordinate data scraped from a web page 

        Returns
        -------
        None.

        """
        self.environment = environment
        self.store = 0
        self.agents = agents
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = x
    
    
    def move(self): 
        """
        This function alters the position of the agents randomly 

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    
    def eat(self):
        """
        This function shares the agents location with the other agents allowing for communication and interaction. 

        Returns
        -------
        None.

        """
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    
    def share_with_neighbours(self, neighbourhood):
        """

        This function uses the distance between one agent compared with all of the other agents. 
        If this distance is within the set neighbourhood distance, 
        this function sets and stores the agents and its neighbours as equal to their combined average.   

        Parameters
        ----------
        neighbourhood : integer
            The set distance that is the limit for the agents to be defined as neighbours. 

        Returns
        -------
        None.

        """
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                distancesum = self.store + agent.store
                ave = distancesum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(distance) + " " + str(ave))
                #print("neighbourhood" + "=" + str(neighbourhood))
                
    def distance_between(self, agent):
        """
        This function calculates the final distance between the agents using Pythagoras Theorem. 

        Parameters
        ----------
        agent : integer
            A list of the x and y coordinates

        Returns
        -------
        integer
            The final distance between the agents. 

        """
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
        
    