import pygame

pygame.init();

class Window:
	def __init__(self):
		self.clock = pygame.time.Clock();
		pass

	def OpenWindow(self, width, height, title):
		pygame.display.set_mode((width, height));
		pygame.display.set_caption(title);

	def UpdateWindow(self):
		pygame.display.update();
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False;
		self.clock.tick(60);
		return True
		pass

	def CloseWindow(self):
		pygame.quit();
		pass


class GameState:
	def Enter(self):
		pass

	def Leave(self):
		pass

	def Update(self, ts):
		pass