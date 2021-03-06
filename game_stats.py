class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.game_over=False
        self.best_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0