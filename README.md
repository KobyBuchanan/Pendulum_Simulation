# Pendulum_Simulation

A pendulum simulation made using the Pygame package. This is an intial project in a series of projects in which I will make physics based particle simulations.
The current physics engine assumes the small angle approximation for the pendulums, I will be making the physics engine more advanced in future builds.


## Energy Plot
A graph to showcase the difference between the RK4 and Euler methods. The Euler method is largely unstable and allows the energy to vary due to confounding rounding errors. The RK4 method minimizes this error. 

![energy plot](Pendulum_Simulation/energy_vs_time.png)


# Planned changes
- Visual upgrade to the graphics and GUI elements
- User input controls 
- True pendulum behavior (string with mass, stiffness, etc.) and allowing damping and driving forces
- Double pendulum and coupled pendula
- possible addition of pendulumn in a fluid