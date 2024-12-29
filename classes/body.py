import math
import pygame
import numpy as np


class Body:
    anchor = pygame.math.Vector2(500, 200)

    def __init__(self, angle, length, radius=10, color=tuple(np.random.randint(0, 256, size=3)), use_euler=False, velocity=None):
        self.color = color
        self.angle = angle * math.pi / 180
        self.length = length * 50
        self.radius = radius
        self.thickness = self.radius * 2
        self.position = self.anchor + (self.length * pygame.Vector2(math.sin(self.angle), math.cos(self.angle)))
        self.velocity = 0
        self.force = 0
        self.euler = use_euler
        self.K = 0.5 * (self.velocity * (self.length / 50)) ** 2
        self.U = 9.81 * (self.length / 50) * (1 - math.cos(self.angle))
        self.E = self.K + self.U

    def draw(self, surface):
        pygame.draw.line(surface, (0, 0, 0), self.anchor, round(self.position), self.radius // 2)
        pygame.draw.circle(surface, self.color, round(self.position), self.radius, self.thickness)


