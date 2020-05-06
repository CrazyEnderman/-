import pygame
from pygame.sprite import Sprite
import sys

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('alien.bmp')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_go
        self.rect.x = self.x