import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
    bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, 
                aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
    bullets, mouse_x, mouse_y):
    
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)    
    if button_clicked and not stats.game_active:
        ai_settings.initialise_dynamic_settings()
        pygame.mouse.set_visible(False)
        
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        aliens.empty()
        bullets.empty()
        
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.moving_left = False
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.moving_right = False
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left == False 
        
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
    play_button):
    """Update images on screen and flip to new screen"""
    screen.fill(ai_settings.bg_colour) 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
               
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    
    
    if not stats.game_active:
        play_button.draw_button()
        
    # Make the most recent screen visible
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
        
    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets)
  
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
    aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_scores(stats, sb)
        
    if (len(aliens) == 0):
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not yet reached"""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)   
        
def create_fleet(ai_settings, screen, ship, aliens):
    """ Create a full fleet of aliens """
    alien = Alien(ai_settings, screen)
    number_of_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)

    # Create the flee of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))
    
    return number_of_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 
        (3* alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
   
    if stats.ships_left > 0:
        stats.ships_left -= 1
        print("Running out of ships " + str(stats.ships_left) + " remaining")
        
        sb.prep_ships()
        
        ai_settings.initialise_dynamic_settings()
        aliens.empty()
        bullets.empty()
    
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        print("Game Over!!")
        
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
          
def check_high_scores(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    
    

