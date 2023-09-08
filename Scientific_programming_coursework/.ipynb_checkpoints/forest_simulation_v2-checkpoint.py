import numpy as np
from numpy.random import default_rng
rng = default_rng()


#define simulation functions :::::::::::::::::::::::

def initialise_state(num_steps, array_size, initial_state):
    """
    Initialise the first state of the system.
    
    Args:
        num_steps (int): how many steps the simulation will run for
        array_size (tuple): the row and column size of numpy 2D array
        initial_state (np.ndarray): rng.integers() 
            2-dimensional initial state of the system with 1s and 2s Args: size=(array_size)
    Returns:
        np.ndarray: the random 2-dimensional array for the inital state in the system.
    Examples:
        >>> num_steps = 5
        >>> array_size = (5,5)
        >>> initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)
        >>> initialise_state(num_steps, array_size, initial_state)
        
        array([[1, 1, 2, 2, 1],
               [2, 1, 1, 2, 1],
               [2, 1, 1, 2, 2],
               [1, 2, 2, 2, 2],
               [1, 1, 1, 2, 1]], dtype=int64)
               
    Requires: 
        numpy as np
        numpy.random import default_rng
        
    Change log:
        GR - 05/01/2023 
            - fixed initialise state function randomisation.
        GR - 15/01/2023
            - Docstring added to functions
    
    """

    #create the array to hold the simulation input array size
    initial_state = rng.integers(low=1, high=2, endpoint =True, size=(array_size))
    return initial_state


# assign variables for rule application
EMPTY = 1
TREE = 2
FIRE = 3
            
def update_state(previous_grid): 
    """
    Applies the rules of the forest fire simulation to the previous time step.
    
    Args:
        previous_array (np.ndarray): the 2-dimensional previous state of the system.
        f (float): The probability ratio lighnting, assign outside function.
        p (float): The probability ratio growth, assign outside function.
    
    Rules: 
        Rule 1: if cell = 3 it BURNS to 1
        Rule 2: if Neighbouring cells to (3) that are trees (2) BURN (3)
        Rule 3: The chance of lightning within the system
        Rule 4: The chance of growth within the system
        
    Returns:
        np.ndarray: the 2D-dimensional new state of the system
        
    Examples:
        p = 0.1
        f = 0.05
        update_state(previous_grid)
        
    Change log:
        GR - 13/01/2023
            - Run simulation step with list to numpy conversion
            - Added in lightning strike ratio
            - Added growth ratio
            - Changed edges rule to default 1.
         GR - 17/01/2023
            - Rule 2 if & elif statement amended.
            - random.random() function replaces random.choice()
            
    Bugs: Probability ratios are assigned outside of function.
    
    """
    
    #create new grid for next step
    new_grid = np.zeros_like(previous_grid)

    #RULE 1 - if cell = 3 it BURNS to 1 :::::::::::::::::::::::::::::::::::::::::::::::
    for (x,y), value in np.ndenumerate(previous_grid):
        if value == 3:
            new_grid[x,y] = EMPTY
            #cell remains unchanged if not 3  
        else:
            new_grid[x,y] = value

    #RULE 2 - Neighbouring cells to (3) that are trees (2) BURN (3) ::::::::::::::::::::::
    
    
    for (x,y), value in np.ndenumerate(previous_grid):
        
        #assign edges rules foro better readability.
        deforest_above = x - 1 < 0
        deforest_below = x + 1 == previous_grid.shape[0]
        deforest_left =  y + 1 == previous_grid.shape[1]
        deforest_right = y - 1 < 0

        if deforest_above or  deforest_below or deforest_left or deforest_right:
            new_grid[x,y] = 1 # deforestation at the edges of the forest
        #When not and edge and burning apply to neighbour.    
        elif value == 3:
            burn_cell = 3
            new_grid[x,y] = 1
            #ABOVE
            if previous_grid[x-1,y] == 2:
                new_grid[x-1,y] = burn_cell
            #BELOW
            if previous_grid[x+1,y] == 2:
                new_grid[x+1,y] = burn_cell
            #LEFT
            if previous_grid[x,y-1] == 2:
                new_grid[x,y-1] = burn_cell
            #RIGHT
            if previous_grid[x,y+1] == 2:
                 new_grid[x,y+1]= burn_cell
                    
         #Rule 3 - lightning random burn from f parameter ::::::::::::::::::        
        elif value == 2 and np.random.random() <= f:
            new_grid[x,y] = FIRE
            
         #rule 4 - growth random from p parameter ::::::::::::::::::::::::::
        elif value == 1 and np.random.random() <= p:
            new_grid[x,y] = TREE
    
    return new_grid


def run_simulation(num_steps, array_size, initial_state):
    """
    Run the simulation with predefined parameters saving history.
    Args:
        initialise_state()
        update_state()
    Returns:
        np.ndarray: 3D-dimensional history of the simulation
        
    Example:
        p = 0.05
        f = 0.01
        num_steps = 500
        array_size = (20,20)
        initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)
        forest_simulation = run_simulation(num_steps, array_size, initial_state)
    
    """
    
    #create inital state
    state = initialise_state(num_steps, array_size, initial_state)
    history = []
    #append the empty list with the inital state
    history.append(state)
    #append each step to list
    for t in range(1,num_steps):
        history.append(update_state(history[t-1]))
    #convert list to numpy array
        simulation = np.asarray(history)
        
    return simulation

#### Run simulation :::::::::::::::::::

##growth
p = 0.05
#lightning
f = 0.01
# Steps and array size
num_steps = 500
array_size = (20,20)

initial_state = rng.integers(low=1, high=2, endpoint =True, size=array_size)

# generate a 3D numpy array for each state
forest_state = run_simulation(num_steps, array_size, initial_state)


#save compressed file for analysis
filename = "forest_simulation_new"
np.savez_compressed(filename, state=forest_state)

#display confirmation to the user and details of parameters.
print(f"SUCCESS - \nSimulation for {num_steps} steps, with an array size of {array_size} has completed.\nFigure named Forest_fire_simulation_steady_state has been created. \nPlease move on to the jupypter notebook to visualise the simulation and different parameters more reproducibly. \nA compressed file called {filename}.npz is also available")
print(f"The growth rate is {p} and the lightning rate is {f}")

