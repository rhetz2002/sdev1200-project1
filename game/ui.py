import pygame
from player_char import player

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

class game_over(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load('sprite/gameover.png').convert_alpha()
        
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (650, 300))

        self.rect = self.image.get_rect(center=(700, 200))

class restart(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/restart.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (300, 100))

        self.rect = self.image.get_rect(center=(700, 500))

class win(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('sprite/WIN.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (300, 100))

        self.rect = self.image.get_rect(center=(700, 300))

class score():
    def __init__(self):
        self.score_font = pygame.font.Font(None, 40)

    def score_draw(self, screen, x, y, score):
        score_text = self.score_font.render(str(score), True, (0, 255, 0))
        screen.blit(score_text, (x, y))