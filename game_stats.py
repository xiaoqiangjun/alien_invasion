import json

class GameStats():
    """追踪游戏统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.get_high_score()
        self.reset_stats()

    def reset_stats(self):
        """初始化变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    def get_high_score(self):
        """获取记录在文件中的最高分"""
        data = {}
        try:
            with open(self.ai_settings.record_path, 'r') as fr:
                data = json.load(fr)
                self.high_score = data["high_score"]
                print(data["author"])
                fr.close()
        except (FileNotFoundError,IOError,KeyError,json.decoder.JSONDecodeError):
            data = self.ai_settings.data
            self.high_score = 520
            print(data["author"])
            with open(self.ai_settings.record_path, 'w') as fw:
                json.dump(data, fw)
                fw.close()
            