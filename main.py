import numpy as np
from Pendulum_Simulation.classes.body import Body
from Pendulum_Simulation.classes.simulation import Simulation

# Intiialize the Pendulums with a starting coordinate and size
body1 = Body(np.array([500, 400]), 5)
body2 = Body(np.array([600, 500]), 5)
body3 = Body(np.array([650, 600]), 5)
body4 = Body(np.array([700, 700]), 5)

sim = Simulation()
sim.init_environment([body1,body2,body3,body4])  # creates body list for sim class
sim.show_environment()