import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS =30
# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#setup assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")


class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"sprite.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (int(WIDTH / 2), int(HEIGHT / 2))
        self.y_speed = 5
        self.x_speed = 5
    
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

        
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# game loop
running = True
# keep loop running at the right speed
while running:
    clock.tick(FPS)
    # Process input (events)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *After* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()