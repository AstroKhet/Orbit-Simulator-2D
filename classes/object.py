from classes.vector import Vector2D
from constants import WIN_HEIGHT

import pygame


class Object2D:
    # objects are all circular
    def __init__(self, name, mass, radius, scale, colour, position, velocity=Vector2D(0, 0), label=True):
        # Assumed to be constant
        self.name = name
        self.mass = mass
        self.radius = radius
        self.scale = scale
        self.colour = colour

        self.Position = position
        self.Velocity = velocity

        self.trajectory = []
        self.label = label

        # dynamic variables that cannot be set when instantiated
        self.SPACE_SCALE = None
        self.display_radius = None
        self.display_pos = None

    def initialize(self, SPACE_SCALE, SPACE_VECTOR):
        self.SPACE_SCALE = SPACE_SCALE
        self.display_radius = self.radius * self.scale / self.SPACE_SCALE
        self.display_pos = (1/SPACE_SCALE) * (SPACE_VECTOR + Vector2D(self.Position.x, WIN_HEIGHT*SPACE_SCALE - self.Position.y))

        if len(self.trajectory) > 12:
            del self.trajectory[0]

    def draw(self, window):
        x, y = self.display_pos.Args

        self.trajectory.append((x, y))

        for t in range(len(self.trajectory)):
            pygame.draw.circle(window, self.colour, self.trajectory[t], self.display_radius * (t+1)/12)

        pygame.draw.circle(window, self.colour, (x, y), self.display_radius)

