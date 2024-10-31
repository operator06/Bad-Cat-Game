import pygame, sys
from pygame import *

pygame.init()

def movement(room_number, screen, room_0, room_1, room_2, room_3, room_4):
    if room_number == 0:
        screen.blit(room_0, (0,0))
    elif room_number == -1:
        screen.blit(room_4, (0,0))
    elif room_number == 1:
        screen.blit(room_1, (0,0))
    elif room_number == 2:
        screen.blit(room_2, (0,0))
    elif room_number == 3:
        screen.blit(room_3, (0,0))

def level_1_function(screen, clock, room_0, room_1, room_2, room_3, room_4, crosshair, bottle_full, bottle_spray, windowSize, spray_sound, footsteps, win_sound, cat_sitting, cat_angry, cat_running, cat_running_in, pause_button, pause_button_r, pause_resume, pause_resume_r, pause_outline, pause_retry, pause_retry_r, pause_menu, pause_menu_r, main_menu_button, main_menu_button_r, retry_button, retry_button_r):
    from random import randint, choice

    pygame.mixer.music.play()

    running = True

    room_number = 0

    bottle_spraying = False

    spray_timer = 0

    cat_moving_timer = 0
    cat_sitting_timer = 0
    cat_angry_timer = 0
    cat_moving_end_time = 0
    cat_sitting_end_time = 0

    level_time_counter = 0
    current_time = 3600

    win_sound_timer = 0

    win_sound_var = True

    new_cat_pos = True
    cat_moving = False
    cat_in_room = False

    being_sprayed = False

    paused = False

    rooms = [-1, 1, 2, 3]
    cat_room = 0

    cat_rect = pygame.Rect(105,258,200,300)

    score = 0

    level_font = pygame.font.Font(None, 60)

    while running:
        pos = pygame.mouse.get_pos()
        if current_time == 0:
            pygame.mixer.music.stop()
            if win_sound_var == True:
                win_sound.play()
                win_sound_var = False
            pygame.mouse.set_visible(True)
            screen.fill((0,0,0))
            finished_words = level_font.render(f"Congratulations! Your final score is: {score}!", False, (255,255,255))
            screen.blit(finished_words, (180,300))
            if win_sound_timer < 200:
                win_sound_timer += 1
            else:
                screen.blit(main_menu_button, (400, windowSize[1]-320))
                screen.blit(retry_button, (400, windowSize[1]-170))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if retry_button_r.collidepoint(pos) and win_sound_timer == 200:
                        return True
                    if main_menu_button_r.collidepoint(pos) and win_sound_timer == 200:
                        return False
            pygame.display.flip()
            clock.tick(60)
        else:
            pygame.mouse.set_visible(False)

            crosshair_pos = list(pos)
            crosshair_pos[0] -= 69
            crosshair_pos[1] -= 56
            crosshair_rect = pygame.Rect(crosshair_pos[0], crosshair_pos[1], 237, 211)

            level_time_counter += 1
            current_time = (3600 - level_time_counter) // 60

            if new_cat_pos == True:
                cat_moving_end_time = randint(60,300)
                cat_sitting_end_time = randint(185, 360)
                cat_room = choice(rooms)
                cat_moving = True
                new_cat_pos = False

            if cat_moving == True:
                if cat_moving_timer < cat_moving_end_time:
                    cat_moving_timer += 1
                else:
                    cat_moving_timer = 0
                    cat_in_room = True
                    cat_moving = False

            for event in pygame.event.get():
                #Lets player exit with "x"
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Lets player move left
                if event.type == KEYDOWN and event.key == K_a:
                    if room_number == 0:
                        room_number = 1
                    elif room_number == 2:
                        room_number = 0
                    footsteps.play()
                #Lets player move right
                if event.type == KEYDOWN and event.key == K_d:
                        if room_number == 0:
                            room_number = 2
                        elif room_number == 1:
                            room_number = 0
                        footsteps.play()
                #Lets player move up
                if event.type == KEYDOWN and event.key == K_w:
                        if room_number == 0:
                            room_number = 3
                        elif room_number == -1:
                            room_number = 0
                        footsteps.play()
                #Lets player move down
                if event.type == KEYDOWN and event.key == K_s:
                        if room_number == 0:
                            room_number = -1
                        elif room_number == 3:
                            room_number = 0
                        footsteps.play()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if pause_button_r.collidepoint(pos):
                        paused = True
                        while paused:
                            pos = pygame.mouse.get_pos()
                            pygame.mouse.set_visible(True)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                                    if pause_resume_r.collidepoint(pos):
                                        paused = False
                                    if pause_retry_r.collidepoint(pos):
                                        return True
                                    if pause_menu_r.collidepoint(pos):
                                        return False
                            screen.blit(pause_outline, (230,50))
                            screen.blit(pause_resume, (370,100))
                            screen.blit(pause_retry, (370, 300))
                            screen.blit(pause_menu, (370, 500))
                            clock.tick(60)
                            pygame.display.flip()
                    else:
                        bottle_spraying = True
                        spray_sound.play()
                        if cat_in_room == True and cat_room == room_number and cat_sitting_timer > 20:
                            if crosshair_rect.colliderect(cat_rect):
                                being_sprayed = True

            if bottle_spraying == True:
                spray_timer += 1
                if spray_timer == 30:
                    bottle_spraying = False
                    spray_timer = 0
            movement(room_number, screen, room_0, room_1, room_2, room_3, room_4)

            if cat_in_room == True:
                if being_sprayed == True:
                    if cat_room == room_number:
                        if cat_angry_timer > 30:
                            screen.blit(cat_running, (50, 300))
                        else:
                            screen.blit(cat_angry, (200,300))
                    cat_angry_timer += 1
                    if cat_angry_timer > 50:
                        being_sprayed = False
                        cat_in_room = False
                        cat_angry_timer = 0
                        cat_sitting_timer = 0
                        score += 10
                        new_cat_pos = True
                else:
                    if cat_room == room_number:
                        if cat_sitting_timer <= 20:
                            screen.blit(cat_running_in, (50, 300))
                        elif cat_sitting_timer < cat_sitting_end_time + 20:
                            screen.blit(cat_sitting, (200,300))
                    cat_sitting_timer += 1
                    if cat_sitting_timer == cat_sitting_end_time:
                        cat_sitting_timer = 0
                        cat_in_room = False
                        new_cat_pos = True
            score_words = level_font.render(f"Score: {score}", False, (255, 0, 0))
            timer_words = level_font.render(f"Time left: {current_time}", False, (0,0,0))
            if bottle_spraying == True:
                screen.blit(bottle_spray, (0,windowSize[1]-559))
            else:
                screen.blit(bottle_full, (0,windowSize[1]-559))
            screen.blit(score_words, (10,10))
            screen.blit(pause_button, (1066,0))
            screen.blit(timer_words, (windowSize[0]-400,10))
            screen.blit(crosshair, crosshair_rect)
            pygame.display.flip()
            clock.tick(60)