# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:39:52 2023

@author: olsso

Project goal: simulate random walk 500 times of starting at step 0
and tossing a dice getting increased and decreased amount of steps depending
on dice toss. Then calculating the probability of reaching step 60 for the
entire set of random walks.
"""

# numpy and matplotlib imported
import numpy as np
import matplotlib.pyplot as plt

#setting seed reproducability
np.random.seed(123)

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        #random clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

#Calculate probability of making it all the way
prob = np.mean( ends >= 60 )
print("The probabilty of making it all the way is =", prob)