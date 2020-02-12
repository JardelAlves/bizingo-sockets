import pygame
from math import sqrt
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
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
        pygame.draw.polygon(screen, GREEN, [[(side/2)+x, y], [x, (self.height) + y], [(self.endPoint), (self.height) + y]])

    def drawPiece(self, piece):
        self.piece = piece
        if piece == "black":
            pygame.draw.circle(screen, BLACK, [int(((self.side)/2) + self.x), int((self.height)/1.5)], 40)
        elif piece == "red":
            pygame.draw.circle(screen, RED, [int(((self.side)/2) + self.x), int((self.height)/1.5)], 40)
        elif piece == "blue":
            pygame.draw.circle(screen, BLUE, [int(((self.side)/2) + self.x), int((self.height)/1.5)], 40)
        elif piece == "yellow":
            pygame.draw.circle(screen, YELLOW, [int(((self.side)/2) + self.x), int((self.height)/1.5)], 40)
        else:
            pass
        
while not done:
 
    clock.tick(10)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
 
    screen.fill(WHITE)

    x0 = 0
    y0 = 0

    triangle = Triangle()
    # triangle.drawUpsideTriangle(200, 200, y0)
    # triangle.drawPiece("yellow")
    for i in range(3):
        triangle.drawUpsideTriangle(200, x0, y0)
        triangle.drawPiece("yellow")
        x0 = x0 + 200

    pygame.display.flip()
 
pygame.quit()