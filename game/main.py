# Imports pygame modual

# !!note!!
#-----------------------
# core functuonalty is here it is just really disorginised
# orginisation is on my list of things to do but i thought it was good enough to submit
#
# pardon spelling as per usual
#
# myles tollefson
#
#
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

# Initalises pygame

pygame.init()

def quit():

    pygame.quit()
    sys.exit()

Win = False

#test code for testing eneime spawn

random_spawn = random.randint(1160 ,11120)

spawn_timer = 0

move_clock = 0

score_value = 0

# tracks which items in the script have been done to prevent spam
past_item_green = []
past_item_blue = []
past_item_orange = []

# may or may not use for event gen
game_clock = 0

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

#menu images 

score_display = score()

Title = title()
Title_sprite = pygame.sprite.GroupSingle()
Title_sprite.add(Title)

Win = win()
Win_message = pygame.sprite.GroupSingle()
Win_message.add(Win)

Game_over = game_over()
Game_over_message = pygame.sprite.GroupSingle()
Game_over_message.add(Game_over)

restart_but = restart()
restart_button = pygame.sprite.GroupSingle()
restart_button.add(restart_but)

start = start_button()
startbutton = pygame.sprite.GroupSingle()
startbutton.add(start)

# single sprite group for player
player_obj = player()
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(player_obj)

bullet = pygame.sprite.Group()
enemie_bullets = pygame.sprite.Group()



green_enemie = pygame.sprite.Group()
blue_enemie = pygame.sprite.Group()
orange_enemie = pygame.sprite.Group()

def reset():

    player_obj.restart()

    
    


menu = True
gameover = False
# while loop will end when user choses to close game
while running:

    while menu is True:

        Title_sprite.draw(screen)

        startbutton.draw(screen)    

        pygame.display.flip() 

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1: 

                    if start.rect.collidepoint(event.pos):

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

    

    #draws sprites

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
    
    #TEMP COMMENT DO NOT REMOVE

    

    enemie_bullets.draw(screen)

    bullet.draw(screen) 

    player_sprite.draw(screen)

    green_enemie.draw(screen)

    blue_enemie.draw(screen)

    orange_enemie.draw(screen)

    pygame.draw.rect(screen, (0, 255, 0), (30, 850, player_obj.hp * 20 , 30) ) 

    score_display.score_draw(screen, 50, 50,  score_value)
    

    pygame.display.flip() 
        
    # debug system for rand enmy spawn and shoot
    #-------------------------------------------
    #curently being modified for final spawn system

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

       # if event.type == KEYDOWN:

        #    if event.key == K_UP:  
    
# checks for bullit hut on enemy

    for active in bullet:

        bullet_hit_green = pygame.sprite.spritecollide(active, green_enemie, True)

        bullet_hit_blue = pygame.sprite.spritecollide(active, blue_enemie, True)

        bullet_hit_orange = pygame.sprite.spritecollide(active, orange_enemie, True)
        
        if bullet_hit_green or bullet_hit_blue or bullet_hit_orange: 

            active.kill()

            score_value += 30
    

    for active in enemie_bullets:

        bullet_hit_self = bullet_hit_green = pygame.sprite.spritecollide(active, player_sprite, False)

        if bullet_hit_self:

            gameover = player_obj.damage()

            active.kill()

            
    

    

       
    
    
    
    
    

    if curent_tick - start_tick == 67000:
        win = True

    if gameover is True or win is True:
        
        reset()
        
        while gameover is True or win is True:

            screen.fill((0, 0, 0))    

            if gameover is True:

                Game_over_message.draw(screen)

                restart_button.draw(screen)    

                pygame.display.flip() 

            if win is True:

                Win_message.draw(screen)

                restart_button.draw(screen)    

                pygame.display.flip() 


            orange_enemie.empty()

            blue_enemie.empty()    

            green_enemie.empty()

            enemie_bullets.empty()

            score = 0
    
            past_item_green = []
            past_item_blue = []
            past_item_orange = []   

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1: 

                        if start.rect.collidepoint(event.pos):

                            gameover = False
                            win = False

                            start_tick =  pygame.time.get_ticks()
                            spawn_timer = 0
                            game_clock = 0
                            move_clock = 0


                if event.type == pygame.QUIT:
            
                    running = False

                    quit()

    # listens for user input
    #print(curent_tick)
    for event in pygame.event.get():
        
       

        


        #controlls player movment

        player_obj.player_con()                

        if event.type == KEYDOWN and event.key == K_SPACE:

            bullet_obj = player_obj.player_fire()

            bullet.add(bullet_obj)

            
            

        # Check if the user clicked X button
        
        if event.type == pygame.QUIT:

            running = False
    

    
            
# Cleanly closes game

quit()

    