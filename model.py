# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:37:53 2021

@author: helena
"""
# Import libraries for accessing the web page 
import requests
import bs4

# Download and read in the web data 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html') # r requests the HTTP data from the web page 
content = r.text # content turns the web page data to a str
soup = bs4.BeautifulSoup(content, 'html.parser') # soup uses a parser module BeautifulSoup to turn the web page data into a data object model 
td_ys = soup.find_all(attrs={"class" : "y"}) # y coordinates
td_xs = soup.find_all(attrs={"class" : "x"}) # x coordinates 
#print(td_ys) # print the y coordinates 
#print(td_xs) # print the x coordinates

# Import and change matplotlib backends
import matplotlib
matplotlib.use('TkAgg')

# Import libraries
import random
import matplotlib.pyplot
import agentframework
import csv

# Set a seed to create the same numbers each time the code is run
random.seed(4323432421)

# Read in the CSV data file and create a list 
f = open('in.txt') # f opens to the text file 
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC) # reader reads the text file and turns the data into integers 
environment = [] # create an empty list for the complete text file data
for row in reader: # reads in each row in the text file 
    rowlist = [] # creates an emplty list for the rows of data in the text file data 
    for value in row: # reads in each value in each row 
        rowlist.append(value) # adds each value in each row to the emplty list 
    environment.append(rowlist) # adds the list of rows to the empty list for the complete text file data 
f.close()

# Check environment by plotting it
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

# Create the figure
fig = matplotlib.pyplot.figure(figsize=(7, 7)) # fig creates a figure for the data to be displayed in 
ax = fig.add_axes([0, 0, 1, 1]) # add axes to the figure 

# Initialising the agents
num_of_agents = 5 # determines the number of pairs of coordintes created 
agents = [] # an empty list for the pairs of coordinate data 
for i in range(num_of_agents): 
    y = int(td_ys[i].text) # assigns the value y to the web page y coordinates 
    x = int(td_xs[i].text) # assigns the value x to the web page x coordinates 
    agents.append(agentframework.Agent(environment, agents, x, y)) # adds these coordinates to the Agent class

# Setting conditions for the agents 
num_of_iterations = 5 # the number of times the model will run 
neighbourhood = 20 # the number of interactions agents with have with their neighbours 
carry_on = True

# Shuffle the data, then move and interact the agents, then change the environment data
def update(frame_number):
    fig.clear()   
    global carry_on
    for j in range(num_of_iterations): # for the set number of interaction of the model 
        for i in range(num_of_agents): # for the set number of pairs of coordinates 
            random.shuffle(agents) # randomly shuffles the order of the coordinates 
            agents[i].move() # move the agents dependent on their initial value 
            agents[i].eat() # allows the agents to change the environment 
            agents[i].share_with_neighbours(neighbourhood) # allows the agents to communicate with the other agents 
# A stopping condition for the model 
        if random.random() < 0.5: 
            carry_on = False
            #print("stopping condition")
# Create a scatter plot of the agents 
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
            #print(agents[i][0],agents[i][1]) # check the agent values 

# Import GUI library 
import tkinter

# Run the function within the model and create an animation 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False, interval=1)
    canvas.draw()


# Edit the interface and add a menu 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


#Create text file of the final model data 
with open('modeldata.txt', 'w', newline='') as tf: # tf creates a new empty text file 
    for i in range (num_of_agents):
        tf.write(str([agents[i]._x, agents[i]._y])) # adds the agent data into the empty text file

# Set system to wait for user interaction 
tkinter.mainloop()



