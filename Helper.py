#Extra Pygame Classes
import pygame



class Button():
	def __init__(self, rect, color, surface, funcToCall, text=None, ExtraParam=False):
		self.ExtraParam = ExtraParam
		if text is not None:
			font = pygame.font.Font("data/Font.ttf", 20)
			self.text = font.render(text, True, (255,255,255, 255))
		else:
			self.text = None
		self.rect = rect
		self.color = color
		self.surface = surface
		self.funcToCall = funcToCall
		self.buttonAreaPoints = []
		self.justPressed = 0
		endy = rect[1] + rect[3]
		endx = rect[0] + rect[2]

		for y in range(rect[1], endy):
			for x in range(rect[0], endx):
				self.buttonAreaPoints.append((x,y))
		self.buttonAreaPoints = set(self.buttonAreaPoints)
	def draw(self):
		pygame.draw.rect(self.surface, self.color, self.rect)
		if self.text is not None:
			if self.ExtraParam:
				self.surface.blit(self.text, (self.rect[0] + 20, self.rect[1] + 15))
			else:
				self.surface.blit(self.text, (self.rect[0], self.rect[1] + 15))
		if self.justPressed != 0:
			self.justPressed -= 1
		self.checkIfPressed()
	def checkIfPressed(self):
		#call from draw

		click = pygame.mouse.get_pressed()
		if click[0] == 1:
			mousepos = pygame.mouse.get_pos()
			if mousepos in self.buttonAreaPoints and self.justPressed == 0:
				self.justPressed = 5
				self.funcToCall()

		# self.funcToCall()
