#
import pygame 

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
y = 150

# Import an image

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    screen.fill('DarkGrey')
    x += 0.1
    screen.blit(surf, (x, y))
    pygame.display.update()

pygame.quit()
