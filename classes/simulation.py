import pygame
import pygame.time
from classes.physics_engine import Physics
from classes.debug import Debugger


class Simulation:
    physics_engine = Physics()
    debug = Debugger()

    def __init__(self):
        screen_size = (1000, 800)
        self.run = None
        self.screen = pygame.display.set_mode(screen_size)
        self.bodies = None
        self.font = None
        self.clock = None

    def init_environment(self, body_list):
        self.bodies = body_list

        #starts pygame
        self.run = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)

        # pass body list to physics engine
        self.physics_engine.define_bodies(body_list)

    def write(self, text, location, color=(0, 0, 255)):
        self.screen.blit(self.font.render(text, True, color), location)

    def grid(self):
        for x in range(50, 1000, 50):
            pygame.draw.lines(self.screen, "gray", False, [(x, 0), (x, 800)])
        for y in range(50, 800, 50):
            pygame.draw.lines(self.screen, "gray", False, [(0, y), (1000, y)])

    #------------------------------------------------------------------------------------------------------
    def show_environment(self):
        previous_time = 0
        #creates a list to store energy data of pendulums,
        #the first element of each list will state if euler method was used
        energy_list = [[body.euler, body.E] for body in self.bodies]
        while self.run:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            #Initialize the screen space
            self.screen.fill((255, 255, 255))
            self.grid()
            self.write("Blue = velocity", (400, 100), (255, 255, 255))
            self.write("Green = Net force", (400, 125), (255, 255, 255))

            #calculate the net force of pendulum per frame
            net_force = self.physics_engine.compute_force_vectors()
            for i, body in enumerate(self.bodies):
                body.force = net_force[i]
            #draws the pendulum onto screen
            for body in self.bodies:
                body.draw(self.screen)
                # velocity
                velocity_txt = str.format('{0:.3f}', body.velocity * (body.length / 50)) + ' m/s'
                location = (body.position[0] + 20, body.position[1] + 20)
                self.write(velocity_txt, location)
                # force
                force_text = str.format('{0:.3f}', body.force)
                location2 = (body.position[0] + 20, body.position[1] + 40)
                self.write(force_text, location2, (0, 255, 0))
            #updates the position of pendulum
            #will use RK4 by default and switch to euler if set in body
            self.physics_engine.move_RK4(dt)
            #-------------------------------------------------------------------------------
            self.debug.debugger(self.clock)
            pygame.display.update()
            #stores energy of each pendulum each second
            current_time = pygame.time.get_ticks()
            if current_time - previous_time >= 1000:
                for i, body in enumerate(self.bodies):
                    energy_list[i].append(self.bodies[i].E)
                previous_time = current_time
                #print(energy_list)

        pygame.quit()

        # Save energy data to a file
        with open("energy_data.txt", "w") as file:
            for energy in energy_list:
                file.write(f"{energy}\n")

        print("Simulation ended. Energy data saved to energy_data.txt")
