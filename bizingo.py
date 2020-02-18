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
    def __init__(self):
        pass
        
    def drawUpsideTriangle(self, side, x, y, hasPiece):
        self.hasPiece = hasPiece
        self.side = side
        self.x = x
        self.y = y
        self.height = side * sqrt(3)/2
        self.endPoint = x + side
        self.upPointUpside = [(side/2) + x, y]
        self.leftPointUpside = [x, (self.height) + y]
        self.rightPointUpside = [(self.endPoint), (self.height) + y]
        # Primeiro ponto: acima
        # Segundo ponto: esquerda
        # Terceiro ponto: direita
        pygame.draw.polygon(screen, GREEN, [self.leftPointUpside, self.rightPointUpside, self.upPointUpside])

    def drawDownsideTriangle(self, side, x, y, hasPiece):
        self.hasPiece = hasPiece
        self.side = side
        self.x = x
        self.y = y
        self.height = side * sqrt(3)/2
        self.endPoint = x + side
        self.leftPointDownside = [x, y]
        self.rightPointDownside = [(self.endPoint), y]
        self.downPointDownside = [(side/2) + x, (self.height) + y]
        # Primeiro ponto: esquerda
        # Segundo ponto: direita
        # Terceiro ponto: abaixo
        pygame.draw.polygon(screen, WHITE, [self.leftPointDownside, self.rightPointDownside, self.downPointDownside])

    def drawPiece(self, piece, center):
        self.piece = piece
        self.center = center

        if piece == "black":
            pygame.draw.circle(screen, BLACK, [int(((self.side)/2) + self.x), int(((self.height)/self.center) + self.y)], 10)
        elif piece == "red":
            pygame.draw.circle(screen, RED, [int(((self.side)/2) + self.x), int(((self.height)/self.center) + self.y)], 10)
        elif piece == "blue":
            pygame.draw.circle(screen, BLUE, [int(((self.side)/2) + self.x), int(((self.height)/self.center) + self.y)], 10)
        elif piece == "yellow":
            pygame.draw.circle(screen, YELLOW, [int(((self.side)/2) + self.x), int(((self.height)/self.center) + self.y)], 10)
        else:
            pass

while not done:
    clock.tick(10)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
 
    screen.fill(GREY)

    w, h = 11, 11
    listTrianglesGreen = [[0 for x in range(w)] for y in range(h)]
    def lineGreen(x, y, quantity, side, wGreen):
        triangle = Triangle()
        for i in range(quantity):
            triangle.drawUpsideTriangle(side, x, y, False)
            x = x + side
            listTrianglesGreen[wGreen][i] = triangle

    listTrianglesWhite = [[0 for x in range(w)] for y in range(h)]
    def lineWhite(x, y, quantity, side, wWhite):
        triangle = Triangle()
        for i in range(quantity):
            triangle.drawDownsideTriangle(side, x, y, False)
            x = x + side
            listTrianglesWhite[wWhite][i] = triangle

    def drawBoardGreen():
        x = 300
        y = 225
        wGreen = 0
        for i in range(3, 12):
            lineGreen(x, y, i, 50, wGreen)
            x = x - 25
            y = y + (50 * sqrt(3)/2)
            wGreen += 1

        x = x + 50
        for i in range(10, 8, -1):
            lineGreen(x, y, i, 50, wGreen)
            x = x + 25
            y = y + (50 * sqrt(3)/2)
            wGreen += 1

    def drawBoardWhite():
        x = 325
        y = 225
        wWhite = 0
        for i in range(2, 12):
            lineWhite(x, y, i, 50, wWhite)
            x = x - 25
            y = y + (50 * sqrt(3)/2)
            wWhite += 1

        x = x + 50
        for i in range(10, 9, -1):
            lineWhite(x, y, i, 50, wWhite)
            x = x + 25
            y = y + (50 * sqrt(3)/2)
            wWhite += 1

    drawBoardGreen()
    drawBoardWhite()

    # def drawInitialBlackPieces():
    #     for i in range

    # triangle.drawPiece(piece, 1.5)
    # triangle.drawPiece(piece, 2.5)

    pygame.display.flip()
 
pygame.quit()

for line in listTrianglesGreen:
    for obj in line:
        if obj == 0:
            continue
        print(obj.hasPiece)