import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
import pygame
from logger import log_event



class Asteroid(CircleShape):
    
    def __init__(self, x , y, radius) -> None:
        super().__init__( x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle( screen, "white", self.position, self.radius, LINE_WIDTH)
        



    def update(self, dt: float) -> None:
       
       self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            random_uniform = random.uniform(20, 50)
            velocity = self.velocity.rotate(random_uniform)
            velocity2 = self.velocity.rotate(-random_uniform)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity * 1.2 
            new_asteroid2.velocity = velocity2 * 1.2
            