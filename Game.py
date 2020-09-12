from Engine import *

mainWindow = Window();
renderer = Renderer();

mainWindow.OpenWindow(480,480,"Hello PyGame!");
renderer.OpenSurface(480, 480, mainWindow);

splash = LoadImage("Splash_480.png");

while mainWindow.UpdateWindow():
	renderer.Background((255,255,255));
	renderer.DrawImage(splash, (0,0));

mainWindow.CloseWindow()