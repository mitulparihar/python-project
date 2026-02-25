#This file is called alien_invasion.py
import pygame
from alien_invasion_settings import Settings
from coded_ship import Ship 
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import os 
import sys

def resource_path1(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path,relative_path)
def run_game():
	#Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	bullets = Group()
	aliens = Group()
	play_button = Button(ai_settings , screen , "Play") 
	pygame.init()
	pygame.mixer.init()

	#Make a damn ship `
	ship = Ship(ai_settings,screen)
	#Make alien boss
	  
	#create instance of game stats
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#Create the fleet of aliens 
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#Start the main loop for the game.
	while True:
		gf.check_events(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings , screen , ship ,aliens ,bullets,sb,stats )
			gf.update_aliens(ai_settings, screen ,ship,aliens,bullets,stats,sb)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button ,stats,sb)
run_game()		