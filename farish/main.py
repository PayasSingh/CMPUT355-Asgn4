import pygame
import sys
from game_window_class import *


WIDTH, HEIGHT = 500,500
BACKGROUND= (199,199,199)
FPS=60

def get_events():
    global running
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

def update():
    game_window.update()


def draw():
    window.fill(BACKGROUND)
    game_window.draw()

pygame.init()
window= pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window= game_window(window, 50,50)

running=True

while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
