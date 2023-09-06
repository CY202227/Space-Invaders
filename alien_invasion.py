import sys  
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from alien import Alien
from ship import Ship
from button import Button

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
	screen = pygame.display.set_mode((1200,800))
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	pygame.display.set_caption("FinalShootAlien")
	play_button = Button(ai_settings,screen,"Play")
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	bg_color = (230,230,230)
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()

