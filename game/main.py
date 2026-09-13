# Imports pygame modual
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
# Initalises pygame

pygame.init()

#test code for testing eneime spawn
random_spawn = random.randint(1160 ,11120)
spawn_timer = 0

move_clock = 0

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

# decalre sprite grouping so i only need to refresh once for all sprites



# add sprites to sprite groups
player_obj = player()

# single sprite group for player

player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(player_obj)

bullet = pygame.sprite.Group()
enemie_bullets = pygame.sprite.Group()


green_enemie = pygame.sprite.Group()
blue_enemie = pygame.sprite.Group()
orange_enemie = pygame.sprite.Group()


# while loop will end when user choses to close game
while running:

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

    if move_clock >= 60:

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

    player_sprite.draw(screen)

    green_enemie.draw(screen)

    blue_enemie.draw(screen)

    orange_enemie.draw(screen)


    pygame.display.flip() 
        
    # debug system for rand enmy spawn and shoot



    if spawn_timer >= random_spawn:
        
        green_obj = enemie_green()

        green_obj.spawn()

        green_enemie.add(green_obj)

        blue_obj = enemie_blue()

        blue_obj.spawn()
        
        blue_enemie.add(blue_obj)

        orange_obj = enemie_orange()

        orange_obj.spawn()

        orange_enemie.add(orange_obj)

        random_spawn = random.randint(1160 ,11120)

        spawn_timer = 0

        #---------

       #blue_bullet_obj = blue_obj.attack()

        #green_bullet_obj = green_obj.attack()

        #orange_bullet_obj = orange_obj.attack()


        for enemie in blue_enemie:

            enemie_bullets.add(enemie.attackC())
            enemie_bullets.add(enemie.attackL())
            enemie_bullets.add(enemie.attackR())    

        for enemie in orange_enemie:

            enemie_bullets.add(enemie.attack())

        #for enemie in green_enemie:

         #   if enemie.shots_fired < 3:

          #      if pygame.time.get_ticks() - enemie.last_shot >= 5000:

           #         enemie_bullets.add(enemie.attack())

            #        enemie.shots_fired += 1
            
            #else:

            #    enemie.shots_fired = 0
        
        #enemie_bullets.add(orange_bullet_obj)

        #enemie_bullets.add(blue_bullet_obj)

        #enemie_bullets.add(green_bullet_obj)

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
    

    for active in enemie_bullets:

        bullet_hit_self = bullet_hit_green = pygame.sprite.spritecollide(active, player_sprite, False)

        if bullet_hit_self:

            player_obj.damage()

            active.kill()

    # listens for user input
    
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

pygame.quit()
sys.exit()