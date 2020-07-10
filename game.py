import random
import time

LEFT = "left"
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

class Game:
    
    def __init__(self , width, height) :
        self.width = width
        self.height = height
        self.randomize = 80
        self.moves = []
        self.fields = []
        for i in range(1, height+1):
            row = []
            for j in range(1, width+1):
                row.append((i-1) * width + j)
            self.fields.append(row)
        
        
    def __str__(self):
        s = ""
        for i in self.fields:
            pom = "["
            for j in i:
                pom += " "
                pom += str(j)
            pom += "]\n"
            s += pom
        return s

    def findVoid(self):
        for i in range(self.width):
            for j in range(self.height):
                if(self.fields[j][i] == self.width * self.height):
                    return (j, i)
    
    def inside(self, x, y):
        if(x >= 0 and x < self.height and y >= 0 and y < self.width):
            return True
        else:
            return False
############   MOVING FIELDS  FUNCTIONS  ######################
    def up(self, x, y):
        if(self.inside(x, y) and (x - 1, y) == self.findVoid()):
            return True
        else:
            return False
    def down(self, x, y):
        if(self.inside(x, y) and (x + 1, y) == self.findVoid()):
            return True
        else:
            return False
    
    def left(self, x, y):
        if(self.inside(x, y) and (x, y - 1) == self.findVoid()):
            return True
        else:
            return False
    
    def right(self, x, y):
        if(self.inside(x, y) and (x, y + 1) == self.findVoid()):
            return True
        else:
            return False
    
    def canMove(self, x, y):
        if (self.right(x,y) or self.left(x,y) or self.up(x,y) or self.down(x,y)):
            return True
        else:
            return False

    def move(self, x, y):
        if(self.up(x, y)):
            self.fields[x][y], self.fields[x-1][y] = self.fields[x-1][y], self.fields[x][y]
            self.moves.append(DOWN)
        elif(self.down(x, y)):
            self.fields[x][y], self.fields[x+1][y] = self.fields[x+1][y], self.fields[x][y]
            self.moves.append(UP)
        elif(self.left(x, y)):
            self.fields[x][y], self.fields[x][y-1] = self.fields[x][y-1], self.fields[x][y]
            self.moves.append(RIGHT)
        elif(self.right(x, y)):
            self.fields[x][y], self.fields[x][y+1] = self.fields[x][y+1], self.fields[x][y]
            self.moves.append(LEFT)
        else:
            print("Tego punktu nie mozesz przesunac")
#################################################################################################
    def handleEvent(self):
        x, y = map(int, input("Podaj wspolrzedne punktu ktory chcesz przesunac: ").split())
        self.move(x-1, y-1)
    
    def play(self):
        self.randomPath()
        print(str(self))
        while True:
            self.handleEvent()           
            print(self.voidOptions())
            print(str(self))


################  MOVING VOID FIELD FUNCTIONS  ##############################################

    def voidOptions(self):
        directions = []
        x, y = self.findVoid()
        if(self.up(x + 1, y)):
            directions.append(DOWN)
        if(self.down(x - 1, y)):
            directions.append(UP)
        if(self.left(x, y + 1)):
            directions.append(RIGHT)
        if(self.right(x, y - 1)):
            directions.append(LEFT)
        return directions

    def voidUp(self):
        x, y = self.findVoid()
        self.move(x - 1, y)
        
    def voidDown(self):
        x, y = self.findVoid()
        self.move(x + 1, y)

    def voidLeft(self):
        x, y = self.findVoid()
        self.move(x, y - 1)

    def voidRight(self):
        x, y = self.findVoid()
        self.move(x, y + 1)

#######################################################################

    def opposite(self, choice):
        if choice == UP:
            return DOWN
        elif choice == DOWN:
            return UP
        elif choice == LEFT:
            return RIGHT
        elif choice == RIGHT:
            return LEFT 

    def randomPath(self):
        for i in range(self.randomize):
            choice = random.choice(self.voidOptions())
            while(not (len(self.moves) == 0 or self.moves[-1] != self.opposite(choice))):
                choice = random.choice(self.voidOptions())
            print(choice)
            if choice == 'up':
                self.voidUp()
            elif choice == 'down':
                self.voidDown()
            elif choice == 'left':
                self.voidLeft()
            elif choice == 'right':
                self.voidRight()
            

    def reverseOne(self):
        if(len(self.moves) > 0):
            print(self.moves)
            move = self.moves.pop()
            if(move == UP):
                self.voidDown()
            elif(move == DOWN):
                self.voidUp()
            elif(move == LEFT):
                self.voidRight()
            elif(move == RIGHT):
                self.voidLeft()
            self.moves.pop()
    
    def newGame(self):
        self.moves = []
        for i in range(self.height):
            for j in range(self.width):
                self.fields[i][j] = j + 1 + i * (self.width)
        
    def reverseAll(self):
        print(self.moves)
        while(len(self.moves) > 0):
            time.sleep(2)
            print(str(self))
            self.reverseOne()
        print(str(self)) 