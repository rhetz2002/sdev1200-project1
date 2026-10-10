# going to send it in as is. it works and the major things that 
# bugs me were fixed, fixed major errors and cleaned up where i could

import random
import sys
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)
from player_char import player
from player_char import player_bullet
from enemie import blue_bullet
from enemie import green_bullet
from enemie import orange_bullet
from enemie import enemie_orange
from enemie import enemie_blue
from enemie import enemie_green
import asyncio
from ui import title
from ui import start_button
from ui import game_over
from ui import restart
from ui import win
from ui import score
from script import *

sprite_name = [title, win, game_over, restart, start_button, player]

sprites = {}
# Initalises pygame 

pygame.init()

wincon = False

# used for random bullet fire

random_spawn = random.randint(1160 ,11120)

# Sets up window with dimensions

width = 1400
height = 900
screen = pygame.display.set_mode((width, height))

# Sets window caption

pygame.display.set_caption("Air Combat Comand")

# Sets running to true to keep track of when to close game

running = True
gameover = False

# add sprites to sprite groups

score_display = score()

key = 0

sprites = {}

# it buggs me to no end with how porly i made this loop and how it names the 
# dictionary keys but im too tired to fix it so i just made sure to clarify with coments

while key <= 5:

    sprites[f'{str(key)}1'] = sprite_name[key]()

    sprites[f'{str(key)}_sprite'] = pygame.sprite.GroupSingle()

    sprites[f'{str(key)}_sprite'].add(sprites[f'{str(key)}1'])

    key += 1

bullet = pygame.sprite.Group()
enemie_bullets = pygame.sprite.Group()

green_enemie = pygame.sprite.Group()
blue_enemie = pygame.sprite.Group()
orange_enemie = pygame.sprite.Group()

menu = True
gameover = False

def quit():

    pygame.quit()
    sys.exit()

def start():

    global spawn_timer, move_clock, score_value, move_tick, game_clock
    global past_item_green, past_item_blue, past_item_orange

    #restart player position

    sprites['51'].restart()

    spawn_timer = 0

    move_clock = 0

    score_value = 0

    move_tick = 0

    past_item_green = []
    
    past_item_blue = []
    
    past_item_orange = []

    game_clock = 0

start()

# while loop will end when user choses to close game

while running:

    while menu is True:
        
        # refrencs sprites dictionary 0_sprite is title sprite

        sprites['0_sprite'].draw(screen)

        # 4_sprite is start button

        sprites['4_sprite'].draw(screen)    

        pygame.display.flip() 

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1: 
                    
                    # miss named but going with it, is also start button
                    # '41' start button
                    if sprites['41'].rect.collidepoint(event.pos):

                        menu = False

                        start_tick =  pygame.time.get_ticks()

            if event.type == pygame.QUIT:
            
                running = False

                quit()

    score_display.score_draw(screen, 50, 50, score)

    for enemie in green_enemie:

            if enemie.shots_fired < 3:

                if pygame.time.get_ticks() - enemie.last_shot >= 1000:

                    enemie_bullets.add(enemie.attack())

                    enemie.shots_fired += 1

                    enemie.last_shot = pygame.time.get_ticks()
            else:

                enemie.shots_fired = 0

    screen.fill((255, 255, 255))

    # Create a surface and pass in a tuple containing its length and width
    
    surf = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    
    surf.fill((0, 0, 0))

    # draws sprites

    bullet.update()

    enemie_bullets.update()

    if move_clock >= 20:

        green_enemie.update()

        blue_enemie.update()

        orange_enemie.update()

        move_clock = 0
    
    else: 

        move_clock +=1
    
    # draws sprites to screen

    # calls player bullet to move if on screen
    

    enemie_bullets.draw(screen)

    bullet.draw(screen) 
    # sprites['5_sprite'] player sprite group
    sprites['5_sprite'].draw(screen)

    green_enemie.draw(screen)

    blue_enemie.draw(screen)

    orange_enemie.draw(screen)
    # sprites['51'] player sprite
    pygame.draw.rect(screen, (0, 255, 0), (30, 850, sprites['51'].hp * 20 , 30) ) 

    score_display.score_draw(screen, 50, 50,  score_value)
    
    pygame.display.flip() 

    curent_tick = pygame.time.get_ticks()

    if str(curent_tick - start_tick) not in past_item_green:  

        if str(curent_tick - start_tick) in script:

            for item in script[str(curent_tick - start_tick)][2]:
                
                green_obj = enemie_green()
            
                past_item_green.append(str(curent_tick - start_tick)) 
        
                green_obj.spawn(item)

                green_enemie.add(green_obj)

    if str(curent_tick - start_tick) not in past_item_blue:  

        if str(curent_tick - start_tick) in script:

            for item in script[str(curent_tick - start_tick)][1]:
                
                blue_obj = enemie_blue()    
            
                past_item_blue.append(str(curent_tick - start_tick)) 
        
                blue_obj.spawn(item)
        
                blue_enemie.add(blue_obj)

    if str(curent_tick - start_tick) not in past_item_orange:  

        if str(curent_tick - start_tick) in script:
            
            for item in script[str(curent_tick - start_tick)][0]:
                
                orange_obj = enemie_orange()

                past_item_orange.append(str(curent_tick - start_tick)) 
        
                orange_obj.spawn(item)

                orange_enemie.add(orange_obj)

    if spawn_timer >= random_spawn:
        
        random_spawn = random.randint(1160 ,11120)

        spawn_timer = 0

        for enemie in blue_enemie:

            enemie_bullets.add(enemie.attackC())
            enemie_bullets.add(enemie.attackL())
            enemie_bullets.add(enemie.attackR())    

        for enemie in orange_enemie:

            enemie_bullets.add(enemie.atk())

    else: 

        spawn_timer += 1

        game_clock += 1

#----------------------------------------
# checks for bullit hit on enemy or self
#----------------------------------------
    
    for active in bullet:

        bullet_hit_green = pygame.sprite.spritecollide(active, green_enemie, True)

        bullet_hit_blue = pygame.sprite.spritecollide(active, blue_enemie, True)

        bullet_hit_orange = pygame.sprite.spritecollide(active, orange_enemie, True)
        
        if bullet_hit_green or bullet_hit_blue or bullet_hit_orange: 

            active.kill()

            score_value += 30

    for active in enemie_bullets:
        # sprites['5_sprite'] = player sprite
        bullet_hit_self = bullet_hit_green = pygame.sprite.spritecollide(active, sprites['5_sprite'], False)

        if bullet_hit_self:
            # player obj
            gameover = sprites['51'].damage()

            active.kill()

    #---------------------------
    # player win check and logic
    #---------------------------
    if curent_tick - start_tick >= 67000:
        
        wincon = True

    if gameover is True or wincon is True:
        
        start()
        
        while gameover is True or wincon is True:

            screen.fill((0, 0, 0))    

            if gameover is True:
                #game over sprite
                sprites['2_sprite'].draw(screen)
                #restart button
                sprites['3_sprite'].draw(screen)    

                pygame.display.flip() 

            if wincon is True:
                # sprites['1_sprite'] = win sprite
                sprites['1_sprite'].draw(screen)
                #restart button
                sprites['3_sprite'].draw(screen)    

                pygame.display.flip() 

            orange_enemie.empty()

            blue_enemie.empty()    

            green_enemie.empty()

            enemie_bullets.empty()

            bullet.empty() 

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1: 

                        if start.rect.collidepoint(event.pos):

                            gameover = False
                            wincon = False

                            start_tick =  pygame.time.get_ticks()
                            
                if event.type == pygame.QUIT:
            
                    running = False

                    quit()

#----------------------------------------
#          listens for user input
#----------------------------------------
    # controlls player movement
    # sprite['51'] = player obj
    move_tick = sprites['51'].player_con(move_tick)

    for event in pygame.event.get():
        
        # controlls player fire

        if event.type == KEYDOWN and event.key == K_SPACE:
            # sprite['51'] = player obj
            bullet_obj = sprites['51'].player_fire()

            bullet.add(bullet_obj)

        # Check if the user clicked X button
        
        if event.type == pygame.QUIT:

            running = False
    
# Cleanly closes game

quit()

    