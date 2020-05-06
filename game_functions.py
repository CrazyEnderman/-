import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
from random import choice
def keydown_check(event,ai_settings,screen,ship,aliens,bullets,stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        print('Thanks for playing!')
        sys.exit()
    elif event.key == pygame.K_r:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        bullets.empty()
        aliens.empty()

        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
def keyup_check(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,x,y):
    press=play_button.rect.collidepoint(x,y)
    if press and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        bullets.empty()
        aliens.empty()

        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    '''检查并响应事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print('Thanks for playing!')
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydown_check(event,ai_settings,screen,ship,aliens,bullets,stats)
        
        elif event.type == pygame.KEYUP:
            keyup_check(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            check_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,x,y)

def draw_wave(ai_settings,screen,stats):
    '''显示波数'''
    string = 'Wave the '+str(ai_settings.wave)+'th    '+str(stats.ships_left)+' Ships Left'
    font = pygame.font.SysFont(None,45)
    msg = font.render(string,True,(255,255,255))
    msg_rect = msg.get_rect()
    msg_rect.x = 10
    msg_rect.y = 20
    screen.blit(msg,msg_rect)

def update_screen(ai_settings,screen,ship,aliens,bullets,stats,score,play_button):
    '''更新屏幕'''
    screen.blit(ai_settings.bg,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    draw_wave(ai_settings,screen,stats)
    score.show_score()
    if not stats.game_active:
        if stats.game_over:
            string = 'Game Over!'
            font = pygame.font.SysFont(None,150)
            text = font.render(string,True,(255,0,0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.y = 200
            screen.blit(text,text_rect)
        play_button.draw_button()
    pygame.display.flip()

def check_collide(bullets,aliens,ship,ai_settings,screen,score,stats):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_score * len(aliens)
            score.prep_score()
        if stats.best_score < stats.score:
            stats.best_score = stats.score
            score.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ai_settings.wave += 1
        ai_settings.alien_speed *= ai_settings.difficultly_add_speed
        ai_settings.fleet_drop_speed *= ai_settings.difficultly_add_speed
        ai_settings.bullet_size[0] *= ai_settings.difficultly_add_speed
        ship.speed *= ai_settings.difficultly_add_speed
        ai_settings.alien_score = int(ai_settings.alien_score * ai_settings.score_add_speed)

def update_bullets(ai_settings,screen,ship,aliens,bullets,score,stats):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            stats.score -= 5
    
    check_collide(bullets,aliens,ship,ai_settings,screen,score,stats)

def fire(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def get_number_x(ai_settings,width):
        space_x = ai_settings.screen_width - 2 * width
        alien_number_x = int(space_x / (2 * width))
        return alien_number_x

def get_number_rows(ai_settings,ship_height,alien_height):
    space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    rows = int(space_y / (2 * alien_height))
    return rows

def create_alien(ai_settings,screen,aliens,alien_number,rows):
    alien = Alien(ai_settings,screen)
    width = alien.rect.width
    alien.x = width + 2 * width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rows
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    width = alien.rect.width
    alien_number_x = get_number_x(ai_settings,width)
    rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row in range(rows):
        for alien_number in range(alien_number_x):
            if choice([True,True,True,False]):
                create_alien(ai_settings,screen,aliens,alien_number,row)

def check_fleet_edge(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_go *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left <= 1:
        ship.speed = 3
        pygame.mouse.set_visible(True)
        ai_settings.reset_settings()
        stats.reset_stats()
        stats.score = 0
        stats.game_active = False
        stats.game_over = True
    else:
        #将ships_left-1
        stats.ships_left -= 1
        #清空外星人和子弹
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        sleep(0.5)
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edge(ai_settings,aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        print('Ship Hit!!!')
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    for alien in aliens.copy():
        if alien.rect.bottom >= screen.get_rect().bottom:
            print('Ship Hit!!!')
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break