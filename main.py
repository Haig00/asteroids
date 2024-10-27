import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

                  
    Asteroid.containers = (asteroids, updatable, drawable) 
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for up in updatable:
           up.update(dt)
        
        for ast in asteroids:
            if ast.collision(player):
                print("Game Over")
                sys.exit()
        
        for ast in asteroids:
            for shot in shots:
                if ast.collision(shot):
                    ast.split()
                    pygame.sprite.Sprite.kill(shot)


        screen.fill("black")
 
        for dr in drawable:
            dr.draw(screen)

        AsteroidField()
        
        
        
        pygame.display.flip()

        

        dt = clock.tick(60) / 1000
        


    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()