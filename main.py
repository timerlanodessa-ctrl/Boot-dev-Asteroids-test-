import pygame
from asteroid import Asteroid
from constants import *
from logger import log_event, log_state
from player import Player
from constants import *
from asteroidfield import AsteroidField
import sys
from logger import log_state
from shot import Shot









def main () :
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 

    

    Player.containers = (updatable, drawable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
       
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
        
           

    
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    dt = 0.0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
                
        for shot in shots:       
            for asteroid in asteroids:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
             
                
        log_state()
                
        screen.fill("black")
        
        for drw in drawable:
            drw.draw(screen)
            
            
        pygame.display.flip()
        
        dt = clock.tick (60) / 1000.0  # Delta time in seconds 
        
        
        

        
        
                
                
if __name__ == "__main__":
    main()
            
            


    
    
    








    
    