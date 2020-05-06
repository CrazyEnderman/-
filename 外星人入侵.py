import pygame
from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from alien import Alien
from ship import Ship
from scoreboard import ScoreBoard
from game_functions import *
from button import Button
ai_settings = Settings()
timer = pygame.time.Clock()
timer.tick(100)
def run():
    pygame.init()
    screen = pygame.display.set_mode([ai_settings.screen_width,ai_settings.screen_height])
    pygame.display.set_caption('外星人入侵')
    #创建实例
    stats = GameStats(ai_settings)
    ship = Ship(screen)
    aliens = Group()
    bullets = Group()
    score = ScoreBoard(ai_settings,screen,stats)
    play_button = Button(ai_settings,screen,'Play(R)')
    create_fleet(ai_settings,screen,ship,aliens)
    bg = ai_settings.bg
    while True:
        check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)#检测事件

        if stats.game_active:
            #更新
            ship.update()
            update_bullets(ai_settings,screen,ship,aliens,bullets,score,stats)
            update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            
        update_screen(ai_settings,screen,ship,aliens,bullets,stats,score,play_button)
run()
