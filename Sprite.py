import Engine;
class Sprite:
	#self: Sprite, tint: tuple3, pos: Vector2, size: tuple2, spriteName: String
	def __init__(self, tint, pos, size, spriteName):
		self.pos = pos;
		self.size = size;
		self.tint = tint;
		self.spriteName = spriteName;

		print(self);

	def DrawSelf(self):
		#Engine.GetRenderer().DrawFilledRect(self.tint, self.pos.X(), self.pos.Y(), self.size[0], self.size[1]);
		Engine.GetRenderer().DrawImage(Engine.GetAssetManager().GetAsset(self.spriteName), self.pos);

	def __str__(self):
		return "Pos: "+str(self.pos)+", Size: "+str(self.size)+", Image Asset ID: "+self.spriteName;
