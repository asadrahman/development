class Settings():
    """A class to store settings for Alien Invasion"""
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_colour = (230, 230, 230)
        
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3
        
        # alien settings
        self.fleet_drop_speed = 10

        self.speed_scale = 1.1
        self.score_scale = 1.5
        
        self.initialise_dynamic_settings()
        
        
    def initialise_dynamic_settings(self):
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.alien_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.ship_speed_factor *= self.speed_scale
        self.fleet_direction *= self.speed_scale 
        
        self.alien_points = int(self.alien_points * self.score_scale)
