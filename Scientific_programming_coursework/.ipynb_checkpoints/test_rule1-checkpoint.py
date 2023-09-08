## Testing Rule 1
# Date: 2023/01/15
# Purpose: To test if statement in Rule 1.

import numpy as np
from numpy.random import default_rng
rng = default_rng()
num_steps = 5
array_size = (5,5)
initial_state = initial_state = np.array([
                       [1,1,1,1,1],
                       [1,3,3,3,1], 
                       [1,3,3,3,1],
                       [1,3,3,3,1],
                       [1,1,1,1,1]])

#RULE 1 - if cell = 3 it BURNS to 1 :::::::::::::::::::::::::::::::::::::::::::::::
#create new grid for next step
new_grid = np.zeros_like(initial_state)
for (x,y), value in np.ndenumerate(initial_state):
    if value == 3:
        new_grid[x,y] = 1
            #cell remains unchanged if not 3  
    else:
        new_grid[x,y] = value
            
#test burning rule


def test_rule_1():
    expect = 1
    for (x,y), value in np.ndenumerate(new_grid):
        assert value == expect
        

    

            


    
    
        
