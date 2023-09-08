import numpy as np
from numpy.random import default_rng
rng = default_rng()


#define functions to apply rules :::::::::::::::::::::::

def initialise_state(num_steps, array_size, initial_state):
    #history = np.zeros((5 *num_steps ,array_size), dtype=int)
    #create the array to hold the simulation based on the number of steps
    initial_state = rng.integers(low=1, high=2, endpoint =True, size=(array_size))
    return initial_state

#assign action to variable
EMPTY = 1
TREE = 2
FIRE = 3

            
def update_state(previous_grid): 
    #create new grid for next step
    new_grid = np.zeros_like(previous_grid)

    #RULE 1 - if cell = 3 it changes to 1 :::::::::::::::::::::::::::::::::::::::::::::::
    for (x,y), value in np.ndenumerate(previous_grid):
        if value == 3:
            new_grid[x,y] = EMPTY
            #cell remains unchanged if not 3  
        else:
            new_grid[x,y] = value

    #RULE 2 - Neighbouring cells to (3) that are trees (2) BURN (3) ::::::::::::::::::::::
    # default burn value
    
    for (x,y), value in np.ndenumerate(previous_grid):
        
        #assign edges rules foro better readability.
        deforest_above = x - 1 < 0
        deforest_below = x + 1 == previous_grid.shape[0]
        deforest_left =  y + 1 == previous_grid.shape[1]
        deforest_right = y - 1 < 0

        if deforest_above or  deforest_below or deforest_left or deforest_right:
            new_grid[x,y] = 3 # deforestation at the edges of the forest
            
        elif value == 3:
            burn_cell = 3
            new_grid[x,y] = 1
            if previous_grid[x-1,y] == 2:
                new_grid[x-1,y] = burn_cell

            if previous_grid[x+1,y] == 2:
                new_grid[x+1,y] = burn_cell

            if previous_grid[x,y-1] == 2:
                new_grid[x,y-1] = burn_cell = 3

            if previous_grid[x,y+1] == 2:
                 new_grid[x,y+1]= burn_cell = 3
                    
       #Rule 3 - lightning           
        elif value == 2 and np.random.random() <= f:
            new_grid[x,y] = FIRE
         #rule 4 - growth   
        elif value == 1 and np.random.random() <= p:
            new_grid[x,y] = TREE
    
    return new_grid




def run_simulation(num_steps, array_size, initial_state):
    #create inital state
    state = initialise_state(num_steps, array_size, initial_state)
    history = []
    #append the empty list with the inital state
    history.append(state)
    
    for t in range(1,num_steps):
    #print(f" step: {i}")
    #print(update_state(history[i-1]))   
    #Reference previous time step in the list
        history.append(update_state(history[t-1]))
    #convert list to numpy array
        simulation = np.asarray(history)
        
    return simulation



#### Run simulation :::::::::::::::::::

##growth
p = 0.05
#lightning
f = 0.8
# Steps and array size
num_steps = 500
array_size = (20,20)

initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)


#4) set random array - code limitation this should be done in function.
#initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)

# generate a 3D numpy array for each state
forest_state = run_simulation(num_steps, array_size, initial_state)

#save compressed folder for analysis
filename = "attack_forest_simulation"
ext = ".png"
np.savez_compressed(filename, state=forest_state)


print(f"SUCCESS - \nSimulation {filename} for {num_steps} steps, with an array size of {array_size} has completed.\nFigure named Forest_fire_simulation_steady_state has been created. \nPlease move on to the jupypter notebook to visualise the simulation and different parameters more reproducibly. \nA compressed file called {filename}.npz is also available")
print(f"The growth rate is {p} and the lightning rate is {f}")


import numpy as np

with np.load("attack_forest_simulation.npz") as f:
    cells = f["state"]

p = 0.05
#lightning
f = 0.8
    
trees_count = []
fires_count = []
light_count = []
growth_count = []
total = np.count_nonzero(cells[0]) 

for time_step_state in cells:
    #tree percentage and append
    trees = np.count_nonzero(time_step_state == 2) / total * 100
    trees_count.append(trees)
    #fires percentage and append
    fires = np.count_nonzero(time_step_state == 3) / total * 100
    fires_count.append(fires)
    #lightning positive at 0 index
    light = f * 100
    light_count.append(light)
    #growth at at index 1
    growth_rate = p * 100
    growth_count.append(growth_rate)

    
#########
import pandas as pd

summary = pd.DataFrame({"number_of_trees": trees_count,
                        "number_of_fires": fires_count,
                        "lightning ratio": light_count,
                        "growth rate"    : growth_count
                       }
                      )
summary.index.name = "Time step"

#########

import seaborn as sns
import matplotlib.pyplot as plt
plt.interactive(True)

sns.set_theme()

g = sns.relplot(data=summary, kind="line").set(
    xlim=(0,None),
    ylim=(0,None),
)
g.set_axis_labels("Time-step", "Cells (%)")
g.fig.suptitle( "Low lightning, moderate growth")

plt.savefig(filename + ext, bbox_inches='tight')
#allows for re-running visualisation repeatly.
plt.show()




