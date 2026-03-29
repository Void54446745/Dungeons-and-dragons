#
import pygame
from os.path import join
import random

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
pygame.display.set_caption('Space ship game')

# Surface
surf = pygame.Surface((100, 200))
surf.fill('BlueViolet')
x = 100

# Import an image

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range (20)]
# Stars


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    screen.fill('DarkGrey')
    for pos in star_positions:
        screen.blit(star_surf, pos)
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left += 0.2
    screen.blit(player_surf, player_rect)
    pygame.display.update()

pygame.quit()
