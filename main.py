# Written by: Nico Santos
# From: Adelaide, South Australia

import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')

# Size of tile in the map
tile_size = 50

# Load image moon
moon_img = pygame.image.load('Graphics/pixel_moon.jpg')
moon_img = pygame.transform.scale(moon_img, (200,200))

# Load image background
background_img = pygame.image.load('Graphics/dark_background.png')
background_img = pygame.transform.scale(background_img, (1000,1000))

def show_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size,0), (line * tile_size, screen_height))

class World():
    def __init__(self, data):
        self.tile_list = []


        # Load image for platform
        floor_img = pygame.image.load('Graphics/dirt.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(floor_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.y = row_count * tile_size
                    img_rect.x = col_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


# This is the map, indicates the number of the chosen image to show based on numbers.
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
[1, 7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 7, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

world = World(world_data)
# Variable controller for the program to run, Returns
# Returns true if the game is still run and False if the game will end
run = True

# Loop to keep the game running. Will quit depending on the player's choice
while run:

    screen.blit(background_img, (0,0))
    screen.blit(moon_img, (75,75))

    world.draw()

    # Uncomment this to show the grid
    #show_grid()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()


# Print hi every time program runs
def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Main function proxy. Functions should be run here
def main():
    print_hi('PyCharm')

# Main Function
if __name__ == '__main__':
    main()
