import pygame.font

class ScoreBoard():
    '''计分板'''
    def __init__(self,ai_settings,screen,stats):
        '''初始化'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

       	self.text_color = (255,255,255)
       	self.font = pygame.font.SysFont(None,48)

       	self.prep_score()

    def prep_score(self):
        score = round(self.stats.score,-1)
        score = str('{:,}'.format(score))
        best_score = round(self.stats.best_score,-1)
        best_score = str('{:,}'.format(best_score))
        self.score_image = self.font.render('Best:'+best_score+'  Score:'+score,True,self.text_color,(0,0,0))

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)