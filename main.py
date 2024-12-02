import numpy as np
from classes.body import Body
from classes.simulation import Simulation

# Intiialize the Pendulums with a starting angle and length of rope
body1 = Body(0, 100)
body2 = Body(25, 100)
body3 = Body(45, 500)
body4 = Body(-25, 550)

sim = Simulation()
sim.init_environment([body1, body2,body3,body4])  # creates body list for sim class
sim.show_environment()