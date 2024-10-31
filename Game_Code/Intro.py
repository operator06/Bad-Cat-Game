import pygame, sys
from pygame import *

pygame.init()

def intro_function(screen, clock, windowSize, intro_1, intro_2, intro_3, intro_sfx):
    counting_var = 0
    sound_effect_var = True
    font1 = pygame.font.Font(None, 64)
    click_txt = font1.render("Click to continue", False, (255,255,255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if counting_var == 501:
                    running = False
        if counting_var <= 170:
            if sound_effect_var == True:
                intro_sfx.play()
                sound_effect_var = False
            screen.blit(intro_1, (0,0))
            counting_var += 1
        elif 170 < counting_var <= 370:
            if sound_effect_var == False:
                intro_sfx.play()
                sound_effect_var = True
            screen.blit(intro_2, (0,0))
            counting_var += 1
        else:
            if sound_effect_var == True:
                intro_sfx.play()
                sound_effect_var = False
            screen.blit(intro_3, (0,0))
            if counting_var <= 500:
                counting_var += 1
            if counting_var == 501:
                screen.blit(click_txt, (766,700))
        clock.tick(60)
        pygame.display.flip()