import pygame

pygame.init();

class Window:
	def __init__(self):
		self.clock = pygame.time.Clock();
		self.frame = None;
		pass

	def OpenWindow(self, width, height, title):
		self.frame = pygame.display.set_mode((width, height));
		pygame.display.set_caption(title);

	def UpdateWindow(self):
		pygame.display.update();
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False;
		self.clock.tick(60);
		return True

	def CloseWindow(self):
		pygame.quit();
		pass

	def BlitToWindow(self, item):
		self.frame.blit(item, (0,0));

class Renderer:
	def __init__(self):
		self.surface = None;
		self.frame = None;

	def OpenSurface(self ,width, height, frame):
		self.surface = pygame.Surface((width, height), pygame.OPENGL);
		self.frame = frame;

	def Background(self,color):
		self.surface.fill(color);
		self.WriteToScreen();

	def DrawImage(self, image, pos):
		self.surface.blit(image,pos);
		self.WriteToScreen();

	def WriteToScreen(self):
		self.frame.BlitToWindow(self.surface);


class GameState:
	def Enter(self):
		pass

	def Leave(self):
		pass

	def Update(self, ts):
		pass


def LoadImage(path):
	return pygame.image.load(path);