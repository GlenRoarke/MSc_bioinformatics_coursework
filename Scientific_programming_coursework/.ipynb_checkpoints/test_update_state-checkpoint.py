#### Run simulation :::::::::::::::::::
import numpy as np
from numpy.random import default_rng
import forest_simulation_v2
rng = default_rng()
# 1) growth (parameter change)
p = 0
# 2) lightning
f = 0.1
# Steps and array size
num_steps = 500
array_size = (100,100)

# state easy to observe burning and neighbourhood rules
initial_state = np.array([[1,1,1,1,1],
                          [1,1,2,1,1], 
                          [1,2,3,2,1],
                          [1,1,2,1,1],
                          [1,1,1,1,1]])



def test_update_1():
    expect = np.array([[1,1,1,1,1],
                       [1,1,3,1,1], 
                       [1,3,1,3,1],
                       [1,1,3,1,1],
                       [1,1,1,1,1]])
    test_state = forest_simulation_v2.update_state(initial_state)
    
    assert (test_state == expect).all()
    

        
