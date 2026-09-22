import pygame
import sys
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
)


class player_bullet(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/bullet.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.hp = 10 

    def fire(self, x, y):

        self.rect.topleft = (x, y)

    def update(self):
    
        self.rect.y -= 1

    


class player(pygame.sprite.Sprite):

    #def __init__(self, lives, health, x, y, image):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/player.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

        self.rect.topleft = (650,600)

        self.hp = 15
    
    def restart(self):
        
        self.rect.topleft = (605,600)

        self.hp = 15

    def player_con(self, move_tick):
        
        pressed = pygame.key.get_pressed()

        if pressed[K_w]:
            

            if move_tick >= 30:
                
                self.rect.move_ip(0, -5)
                
                move_tick = 0

            else:

                move_tick += 1
        if pressed[K_s]:
            
            if move_tick >= 30:
                
                self.rect.move_ip(0, 5)

                move_tick = 0

            else:

                move_tick += 1

        if pressed[K_a]:
            
            if move_tick >= 30:    
                
                self.rect.move_ip(-5, 0)

                move_tick = 0

            else:

                move_tick += 1

        if pressed[K_d]:
            
            if move_tick >= 30:
                
                self.rect.move_ip(5, 0)

                move_tick = 0

            else:

                move_tick += 1

        return move_tick

    def player_fire(self):

        bullet = player_bullet()

        bullet.fire(self.rect.x, self.rect.y)

        return bullet

    def damage(self):

        self.hp -= 1

        if self.hp <= 0:

            gameover = True

            return gameover
    
    
        

    


    






    
    



