import pygame

class title(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load('sprite/title.png').convert_alpha()
        
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (650, 300))

        self.rect = self.image.get_rect(center=(700, 200))

class start_button(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/start.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (300, 100))

        self.rect = self.image.get_rect(center=(700, 500))