import numpy as np



class Physics_engine:
    def __init__(self):
        self.body_pos = None
        self.body_list = None

    def define_bodies(self, body_list):
        self.body_list = [np.array([i, body]) for i, body in enumerate(body_list)]

    def compute_force_vectors(self):
        net_force = []
        for body in self.body_list:
            # force = -m * g * sin(angle)
            force = -1 * 9.81 * np.sin(body[1].angle)
            net_force.append(force)

        return net_force
