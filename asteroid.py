from circleshape import CircleShape
from constants import *
import pygame
import random as rand

class Asteroid (CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            print('triggered')
            return
        
        else:
        
            rot = rand.uniform(20,50)

            v1 = self.velocity.rotate(rot)
            v2 = self.velocity.rotate(-rot)

            newRad = self.radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, newRad)
            a2 = Asteroid(self.position.x, self.position.y, newRad)

            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
