import pygame
from math import sqrt
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
GREY   = (200, 200, 200)
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)
GREEN  = ( 25, 255,  50)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)
 
# Set the height and width of the screen
size = [1280, 960]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bizingo")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# This draws a triangle using the polygon command
class Triangle():
    def __init__(self, side):
        self.side = side
        self.height = side * sqrt(3)/2
        pass
        
    def drawUpsideTriangle(self, x, y, hasPiece):
        self.x = x
        self.y = y
        self.hasPiece = hasPiece
        endPoint = x + self.side
        upPointUpside = [(self.side/2) + x, y]
        leftPointUpside = [x, (self.height) + y]
        rightPointUpside = [(endPoint), (self.height) + y]
        # Primeiro ponto: acima
        # Segundo ponto: esquerda
        # Terceiro ponto: direita
        pygame.draw.polygon(screen, GREEN, [leftPointUpside, rightPointUpside, upPointUpside])

    def drawDownsideTriangle(self, x, y, hasPiece):
        self.x = x
        self.y = y
        self.hasPiece = hasPiece
        endPoint = x + self.side
        leftPointDownside = [x, y]
        rightPointDownside = [(endPoint), y]
        downPointDownside = [(self.side/2) + x, (self.height) + y]
        # Primeiro ponto: esquerda
        # Segundo ponto: direita
        # Terceiro ponto: abaixo
        pygame.draw.polygon(screen, WHITE, [leftPointDownside, rightPointDownside, downPointDownside])

    def drawPiece(self, piece, center):
        self.piece = piece

        if piece == "black":
            pygame.draw.circle(screen, BLACK, [int(((self.side)/2) + self.x), int(((self.height)/center) + self.y)], 10)
        elif piece == "red":
            pygame.draw.circle(screen, RED, [int(((self.side)/2) + self.x), int(((self.height)/center) + self.y)], 10)
        elif piece == "blue":
            pygame.draw.circle(screen, BLUE, [int(((self.side)/2) + self.x), int(((self.height)/center) + self.y)], 10)
        elif piece == "yellow":
            pygame.draw.circle(screen, YELLOW, [int(((self.side)/2) + self.x), int(((self.height)/center) + self.y)], 10)
        else:
            pass

    def drawButtonGreen(self, side):
        height = side * sqrt(3)/2
        heightRec = height*2/3
        widthRec = (heightRec/height)*(side/2)

        # pygame.draw.rect(screen, BLACK, (300 + ((50-widthRec)/2), 240, widthRec, heightRec), 0)

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                print("True")
            
        print("False")

class Board():
    def __init__(self, w, h, side):
        self.listTrianglesGreen = [[0 for x in range(w)] for y in range(h)]
        self.listTrianglesWhite = [[0 for x in range(w)] for y in range(h)]
        self.side = side

    def lineGreen(self, x, y, quantity, wGreen):
        self.wGreen = wGreen

        triangle = Triangle(self.side)
        for i in range(quantity):
            triangle.drawUpsideTriangle(x, y, True)
            x = x + self.side
            self.listTrianglesGreen[self.wGreen][i] = triangle
            triangle.drawPiece("black", 1.5)

    def lineWhite(self, x, y, quantity, wWhite):
        self.wWhite = wWhite

        triangle = Triangle(self.side)
        for i in range(quantity):
            triangle.drawDownsideTriangle(x, y, False)
            x = x + self.side
            self.listTrianglesWhite[self.wWhite][i] = triangle
            triangle.drawPiece("red", 2.5)

    def drawBoardGreen(self, x, y):
        self.wGreen = 0
        for i in range(3, 12):
            self.lineGreen(x, y, i, self.wGreen)
            x = x - (self.side/2)
            y = y + (self.side * sqrt(3)/2)
            self.wGreen += 1

        x = x + self.side
        for i in range(10, 8, -1):
            self.lineGreen(x, y, i, self.wGreen)
            x = x + (self.side/2)
            y = y + (self.side * sqrt(3)/2)
            self.wGreen += 1

    def drawBoardWhite(self, x, y):
        self.wWhite = 0
        for i in range(2, 12):
            self.lineWhite(x, y, i, self.wWhite)
            x = x - (self.side/2)
            y = y + (self.side * sqrt(3)/2)
            self.wWhite += 1

        x = x + self.side
        for i in range(10, 9, -1):
            self.lineWhite(x, y, i, self.wWhite)
            x = x + (self.side/2)
            y = y + (self.side * sqrt(3)/2)
            self.wWhite += 1

while not done:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
 
    screen.fill(GREY)

    board = Board(11, 11, 50)
    board.drawBoardGreen(300, 225)
    board.drawBoardWhite(325, 225)

    pygame.display.flip()
 
pygame.quit()

for line in board.listTrianglesGreen:
    for obj in line:
        if obj == 0:
            continue
        print(obj.hasPiece)