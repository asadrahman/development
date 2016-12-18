import pygame
from pygame.sprite import Group
from settings import Settings
from games_stats import GamesStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    stats = GamesStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Create a ship
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
        
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, 
                aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
            play_button)
        

        
run_game()
