import pygame
class Settings():
    '''存储《外星人入侵》的所有设置'''

    def __init__(self):
        #屏幕
        self.screen_width=800
        self.screen_height=1200
        self.bg=pygame.image.load('bg.bmp')

        #子弹
        self.bullet_speed = 6
        self.bullet_size = [3,15]
        self.bullet_color = 255,255,0
        self.bullets_allowed = 5000

        #外星人
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_go = 1
        self.alien_score = 50

        self.wave = 1
        self.ship_limit = 3
        self.score_add_speed = 1.5
        self.difficultly_add_speed = 1.1

    def reset_settings(self):
        #屏幕
        self.screen_width=800
        self.screen_height=1200
        self.bg=pygame.image.load('bg.bmp')

        #子弹
        self.bullet_speed = 6
        self.bullet_size = [3,15]
        self.bullet_color = 255,255,0
        self.bullets_allowed = 5

        #外星人
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_go = 1
        self.alien_score = 50

        self.wave = 1
        self.ship_limit = 3
        self.difficultly_add_speed = 1.1