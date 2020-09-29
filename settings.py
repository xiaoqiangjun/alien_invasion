class Settings():
    """储存所有设置的类"""
    def __init__(self):
        """初始化静态游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 加速参数
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态游戏设置"""
        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        # 1向右，-1向左
        self.fleet_direction = 1
        # 计分设置
        self.alien_points = 50

    def increase_speed(self):
        """加速，增加分数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)