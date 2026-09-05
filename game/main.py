# Imports pygame modual
import sys
import pygame

# Initalises pygame
pygame.init()

# Sets up window with dimensions
width = 1400
height = 900
screen = pygame.display.set_mode((width, height))

# Sets window caption
pygame.display.set_caption("Air Combat Comand")

# Sets running to true to keep track of when to close game
running = True

# while loop will end when user choses to close game
while running:
    
    # listens for user input
    for event in pygame.event.get():

        # Check if the user clicked X button
        
        if event.type == pygame.QUIT:

            running = False
# Cleanly closes game
pygame.quit()
sys.exit()