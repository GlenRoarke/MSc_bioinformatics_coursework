import numpy as np
from numpy.random import default_rng
rng = default_rng()


#define functions to apply rules :::::::::::::::::::::::

def initialise_state(num_steps, array_size, initial_state):
    #history = np.zeros((5 *num_steps ,array_size), dtype=int)
    #create the array to hold the simulation based on the number of steps
    initial_state = rng.integers(low=1, high=2, endpoint =True, size=(array_size))
    return initial_state

EMPTY = 1
TREE = 2
FIRE = 3

def lightning(new_grid):
    light_grid = new_grid
    for (x,y), value in np.ndenumerate(light_grid):
        if value == 2 and np.random.random() <= f:
            light_grid[x,y] = FIRE
    return light_grid
            
def growth(new_grid):
    growth_grid = new_grid
    for (x,y), value in np.ndenumerate(growth_grid):
         if value == 1 and np.random.random() <= p:
            #if there is growth make it a tree or fire resistant tree
            growth_grid[x,y] = np.random.choice([2,5], 1, p =[0.5, 0.5])
    return growth_grid

 
            
def update_state(previous_grid):
    """
    Contains extra if statements to generate different parameters
    """
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
            new_grid[x,y] = 1 # deforestation at the edges of the forest
            
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
            new_grid[x,y] = np.random.choice([2,5], 1, p =[0.5, 0.5])
         # rule 5 - mining activity   
        elif value == 5 and np.random.random() <= pn:
            new_grid[x,y] = EMPTY
    
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
p = 0.1

#growth of new tree
pn = 0.01

#lightning
f = 0.01
# Steps and array size
num_steps = 500
array_size = (20,20)

initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)


#4) set random array - code limitation this should be done in function.
#initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)

# generate a 3D numpy array for each state
forest_state = run_simulation(num_steps, array_size, initial_state)


#save compressed folder for analysis
filename = "evolution_forest_simulation_new"
np.savez_compressed(filename, state=forest_state)


print(f"SUCCESS - \nSimulation for {num_steps} steps, with an array size of {array_size} has completed.\nFigure named Forest_fire_simulation_steady_state has been created. \nPlease move on to the jupypter notebook to visualise the simulation and different parameters more reproducibly. \nA compressed file called {filename}.npz is also available")
print(f"The growth rate is {p} and the lightning rate is {f}")

