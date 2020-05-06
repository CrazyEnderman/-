import pygame

class Ship():
    '''飞船'''
    def __init__(self,screen):
        '''初始化飞船，获取位置'''
        self.screen = screen

        #加载图像并获取外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.speed = 3
        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed
    
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx