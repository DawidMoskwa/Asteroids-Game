import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS  # explicit imports
from circleshape import CircleShape  # Import CircleShape first
from player import Player  # Import Player after CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Shot.containers = (shot, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                print ("Game Over!")
                sys.exit()
            for bullets in shot:
                if bullets.collisions(asteroid):
                    bullets.kill()
                    asteroid.split(asteroid.radius, asteroids, updatable, drawable)

        pygame.Surface.fill(screen, "black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":

    main()