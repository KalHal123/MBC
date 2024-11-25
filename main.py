import time
from time import sleep as sl
import random
import pygame
import os
import base64

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Template")

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Main game loop
def main():
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit the game
                running = False
        
        # Update game logic
        # (Add your game updates here)
        
        # Draw everything
        screen.fill(WHITE)  # Clear the screen
        # (Add your drawing code here)
        
        pygame.display.flip()  # Update the display
        
        # Cap the frame rate
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
