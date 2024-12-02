import pygame
import numpy as np
import math

class Body:
    anchor = pygame.math.Vector2(500, 200)

    def __init__(self, angle, length, radius=10, velocity=None):
        self.color = tuple(np.random.randint(0, 256, size=3))
        self.angle = angle * np.pi / 180
        self.length = length
        self.radius = radius
        self.thickness = self.radius * 2
        self.position = self.anchor + (self.length * pygame.Vector2(math.sin(self.angle), math.cos(self.angle)))
        self.velocity = 0
        self.force = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, self.thickness)
        pygame.draw.line(surface, (0, 0, 0), self.anchor, self.position, self.radius // 2)

    def move(self, delta_time):
        self.velocity = self.velocity + (self.force/self.length) * delta_time
        self.angle = self.angle + self.velocity * delta_time
        self.position = self.anchor + (self.length * pygame.Vector2(math.sin(self.angle), math.cos(self.angle)))