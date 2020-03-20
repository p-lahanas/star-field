import pygame
from star import Star

WIN_WIDTH = 800
WIN_HEIGHT = 800
run = True

display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
stars = []

for i in range(0,300):
    stars.append(Star(WIN_WIDTH, WIN_HEIGHT))



while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill((0,0,0))

    for star in stars:
        star.update()
        star.draw(display)
        
    pygame.display.update()


pygame.quit()