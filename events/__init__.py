import settings as s
from settings import *
import sys


class EventsListen:
    @staticmethod
    def listen():
        
        # Listen for Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
                # Listen for KEyDOWN events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    s.ship.ship_width_motion = -5
                if event.key == pygame.K_RIGHT:
                    s.ship.ship_width_motion = 5
                
                # Listen for 'Fire" Events. aka Spacebar
                if event.key == pygame.K_SPACE:
                    if s.bullets.bullet_state is "ready":
                        # Play Bullet Sound
                        s.sounds.play_bullet_audio()
                        
                        # Fire the bullet
                        s.bullets.bullet_x_width = s.ship.ship_width
                        s.bullets.draw_bullets(s.bullets.bullet_x_width,
                                                     s.bullets.bullet_y_height)
            
            # Listen for KEyUP Events: If the L or R keys are released. Stop the ship.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    s.ship.ship_width_motion = 0


listen_for_events = EventsListen()
