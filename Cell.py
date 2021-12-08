import pygame
import random


class Cell:
    green = (50, 255, 50)
    red = (255, 50, 50)

    def __init__(self, location, size, alive):
        self.alive_color = (0, 0, 0)
        self.dead_color = (255, 255, 255)
        self.alive = alive
        self.location = location
        self.size = size
        self.index = (location[0] // size, location[1] // size)
        self.shape = pygame.Rect(location[0], location[1], size, size)

    def print_cell(self, screen):
        if self.alive:
            # self.set_random_color()
            # self.set_random_color()
            pygame.draw.rect(screen, self.alive_color, self.shape, 0, 0)
        else:
            pygame.draw.rect(screen, self.dead_color, self.shape, 0, 0)

    def set_random_color(self):
        top = 255
        bottom = 50
        self.alive_color = (random.randint(bottom, top), random.randint(bottom, top), random.randint(bottom, top))

    def check(self, cells):
        num = self.get_num_of_alive_neighbors(cells)
        if num == 3:
            self.set_random_color()
            self.alive = True
        if num < 2 or num > 3:
            self.alive = False

    def color_check(self, cells):
        num = self.get_num_of_alive_neighbors(cells)
        if num == 3:
            self.alive = True
            self.alive_color = self.green
            return
        if num < 2 or num > 3:
            self.alive = False
        self.alive_color = self.red

    def get_num_of_alive_neighbors(self, cells):
        check_nums = [[-1, -1],
                      [-1, 0],
                      [-1, 1],
                      [0, -1],
                      [0, 1],
                      [1, -1],
                      [1, 0],
                      [1, 1]
                      ]
        count = 0
        for pair in check_nums:
            x = self.index[0] + pair[0]
            y = self.index[1] + pair[1]
            if (0 <= (self.index[0] + pair[0]) < len(cells)) and (0 <= (self.index[1] + pair[1]) < len(cells[0])):

                if cells[self.index[0] + pair[0]][self.index[1] + pair[1]].alive:
                    count += 1
        return count
