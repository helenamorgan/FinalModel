# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:37:53 2021

@author: helena
"""
# Import libraries for accessing the web page 
import requests
import bs4

# Download and read in the web data 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

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
f = open('in.txt')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# Check environment by plotting it
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

# Create the figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Initialising the agents
num_of_agents = 5
agents = []
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, x, y))

# Setting conditions for the agents 
num_of_iterations = 5
neighbourhood = 20
carry_on = True

# Shuffle the data, then move and interact the agents, then change the environment data
def update(frame_number):
    fig.clear()   
    global carry_on
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
# A stopping condition for the model 
        if random.random() < 0.5:
            carry_on = False
            print("stopping condition")
# Create a scatter plot of the agents 
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
            #print(agents[i][0],agents[i][1])

# Import GUI library 
import tkinter

# Run the function within the model 
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

# Set system to wait for user interaction 
tkinter.mainloop()


    
