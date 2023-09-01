import pygame


class LedCreator:
    def __init__(self, position, idx, win, radius):
        self.position = position
        self.idx = idx
        self.win = win
        self.color = [100, 100, 100]
        self.radius = radius


    def draw(self):
        pygame.draw.circle(self.win, self.color, self.position, self.radius)

    


