class Settings:
    """stores all settings"""
    def __init__(self):
        """starts the game settings"""
        #screen settings
        self.screen_width = 1800
        self.screen_height = 900
        self.bg_color = (230,230,230)

        #ship speed
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        
