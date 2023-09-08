
import numpy as np
from numpy.random import default_rng
import forest_simulation_v2
rng = default_rng()
# 1) growth (parameter change)
p = 0
# 2) lightning
f = 0.8
# Steps and array size
num_steps = 5
array_size = (5,5)

initial_state = np.array([[1,1,1,1,1],
                          [1,1,2,1,1], 
                          [1,2,2,2,1],
                          [1,1,2,1,1],
                          [1,1,1,1,1]])



def test_update_1():
    expect = np.array([[1,1,1,1,1],
                       [1,1,1,1,1], 
                       [1,1,1,1,1],
                       [1,1,1,1,1],
                       [1,1,1,1,1]])
    test_state = forest_simulation_v2.run_simulation(num_steps, array_size, initial_state)
    
    assert (test_state[4] == expect).all()
    

        
