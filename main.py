import pygame
import random
import settings as s
import events


class AlienInvasion:
    # Initialize pyGame
    pygame.init()
    
    @staticmethod
    def play_game():
        
        # Set Game's Icon
        s.display.set_game_icon()
        
        # Set Game's Caption (title)
        s.display.set_game_caption()
        
        # Set Game's Background Music
        s.sounds.background_music()
        
        game_play = True
        while game_play:
            
            # Set Game's Surface color
            s.display.set_background_color()
            
            # Set Game's background
            s.display.set_custom_background()
            
            # Start Listening for Events
            events.listen_for_events.listen()
            
            # Location of Player's ship: Declare Ship Boundaries on the x axis
            s.ship.ship_width += s.ship.ship_width_motion
            if s.ship.ship_width <= 0:
                s.ship.ship_width = 0
            elif s.ship.ship_width >= 1136:
                s.ship.ship_width = 1136
            
            # Movement, Location of enemies: Enemy's boundaries on the x axis
            for enemy in range(s.aliens.number_of_aliens):
                
                # Game Over Condition
                if s.aliens.alien_y[enemy] > 600:
                    for all_enemies in range(s.aliens.number_of_aliens):
                        s.aliens.alien_y[all_enemies] = 8000
                    s.score.show_game_over()
                    break
                
                s.aliens.alien_x[enemy] += s.aliens.alien_x_move[enemy]
                if s.aliens.alien_x[enemy] <= 0:
                    s.aliens.alien_x_move[enemy] = 2
                    s.aliens.alien_y[enemy] += s.aliens.alien_y_move[enemy]
                elif s.aliens.alien_x[enemy] >= 1136:
                    s.aliens.alien_x_move[enemy] = -2
                    s.aliens.alien_y[enemy] += s.aliens.alien_y_move[enemy]
                
                # Define Collision:
                collision = s.bullets.collision_equation(s.aliens.alien_x[enemy], s.aliens.alien_y[enemy])
                
                # After Collision, reset bullet to fire again
                if collision:
                    s.bullets.bullet_y_height = 700
                    s.bullets.bullet_state = "ready"
                    
                    # Direct Hit Sound Plays
                    s.sounds.play_collision_audio()
                    
                    # Update the score to count the collision/hit
                    s.score.current_score = s.score.current_score + 1
                    
                    # Make the Enemy aliens re-spawn at a random location
                    s.aliens.alien_x[enemy] = random.randint(0, 735)
                    s.aliens.alien_y[enemy] = random.randint(100, 300)
                
                s.aliens.alien(s.aliens.alien_x[enemy],
                               s.aliens.alien_y[enemy], enemy)
            
            if s.bullets.bullet_y_height <= 0:
                s.bullets.bullet_y_height = 700
                s.bullets.bullet_state = "ready"
            
            # Bullet Redraw
            if s.bullets.bullet_state is "fire":
                s.bullets.draw_bullets(s.bullets.bullet_x_width, s.bullets.bullet_y_height)
                s.bullets.bullet_y_height -= s.bullets.bullet_y_height_motion
            
            # Screen always has a player/ship
            s.ship.draw_ship(s.ship.ship_width, s.ship.ship_height)
            
            # Always display the score as defined
            s.score.display_score(s.score.font_text_x, s.score.font_text_y)
            pygame.display.update()


if __name__ == '__main__':
    game = AlienInvasion()
    game.play_game()
