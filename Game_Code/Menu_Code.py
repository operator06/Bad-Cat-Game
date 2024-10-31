import pygame, sys
from pygame import *

pygame.init()

def menu_function(screen, clock, menu_block, menu_title, menu_block_r, menu_title_r, continue_button,quit_button,continue_button_r,quit_button_r):
    running = True
    red_var = 0
    green_blue = 0
    while running:
        mouse_pos = pygame.mouse.get_pos()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if continue_button_r.collidepoint(mouse_pos):
                    running = False
                if quit_button_r.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        if red_var < 204:
            red_var += 6
        if green_blue < 255:
            green_blue += 5
        screen.fill(color=(red_var,green_blue,green_blue))
        if red_var == 204 and green_blue == 255:
            if menu_block_r.x != 100 and menu_title_r.x != menu_block_r.x:
                menu_block_r = menu_block_r.move(7,0)
                menu_title_r = menu_title_r.move(-7,0)
            screen.blit(menu_block, (menu_block_r.x,menu_block_r.y))
            screen.blit(menu_title, (menu_title_r.x,menu_title_r.y))
            if menu_block_r.x == 100:
                screen.blit(continue_button, (continue_button_r.x, continue_button_r.y))
                screen.blit(quit_button, (quit_button_r.x,quit_button_r.y))
        pygame.display.flip()