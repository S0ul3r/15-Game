import pygame

class Field:
    def __init__(self, x, y, width, height, number):
        self.obszar = pygame.Rect(x, y, width, height)
        self.liczba = number

    def isOver(self, x, y):
        if(x > self.obszar.left and x < self.obszar.right and 
        y > self.obszar.top and y < self.obszar.bottom):
            return True
        else:
            return False