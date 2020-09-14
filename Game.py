from Engine import *

mouseX = 0;
mouseY = 0;

def CloseFunc():
	print("Closing...");

def MousePos(pos):
	print(pos);
	mouseX = pos[0];
	mouseY = pos[1];

def KeyDown(key, mods):
	pass;



mainWindow = Window();


mainWindow.OpenWindow(480,480,"Hello PyGame!");
renderer.OpenSurface(480, 480, mainWindow);

splash = LoadImage("Splash_480.png");
assets.LoadImage("Splash_480.png","Splash");

GetEventSystem().SetCloseHandler(CloseFunc);
EventSys.SetMousePosHandler(MousePos);
EventSys.SetKeyDownHandler(KeyDown);

box = Sprite((255,0,255), Vector2(0,0), (480, 480), "Splash");

while mainWindow.UpdateWindow():
	renderer.Background((255,255,255));
	#renderer.DrawImage(assets.GetAsset("Splash"), (0,0));
	renderer.DrawFilledRect((255,0,255),0,0,mouseX,mouseY);

	print(mouseX, mouseY);
	#box.DrawSelf();

mainWindow.CloseWindow()



