import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
	def __init__(self,ai_settings ,screen):
		super(Ship,self).__init__()
		"""Initialize the ship and set it's freaking starting position"""
		self.screen = screen 
		self.ai_settings = ai_settings
		
		#Load the ship image and convert this shitty rocket into rectangles
		self.image = pygame.image.load(('images/ship.bmp'))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Start each new ship at the bottom centre of the screen 
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom 
		#Store decimal point for self.rect
		self.center = float(self.rect.centerx)
		#Movement Flags
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the ship's position based on movement flags"""
		#Update ship center value not the rect	
		if self.moving_right and self.rect.right <self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
				
		#Update rect object
		self.rect.centerx = self.center	
	def blitme(self):
		'''Draw the ship'''
		self.screen.blit(self.image , self.rect)	
	def center_ship(self):
		'''recenter the ship when it is hit'''
		self.center = self.screen_rect.centerx
