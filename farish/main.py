import sys

import pygame
from game_window_class import *
from button_class import *

WIDTH, HEIGHT = 800,800
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

            else:
                for button in buttons:
                    button.click()


def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)

            else:
                for button in buttons:
                    button.click()


def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)

            else:
                for button in buttons:
                    button.click()


def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)


def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()


def make_buttons():
    buttons = []
    '''
    buttons.append(Button(window, WIDTH//2-50, 50, 100, 20, text="START", color = (28,111,51),
                          hover_color=(48, 131, 82)))
    '''
    buttons.append(Button(window, WIDTH//5-50, 50, 100, 30, text= "RUN", color = (28,111,51), function= run_game,
                          hover_color=(48, 131, 82)))

    buttons.append(Button(window, WIDTH//2-50, 50, 100, 20, text="Pause", color = (28,111,51), function= pause_game,
                          hover_color=(48, 131, 82)))
    buttons.append(Button(window, WIDTH//1.2-50, 50, 100, 20, text="Restart", color = (28,111,51),function = restart_game,
                          hover_color=(48, 131, 82)))

    return buttons

    pass
def run_game():
    global state
    state="running"
    pass

def pause_game():
    global state
    state="paused"
    pass

def restart_game():
    global state
    state="restart"
    pass

def mouse_on_grid(pos):
    if pos[0] > 100 and pos [0] < WIDTH - 100:
        if pos[1] > 180 and pos[1] < HEIGHT-20:
            return True
    return False


def click_cell(pos):

    grid_pos=[pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    print(grid_pos[0], grid_pos[1])


    if game_window.grid[grid_pos[1]] [grid_pos[0]].alive:
        game_window.grid[grid_pos[1]] [grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]] [grid_pos[0]].alive = True



    print("click")

pygame.init()
window= pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window= game_window(window, 100,180)
buttons = make_buttons()
state='setting'

running=True

while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()

    pygame.display.update()
    clock.tick(FPS)
    print(state)

pygame.quit()
sys.exit()
