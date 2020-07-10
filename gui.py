import pygame
import sys
from pygame.locals import *
from field import *
from game import *
from locals import *


class Gui:
    def __init__(self):
        pygame.init()
        self.game = Game(BOARDWIDTH, BOARDHEIGHT)
        self.win = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption("15")
        self.font = pygame.font.Font('C:/Users/jakub/Desktop/gra 2/frog.ttf', 32)
        self.fields = []
        for i in range(BOARDHEIGHT):
            row = []
            for j in range(BOARDWIDTH):
                field = Field(XMARGIN + j*FIELDSIZE, YMARGIN + i*FIELDSIZE,
                FIELDSIZE, FIELDSIZE, i*BOARDWIDTH + j + 1)
                row.append(field)
            self.fields.append(row)
        self.newgame = Field(WINDOWWIDTH - 170, WINDOWHEIGHT -200, 160, 60, 'New Game')
        self.reset = Field(WINDOWWIDTH - 170, WINDOWHEIGHT -135, 160, 60, 'Reset')
        self.solve = Field(WINDOWWIDTH - 170, WINDOWHEIGHT -70, 160, 60, 'Solve')

    def drawnew(self):
        napis = self.font.render(self.newgame.liczba, True, FONTCOLOR)
        kwadrat = napis.get_rect()
        kwadrat.center = self.newgame.obszar.center
        self.win.blit(napis, kwadrat)
        pygame.draw.rect(self.win, FIELDCOLOR, self.newgame.obszar)
        pygame.draw.rect(self.win, FIELDFRAME, self.newgame.obszar, 1)
        self.win.blit(napis, kwadrat)

        napis = self.font.render(self.reset.liczba, True, FONTCOLOR)
        kwadrat = napis.get_rect()
        kwadrat.center = self.reset.obszar.center
        self.win.blit(napis, kwadrat)
        pygame.draw.rect(self.win, FIELDCOLOR, self.reset.obszar)
        pygame.draw.rect(self.win, FIELDFRAME, self.reset.obszar, 1)
        self.win.blit(napis, kwadrat)

        napis = self.font.render(self.solve.liczba, True, FONTCOLOR)
        kwadrat = napis.get_rect()
        kwadrat.center = self.solve.obszar.center
        self.win.blit(napis, kwadrat)
        pygame.draw.rect(self.win, FIELDCOLOR, self.solve.obszar)
        pygame.draw.rect(self.win, FIELDFRAME, self.solve.obszar, 1)
        self.win.blit(napis, kwadrat)
        
    def draw(self):
        self.win.fill(BGCOLOR)
        
        for i in range(BOARDHEIGHT):
            for j in range(BOARDWIDTH):
                if(self.game.fields[i][j] != BOARDWIDTH * BOARDHEIGHT):
                    pygame.draw.rect(self.win, FIELDCOLOR, self.fields[i][j].obszar)
                    liczba = self.font.render(str(self.fields[i][j].liczba), True, FONTCOLOR)
                    kwadrat = liczba.get_rect()
                    kwadrat.center = self.fields[i][j].obszar.center
                    self.win.blit(liczba, kwadrat)
                pygame.draw.rect(self.win, FIELDFRAME, self.fields[i][j].obszar, 1)
        self.drawnew()
        pygame.display.update()
    
    def handelEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                what = self.overWhat(x,y)
                print(what)
                if(what == 'newgame'):
                    self.game.newGame()
                    self.game.randomPath()
                elif(what == 'reset'):
                    self.game.newGame()
                elif(what == 'solve'):
                    while(len(self.game.moves) > 0):
                        time.sleep(0.4)
                        self.game.reverseOne()
                        self.update()
                        self.draw()

                elif(what == ' '):
                    continue
                else:
                    self.game.move(*what)
    
    def update(self):
        for i in range(BOARDHEIGHT):
            for j in range(BOARDWIDTH):
                self.fields[i][j].liczba = self.game.fields[i][j]
        
    def play(self):
        while True:
            self.handelEvent()
            self.update()
            self.draw()
    
    def overWhat(self, x, y):
        for i in range(BOARDWIDTH):
            for j in range(BOARDHEIGHT):
                if self.fields[i][j].isOver(x, y):
                    return (i, j)
        if self.newgame.isOver(x, y):
            return 'newgame'
        elif self.solve.isOver(x, y):
            return 'solve'
        elif self.reset.isOver(x, y):
            return 'reset'
        else:
            return ' '