import numpy as np
from classes.body import Body
from classes.simulation import Simulation
from energy_plotter import make_energy_graph

#input angle in degrees and length in meters
#gird spacing is 50px, and 50px is 1 meter
body0 = Body(0,5)
body1 = Body(25,5)
body2 = Body(25,5,color="red",use_euler=True)
body_list = [body1, body2]
sim = Simulation()
sim.init_environment(body_list)  # creates body list for sim class
sim.show_environment()
#Runs after the simulation is closed
make_energy_graph(body_list)
