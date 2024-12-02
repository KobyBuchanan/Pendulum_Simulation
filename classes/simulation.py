import pygame
import time
from classes.physics_engine import Physics_engine
from debug import Debugger


class Simulation:
    physics_engine = Physics_engine()
    debug = Debugger()

    def __init__(self):
        self.run = None
        self.screen = None
        self.bodies = None
        self.font = None
        self.clock = None

    def init_environment(self, body_list):
        self.bodies = body_list
        screen_size = (1000, 800)
        self.run = True

        #starts pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)

        #display window
        self.screen = pygame.display.set_mode(screen_size)
        #clock
        self.clock = pygame.time.Clock()
        # pass body list to physics engine
        self.physics_engine.define_bodies(body_list)

    def write(self, text, location, color=(0, 0, 255)):
        self.screen.blit(self.font.render(text, True, color), location)

    def show_environment(self):
        while self.run:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.screen.fill((255, 255, 255))

            net_force = self.physics_engine.compute_force_vectors()

            
            pygame.draw.rect(self.screen, "black", (0, 0, 1000, 200), )
            self.write("Blue = velocity", (400, 100), (255, 255, 255))
            self.write("Green = Net force", (400, 125), (255, 255, 255))

            for i, body in enumerate(self.bodies):
                body.force = net_force[i]

            for body in self.bodies:
                body.draw(self.screen)
                # velocity
                text = str.format('{0:.3f}', body.velocity)
                location = (body.position[0] + 20, body.position[1] + 20)
                self.write(text, location)
                # force
                text2 = str.format('{0:.3f}', body.force)
                location2 = (body.position[0] + 20, body.position[1] + 60)
                self.write(text2, location2, (0, 255, 0))

            for body in self.bodies:
                body.move(dt)

            self.debug.debugger(dt)
            pygame.display.update()
            
