import pygame
import random
from pygame import mixer
import math

pygame.init()


class DisplaySettings:
    """A class to store all settings for Alien Invasion Display"""
    
    def __init__(self):
        """Initialize the game settings"""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_img = pygame.image.load('images/background.png')
        self.screen_caption = "SpaceCrash"
        self.game_icon = pygame.image.load('images/wheel.png')
        self.screen_surface = pygame.display.set_mode((1200, 800))
    
    def set_background_color(self):
        self.screen_surface.fill((10, 10, 10))
    
    def set_custom_background(self):
        self.screen_surface.blit(self.background_img, (0, 0))
    
    @staticmethod
    def set_game_caption():
        pygame.display.set_caption("SpaceCrash")
    
    def set_game_icon(self):
        pygame.display.set_icon(self.game_icon)
        
        
display = DisplaySettings()


class ShipSettings:
    """A class to store all settings for Player/Ships settings"""
    
    def __init__(self):
        self.ship_img = pygame.image.load('images/spaceship.png')
        self.ship_width = 555
        self.ship_height = 700
        self.ship_width_motion = 0
    
    def draw_ship(self, x_axis, y_axis):
        display.screen_surface.blit(self.ship_img, (x_axis, y_axis))


ship = ShipSettings()


class Enemies:
    """A class to store all settings for Enemies"""
    
    alien_img = []
    alien_x = []
    alien_y = []
    alien_x_move = []
    alien_y_move = []
    number_of_aliens = 15
    for enemy in range(number_of_aliens):
        alien_img.append(pygame.image.load('images/monster.png'))
        alien_x.append(random.randint(0, 735))
        alien_y.append(random.randint(100, 300))
        alien_x_move.append(2)
        alien_y_move.append(80)
    
    def alien(self, x_axis, y_axis, enemy):
        display.screen_surface.blit(self.alien_img[enemy], (x_axis, y_axis))


aliens = Enemies()


class BulletSettings:
    """A class to store all settings for Bullets and Collisions"""
    
    def __init__(self):
        self.bullet_img = pygame.image.load('images/bullet.png')
        self.bullet_x_width = 0
        self.bullet_y_height = 700
        self.bullet_x_width_motion = 0
        self.bullet_y_height_motion = 15
        self.bullet_state = "ready"
    
    def draw_bullets(self, x_axis, y_axis):
        self.bullet_state = "fire"
        display.screen_surface.blit(bullets.bullet_img, (x_axis + 16, y_axis + 10))
    
    def collision_equation(self, alien_x, alien_y):
        distance = math.sqrt((math.pow(alien_x - self.bullet_x_width, 2)) +
                             (math.pow(alien_y - self.bullet_y_height, 2)))
        if distance < 27:
            return True
        else:
            return False


bullets = BulletSettings()


class ScoringSettings:
    """A class to store all settings for Scoring and Game over"""
    
    def __init__(self):
        self.current_score = 0
        self.font_text_x = 20
        self.font_text_y = 20
        self.font = pygame.font.Font('freesansbold.ttf', 34)
        self.game_over = pygame.font.Font('freesansbold.ttf', 64)
    
    def display_score(self, x_axis, y_axis):
        score = self.font.render("Score: " + str(self.current_score), True, (255, 255, 255))
        display.screen_surface.blit(score, (x_axis, y_axis))
    
    def show_game_over(self):
        text = self.game_over.render("Game Over!", True, (255, 255, 255))
        display.screen_surface.blit(text, (400, 300))


score = ScoringSettings()


class GameAudioSettings:
    """Stores all Audio configs for the game"""
    
    def __init__(self):
        self.fire_bullet_sound = mixer.Sound('audio/fire.wav')
        self.bullet_hits_sound = mixer.Sound('audio/boom.wav')
        self.background_sound = mixer.music.load("audio/loop.wav")
    
    @staticmethod
    def background_music():
        mixer.music.play(-1)
    
    def play_bullet_audio(self):
        self.fire_bullet_sound.play()
    
    def play_collision_audio(self):
        self.bullet_hits_sound.play()


sounds = GameAudioSettings()