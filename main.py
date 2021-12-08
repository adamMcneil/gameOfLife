import pygame
import Cell
import time
import random

pygame.init()

screenWidth = 1000
screenHeight = 1000
white = (255, 255, 255)

screen = pygame.display.set_mode((screenWidth, screenHeight))
size = 10
cells = []
for x in range(0, screenWidth, size):
    row = []
    cells.append(row)
    for y in range(0, screenHeight, size):
        cell = Cell.Cell([x, y], size, False)
        rand_num = random.randint(0,1)
        if rand_num == 1:
            cell.alive = True
        else:
            cell.alive = False
        cells[x//size].append(cell)
# cells[50][50].alive = True
# cells[51][51].alive = True
# cells[51][52].alive = True
# cells[50][52].alive = True
# cells[49][52].alive = True

# print(cells)


def copy_cells(cells):
    copy = []
    for rows in cells:
        row = []
        copy.append(row)
        for cell in rows:
            copy_cell = Cell.Cell(cell.location, cell.size, cell.alive)
            row.append(copy_cell)
    return copy


running = True
while running:
    events = pygame.event.get()
    # screen.fill(white)
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    copy = copy_cells(cells)
    # print(type(copy))
    # print(type(copy[0]))
    # print(type(copy[0][0]))
    for row in cells:
        for cell in row:
            cell.print_cell(screen)
            cell.check(copy)
            # print(cell.alive)

    pygame.display.update()
    time.sleep(0)
