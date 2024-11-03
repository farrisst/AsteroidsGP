import pygame
from constants import *
from player import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0  

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.Containers = (updateable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             return
            
        screen.fill(BLACK)
        
        for i in drawable:
            i.draw(screen)

        for i in updateable:
           i.update(dt)


        player.draw(screen)
        player.update(dt)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()