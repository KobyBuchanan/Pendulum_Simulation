import numpy as np


def _magnitude(arr): # not implemented
    return np.sqrt(arr[0] ** 2 + arr[1] ** 2)


def _unit_vector(arr): # not implemented
    mag = _magnitude(arr)
    return np.array([
        arr[0] / mag,
        arr[1] / mag
    ])


class Physics_engine:
    def __init__(self):
        self.body_pos = None
        self.body_list = None

    def define_bodies(self, body_list):
        self.body_list = [np.array([i, body]) for i, body in enumerate(body_list)]

    def compute_force_vectors(self):
        net_force = []
        for body in self.body_list:
            # force = -m * g * (s/l)
            #small angle approx make S = x-axis displacement
            new_force = -1 * 9.81 * (body[1].arc_displacement / body[1].rope_length) * np.array([1,-1]) # flips direction of vector to match pygame coordinates
            force = np.array([new_force[0],0])
            net_force.append(force)

        return net_force
