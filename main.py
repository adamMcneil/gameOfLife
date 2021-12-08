import pygame

pygame.init()

screenWidth = 1000
screenHeight = 1000
white = (255, 255, 255)

screen = pygame.display.set_mode((screenWidth, screenHeight))
size = 10


running = True
while running:
    events = pygame.event.get()
    screen.fill(white)
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
