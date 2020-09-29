class GameStats():
    """追踪游戏统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """初始化变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1