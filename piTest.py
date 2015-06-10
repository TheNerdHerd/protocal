#I wouldn't run it if I were you....

import joshPyLib
import pygame
pygame.init()


def main():
    #Declare colors, to make it easier later and stuffs
    colors = {
    "white" : "#ffffff",
    "black" : "#000000",
    "bg" : "#d7d7c5",
    "bluesteel" : "#85a8a0"
    }
    #Convert colors into a format pygame can use
    for key in colors:
        colors[key] = pygame.color.Color(colors[key])

    size = (800, 600)
    caption = "This is a caption"

    screen = joshPyLib.createMainWindow(size, caption)
    background = joshPyLib.createSurface(screen, colors["bg"])

    clock = pygame.time.clock()
    font = pygame.font.SysFont('Helvetica', 25, True, False) #because I can't stand crappy default fonts

    #Main program loop
    done = False
    while not done:
        #Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


        #Drawing code
    pygame.quit()
