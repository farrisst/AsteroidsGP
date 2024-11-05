import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             return
            
        screen.fill(BLACK)
        
        for i in drawable:
            i.draw(screen)

        for i in updateable:
           i.update(dt)

        for i in asteroids:
           if i.collision(player):
              print('Game Over!')
              pygame.quit()

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()