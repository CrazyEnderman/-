import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        '''绘制子弹对象'''
        super().__init__()
        self.screen = screen
        
        #绘制矩形
        self.rect = pygame.Rect(0,0,ai_settings.bullet_size[0],ai_settings.bullet_size[1])
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y 

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)