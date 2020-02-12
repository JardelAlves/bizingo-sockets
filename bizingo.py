import pygame
from math import sqrt
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
GREY   = (225, 225, 225)
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)
GREEN  = (  0, 255,   0)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)
 
# Set the height and width of the screen
size = [1280, 960]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# This draws a triangle using the polygon command
class Triangle():
    def __init__(self):
        pass
        
    def drawUpsideTriangle(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y
        self.height = side * sqrt(3)/2
        self.endPoint = x + side
        # Primeiro ponto: acima
        # Segundo ponto: esquerda
        # Terceiro ponto: direita
        pygame.draw.polygon(screen, GREEN, [[(side/2) + x, y], [x, (self.height) + y], [(self.endPoint), (self.height) + y]])

    def drawDownsideTriangle(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y
        self.height = side * sqrt(3)/2
        self.endPoint = x + side
        # Primeiro ponto: esquerda
        # Segundo ponto: direita
        # Terceiro ponto: abaixo
        pygame.draw.polygon(screen, BLACK, [[x, y], [(self.endPoint), y], [(side/2) + x, (self.height) + y]])

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

    def lineGreen(x, y, quantity, side, piece):
        triangle = Triangle()
        for i in range(quantity):
            triangle.drawUpsideTriangle(side, x, y)
            triangle.drawPiece(piece, 1.5)
            x = x + side

    def lineWhite(x, y, quantity, side, piece):
        triangle = Triangle()
        for i in range(quantity):
            triangle.drawDownsideTriangle(side, x, y)
            triangle.drawPiece(piece, 2.5)
            x = x + side

    def drawBoardGreen():
        x = 350
        y = 100
        for i in range(3, 12):
            lineGreen(x, y, i, 50, "red")
            x = x - 25
            y = y + (50 * sqrt(3)/2)

        x = x + 50
        for i in range(10, 8, -1):
            lineGreen(x, y, i, 50, "red")
            x = x + 25
            y = y + (50 * sqrt(3)/2)

    def drawBoardWhite():
        x = 375
        y = 100
        for i in range(2, 12):
            lineWhite(x, y, i, 50, "blue")
            x = x - 25
            y = y + (50 * sqrt(3)/2)

        x = x + 50
        for i in range(10, 9, -1):
            lineWhite(x, y, i, 50, "blue")
            x = x + 25
            y = y + (50 * sqrt(3)/2)

    drawBoardGreen()

    drawBoardWhite()
    pygame.display.flip()
 
pygame.quit()