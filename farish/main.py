import sys

import pygame
from game_window_class import *
from button_class import *

WIDTH, HEIGHT = 500,700
BACKGROUND= (199,199,199)
FPS=60



def get_events():
    global running
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)


def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

def button_draw():
    buttons = []
    '''
    buttons.append(Button(window, WIDTH//2-50, 50, 100, 20, text="START", color = (28,111,51), 
                          hover_color=(48, 131, 82)))
    '''
    buttons.append(Button(window, WIDTH//2-50, 550, 100, 20, text="START", color = (28,111,51), 
                          hover_color=(48, 131, 82)))                      
                    
    return buttons


def mouse_on_grid(pos):
    if pos[0] > 50 and pos [0] < WIDTH - 50:
        if pos[1] > 50 and pos[1] < HEIGHT-20:
            return True
    return False


def click_cell(pos):
    grid_pos=[pos[0]-50, pos[1]-50]
    grid_pos[0] = grid_pos[0]//20 
    grid_pos[1] = grid_pos[1]//20
    print(grid_pos[0], grid_pos[1])

    if game_window.grid[grid_pos[1]] [grid_pos[0]].alive:
        game_window.grid[grid_pos[1]] [grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]] [grid_pos[0]].alive = True

    


pygame.init()
window= pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window= game_window(window, 50,50)
buttons = button_draw()

running=True

while running:
    mouse_pos = pygame.mouse.get_pos()
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
