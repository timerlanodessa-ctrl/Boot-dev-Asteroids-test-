import pygame
from constants import *
from logger import log_state







def main () :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    dt = 0.0
    clock = pygame.time.Clock()
    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick (60) / 1000.0  # Delta time in seconds 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
                
if __name__ == "__main__":
    main()
            
            


    
    
    





def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
    
    