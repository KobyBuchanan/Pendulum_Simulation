import pygame
import numpy as np

#constants
time_delay = 0.005


class Body:
    def __init__(self, center_position_array, radius):
        self.color = tuple(np.random.randint(0, 256, size=3))
        self.radius = radius
        self.thickness = self.radius * 2
        self.position = center_position_array
        self.velocity = np.array([0, 0])
        self.force = np.array([0, 0])
        self.rope_length = np.sqrt(
            (
                    (self.position[0] - 500) ** 2 + (self.position[1] - 200) ** 2
            )
        )
        self.arc_displacement = [(self.position[0] - 500), 0]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.position[0], self.position[1]), self.radius, self.thickness)
        pygame.draw.line(surface, self.color, (500, 200), (self.position[0], self.position[1]), 2)

    def move(self):
        self.velocity = self.velocity + ((self.force / 1) * time_delay)
        self.position = self.position + self.velocity * time_delay
        self.arc_displacement = [(self.position[0] - 500), 0]