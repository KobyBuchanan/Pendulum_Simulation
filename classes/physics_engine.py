import numpy as np
import math
import pygame

class Physics:
    def __init__(self):
        self.body_pos = None
        self.body_list = None

    def define_bodies(self, body_list):
        self.body_list = [np.array([i, body]) for i, body in enumerate(body_list)]

    def compute_force_vectors(self):
        net_force = []
        for body in self.body_list:
            # force = -m * g * sin(theta)
            force = -1 * 9.81 * math.sin(body[1].angle)
            net_force.append(force)
        return net_force
#-------------------RK4 Method-------------------------------
    def move_RK4(self, delta_time):
        for body in self.body_list:
            if body[1].euler:
                move(body[1], delta_time)
            else:
                const = -9.81 / body[1].length * 50  # convert to meters
                k1 = body[1].velocity * delta_time
                l1 = const * math.sin(body[1].angle) * delta_time
                k2 = (body[1].velocity + (.5 * l1)) * delta_time
                l2 = const * math.sin(body[1].angle + (.5 * k1)) * delta_time
                k3 = (body[1].velocity + (.5 * l2)) * delta_time
                l3 = const * math.sin(body[1].angle + (.5 * k2)) * delta_time
                k4 = (body[1].velocity + l3) * delta_time
                l4 = const * math.sin(body[1].angle + k3) * delta_time
                body[1].velocity = body[1].velocity + ((l1 + 2 * l2 + 2 * l3 + l4) / 6)
                body[1].angle = body[1].angle + ((k1 + 2 * k2 + 2 * k3 + k4) / 6)
                body[1].K = 0.5 * (body[1].velocity * (body[1].length / 50)) ** 2
                body[1].U = 9.81 * (body[1].length / 50) * (1 - math.cos(body[1].angle))
                body[1].E = body[1].K + body[1].U
                body[1].position = (
                        body[1].anchor + (
                            body[1].length * pygame.Vector2(math.sin(body[1].angle), math.cos(body[1].angle))))

#-----------Euler Method--------------------------------
def move(body, delta_time):
    body.velocity = body.velocity + ((body.force / body.length) * delta_time * 50)  # angular velocity
    body.angle = body.angle + (body.velocity * delta_time)
    body.K = 0.5 * (body.velocity * (body.length / 50)) ** 2
    body.U = 9.81 * (body.length / 50) * (1 - math.cos(body.angle))
    body.E = body.K + body.U
    body.position = body.anchor + (body.length * pygame.Vector2(math.sin(body.angle), math.cos(body.angle)))
