import pygame
import math

from Sprite import *;

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
				EventSys.DispatchClose();
				return False;

			if event.type == pygame.MOUSEMOTION:
				EventSys.DispatchMousePos(event.pos);

			if event.type == pygame.KEYDOWN:
				EventSys.DispatchKeyDown(event.key, event.mod);
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
		self.surface = pygame.Surface((width, height), pygame.OPENGL | pygame.DOUBLEBUF);
		self.frame = frame;

	def Background(self,color):
		self.surface.fill(color);
		self.WriteToScreen();

	def DrawImage(self, image, pos, scale=(-1,-1)):
		if scale != (-1, -1):
			image = pygame.transform.scale(image, scale);
		self.surface.blit(image,pos);
		self.WriteToScreen();

	def DrawFilledRect(self, color, x, y, w, h):
		pygame.draw.rect(self.surface, color, (x, y, w, h));
		self.WriteToScreen();

	def WriteToScreen(self):
		self.frame.BlitToWindow(self.surface);

class Texture:
	def __init__(self, width, height, flags=0):
		self.surface = pygame.Surface((width,height),flags);

	def SetPixel(self, x, y, color):
		self.surface.set_at((x,y), color);

	def GetPixel(self, x, y):
		return self.surface.get_at((x,y));

	def LoadFromDisk(self, path):
		self.surface.blit(LoadImage(path), (0,0));

	def GetWriteToSurface(self, surface):
		surface.blit(self.surface, (0,0));



class EventSystem:
	def __init__(self):
		self.closeHandler = None;
		self.mousePosHandler = None;
		self.keyDownHandler = None;

	def DispatchClose(self):
		if self.closeHandler != None:
			self.closeHandler();

	def DispatchMousePos(self, pos):
		if self.mousePosHandler != None:
			self.mousePosHandler(pos);

	def DispatchKeyDown(self, key, mods):
		if self.keyDownHandler != None:
			self.keyDownHandler(key, mods);

	def SetCloseHandler(self, func):
		self.closeHandler = func;

	def SetMousePosHandler(self, func):
		self.mousePosHandler = func;

	def SetKeyDownHandler(self, func):
		self.keyDownHandler = func;


class GameState:
	def Enter(self):
		pass

	def Leave(self):
		pass

	def Update(self, ts):
		pass

class AssetManager:

	def __init__(self):
		self.assets = {};

	def LoadImage(self, path, name):
		self.assets[name] = LoadImage(path);

	def GetAsset(self, name):
		return self.assets[name];


class Vector2:
	def __init__(self, x = 0, y = 0):
		self.x = x;
		self.y = y;

	def __str__(self):
		return "[X:"+str(self.x)+", Y:"+str(self.y)+"]";

	def X(self):
		return self.x;

	def Y(self):
		return self.y;

	def __add__(self, other):
		x = self.x + other.x;
		y = self.y + other.y;
		return Vector2(x,y);

	def __sub__(self, other):
		x = self.x - other.x;
		y = self.y - other.y;
		return Vector2(x,y);

	def __mul__(self, other):
		x = self.x * other;
		y = self.y * other;
		return Vector2(x,y);

	def __div__(self, other):
		x = self.x / other;
		y = self.y / other;
		return Vector2(x,y);

	def MagSq(self):
		return self.x * self.x + self.y * self.y;

	def Mag(self):
		return  math.sqrt(self.MagSq());

	def Tuple2(self):
		return (self.x, self.y);

	def Tuple3(self):
		return (self.x, self.y, 1);


def LoadImage(path):
	return pygame.image.load(path);

FLAG_OPENGL = pygame.OPENGL
FLAG_DOUBLE_BUFFER = pygame.DOUBLEBUF

def GetRenderer():
	return renderer;

def GetAssetManager():
	return assets;

def GetEventSystem():
	return EventSys;

EventSys = EventSystem();
renderer = Renderer();
assets = AssetManager();