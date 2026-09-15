import random
import pygame
import time
from script import *

# enemie class 1

class enemie_orange(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprite/enemy1.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    

    def atk(self):
        
        bullet = orange_bullet()

        bullet.fire(self.rect.x, self.rect.y)

        return bullet

    def spawn(self, item):

        self.rect.topleft = (item, -110)

        

                
            
        

                 



    def update(self):

        self.rect.y += 1

class orange_bullet(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/bullet.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.power = 2  

    def fire(self, x, y):

        self.rect.topleft = (x, y)

    def update(self):
    
        self.rect.y += 1


class enemie_blue(pygame.sprite.Sprite):


    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprite/enemy2.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

        self.health = 5
    
    def attackL(self):
        
        bullet = blue_bullet()
        
        

        bullet.fire(self.rect.x, self.rect.y)
        
        

        return bullet
    def attackR(self):
        bullet2 = blue_bullet2()
        bullet2.fire(self.rect.x, self.rect.y)
        return bullet2

    def attackC(self):
        bullet3 = blue_bullet3()
        bullet3.fire(self.rect.x, self.rect.y)
        return bullet3
    
    def spawn(self, item):

        self.rect.topleft = (item, -110)

    def update(self):

        self.rect.y += 1

class blue_bullet(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/bullet.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.power = 2  

    def fire(self, x, y):

        self.rect.topleft = (x, y)

    def update(self):
    
        self.rect.y += 1
        self.rect.x += 1

class blue_bullet2(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/bullet.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.power = 2  

    def fire(self, x, y):

        self.rect.topleft = (x, y)

    def update(self):
    
        self.rect.y += 1
        self.rect.x -= 1

class blue_bullet3(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/bullet.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.power = 2  

    def fire(self, x, y):

        self.rect.topleft = (x, y)

    def update(self):
    
        self.rect.y += 1

class enemie_green(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprite/enemy3.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

        self.health = 5

        self.shots_fired = 0
        
        self.last_shot = pygame.time.get_ticks()

    def attack(self):
            
            bullet = green_bullet()

            bullet.fire(self.rect.x, self.rect.y)

            return bullet

    def spawn(self, item):

        self.rect.topleft = (item,-110)
            
    
    def update(self):

        self.rect.y += 1



class green_bullet(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/bullet.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.power = 2  

    def fire(self, x, y):

        self.rect.topleft = (x, y)

    def update(self):
    
        self.rect.y += 1
