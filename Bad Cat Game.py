import pygame, os
from Game_Code import Intro, New_Menu_Code, Level_1, Menu_Code

pygame.init()

pygame.display.set_caption('Bad Cat!')

clock = pygame.time.Clock()

windowSize = (1136, 764)

first_opening = True

#Create the display. Make it right size and let user change size
screen = pygame.display.set_mode(windowSize)

cat_sitting = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Cat Sitting.jpg')).convert_alpha()
pygame.display.set_icon(cat_sitting)

while True:
    with open("New Player.txt", mode="r", encoding="utf-8") as f:
        new_player = f.read()

    intro_1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Intro Screens', 'Intro Img1.jpg')).convert_alpha()
    intro_1 = pygame.transform.scale(intro_1, windowSize)
    intro_2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Intro Screens', 'Intro Img2.jpg')).convert_alpha()
    intro_2 = pygame.transform.scale(intro_2, windowSize)
    intro_3 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Intro Screens', 'Intro Img3.jpg')).convert_alpha()
    intro_3 = pygame.transform.scale(intro_3, windowSize)

    intro_sfx = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds_and_Music', 'Undertale Sound Effect - Intro.mp3'))

    if first_opening == True:
        Intro.intro_function(screen, clock, windowSize, intro_1, intro_2, intro_3, intro_sfx)
        first_opening = False

    menu_block = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Menu_Block.jpg')).convert_alpha()
    menu_block = pygame.transform.scale(menu_block, (817,579))
    menu_block_r = pygame.Rect(-817,-100,817,579)

    menu_title = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Menu_Title.jpg')).convert_alpha()
    menu_title = pygame.transform.scale(menu_title, (817,579))
    menu_title_r = pygame.Rect(windowSize[0] - 120,-100,817,579)

    new_game_button = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'New_Game_Button.png')).convert_alpha()
    new_game_button = pygame.transform.scale(new_game_button, (290,143))
    new_game_button_r = pygame.Rect(400, 450, 290, 143)

    continue_button = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Continue Button.png')).convert_alpha()
    continue_button = pygame.transform.scale(continue_button, (290, 143))
    continue_button_r = pygame.Rect(400, 450, 290, 143)

    quit_button = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Quit_Button.png')).convert_alpha()
    quit_button = pygame.transform.scale(quit_button, (290,143))
    quit_button_r = pygame.Rect(400, 600, 290, 143)

    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'Sounds_and_Music', 'Menu Music.wav'))
    pygame.mixer.music.play()

    if new_player == "True":
        New_Menu_Code.new_menu_function(screen, clock, menu_block, menu_title,menu_block_r,menu_title_r,new_game_button,quit_button,new_game_button_r,quit_button_r)
        with open("New Player.txt", mode="w", encoding="utf-8") as f:
            f.write("False")
    else:
        Menu_Code.menu_function(screen, clock, menu_block, menu_title, menu_block_r, menu_title_r, continue_button,quit_button,continue_button_r,quit_button_r)

    room_0 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Level Screens', 'Room_0.png')).convert_alpha()
    room_0 = pygame.transform.scale(room_0, windowSize)
    room_1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Level Screens', 'Room_1.png')).convert_alpha()
    room_1 = pygame.transform.scale(room_1, windowSize)
    room_2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Level Screens', 'Room_2.png')).convert_alpha()
    room_2 = pygame.transform.scale(room_2, windowSize)
    room_3 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Level Screens', 'Room_3.png')).convert_alpha()
    room_3 = pygame.transform.scale(room_3, windowSize)
    room_4 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Screens', 'Level Screens', 'Room_-1.png')).convert_alpha()
    room_4 = pygame.transform.scale(room_4, windowSize)

    crosshair = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Crosshair.png')).convert_alpha()
    crosshair = pygame.transform.scale(crosshair, (137,111))

    bottle_full = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Bottle Full.png')).convert_alpha()
    bottle_full = pygame.transform.scale(bottle_full, (1029,659))

    bottle_spray = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Bottle Spray.png')).convert_alpha()
    bottle_spray = pygame.transform.scale(bottle_spray, (1029,659))

    cat_sitting = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Cat Sitting.jpg')).convert_alpha()
    cat_angry = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Cat Angry.jpg')).convert_alpha()
    cat_running = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Characters', 'Cat Running.png')).convert_alpha()
    cat_running_in = pygame.transform.flip(cat_running,True,False)

    pause_button = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Pause Button.png')).convert_alpha()
    pause_button = pygame.transform.scale(pause_button, (70, 70))
    pause_button_r = pygame.Rect(1066, 0, 70, 70)

    pause_resume = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Pause Resume Button.png')).convert_alpha()
    pause_resume_r = pygame.Rect(370,100,423,144)
    pause_retry = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Pause Restart Button.png')).convert_alpha()
    pause_retry_r = pygame.Rect(370, 300, 423, 144)
    pause_menu = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Pause Menu Button.png')).convert_alpha()
    pause_menu_r = pygame.Rect(370, 500, 423, 144)
    pause_outline = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Pause Outline.png')).convert_alpha()
    pause_outline = pygame.transform.scale(pause_outline, (700, 664))

    main_menu_button = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Go Main Menu Button.png')).convert_alpha()
    main_menu_button = pygame.transform.scale(main_menu_button, (367,122))
    main_menu_button_r = pygame.Rect(400, windowSize[1]-320, 367, 122)
    retry_button = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Other', 'Retry Button.png')).convert_alpha()
    retry_button = pygame.transform.scale(retry_button, (367,122))
    retry_button_r = pygame.Rect(400, windowSize[1]-170, 367, 122)

    spray_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds_and_Music', 'Spray Bottle sfx.wav'))
    footsteps = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds_and_Music', 'Footsteps.wav'))
    win_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds_and_Music', 'Win Music.mp3'))
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'Sounds_and_Music', 'Pepper Steak.mp3'))

    while Level_1.level_1_function(screen, clock, room_0, room_1, room_2, room_3, room_4, crosshair, bottle_full, bottle_spray, windowSize, spray_sound, footsteps, win_sound, cat_sitting, cat_angry, cat_running, cat_running_in, pause_button, pause_button_r, pause_resume, pause_resume_r, pause_outline, pause_retry, pause_retry_r, pause_menu, pause_menu_r, main_menu_button, main_menu_button_r, retry_button, retry_button_r) == True:
        Level_1.level_1_function(screen, clock, room_0, room_1, room_2, room_3, room_4, crosshair, bottle_full, bottle_spray, windowSize, spray_sound, footsteps, win_sound, cat_sitting, cat_angry, cat_running, cat_running_in, pause_button, pause_button_r, pause_resume, pause_resume_r, pause_outline, pause_retry, pause_retry_r, pause_menu, pause_menu_r, main_menu_button, main_menu_button_r, retry_button, retry_button_r)