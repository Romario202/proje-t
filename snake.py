import pygame

red = (225, 0, 0)
green = (0, 225, 0)
blue = (0, 0, 225)
white = (225, 225, 225)

x, y = 0, 0

surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Game")

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

