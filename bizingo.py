import pygame
from math import sqrt
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [1280, 960]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # This draws a triangle using the polygon command
    def drawTriangle(side, initialPoint, quantity):
        height = side*sqrt(3)/2
        # Primeiro ponto: acima
        # Segundo ponto: esquerda
        # Terceiro ponto: direita
        pygame.draw.polygon(screen, BLACK, [[quantity*(side/2), initialPoint], [(quantity*initialPoint), height], [(quantity*side), height]])

    for i in range (1, 3):
        anotherPoint = 100 * i
        drawTriangle(100, anotherPoint, i)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()