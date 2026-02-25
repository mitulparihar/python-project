import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	''' Class to manage bullets fired from the ship'''
	def __init__(self , ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen = screen
	#Create a bullet rect at 0,0 then set correct position
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
	#Store the y factor in decimal because y is height
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor 
		
	def update(self):
		'''Move the bullet up when it is shooted from the ship'''
		self.y -= self.speed_factor
		#update the rect according to y 
		self.rect.y = self.y
	def draw_bullets(self):
		pygame.draw.rect(self.screen , self.color , self.rect)		
