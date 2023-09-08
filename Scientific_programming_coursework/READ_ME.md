# Forest Fire Simulation

## Authors
Glen Roarke

This project applies a series of neighbourhood rules to a numpy simulation of forest fires.

## Description

The main simulation is a python file named forest_simulation_v2.py, 
additional rules have been added into evolution_forest_simulation.py and forest_simulation_attack.py.
These can all be imported into the jupyterLab file Forest_fire_simulation_20230118.ipynb.

## Getting Started

There is a report alongside this notebook which explains the results further.

### Dependencies

* Windows 10
* Python 3.0 & Anaconda
* Jupyter labs is required to run animations.

### Installing

The software will be downloaded by cloning this repositiory. 

### Executing program

* Open the file Forest_fire_simulation_20230118.ipynb
* It has been executed and the results are displayed.
* If not click the restart and run all cells button to run multiple simulations and present the results.
* The file must be ran in sequential order. Executing individual chunks for animations will change the results.
* It will output several .npz files which are loaded into this notebook.
* It is recommended that you view the visualisations within the jupyter notebook.


## Testing 

* pytest can be carried out within the terminal for basic rules.
* test_lightning_rule_module.py highlights that growth probabilites are not imported well for this situation which is a limitation.


## Help

Running the help() will provide more information on function parameters.
* The simulations need to be run with a 5,5 grid to apply the rules correctly, due to the edges rule.

## Version History

* 0.1
    * Initial Release 18/01/2023

## License
University of Bristol


## Acknowledgments

Inspiration, code snippets, etc.
* (https://milliams.com/courses/numpy_simulation/Cellular%20automata.html))
* (https://en.wikipedia.org/wiki/Von_Neumann_neighborhood)
