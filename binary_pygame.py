import binary_tree
import pygame
wn = pygame.display.set_mode((500,400))
wn.fill((255,255,255))
pygame.display.flip()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (248, 184, 120)
RED = (255, 0, 0)

state = True
while state: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    

