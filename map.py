class Map:


	def __init__(self):
		self.name = "test"
		self.load_map()
		

	def load_map(name):
		self.map - [
		[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
		[2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1],
		[3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2],
		[4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3]
		]

	def scroll_x(dir):
		self.x += dir

	def scroll_y(dir):
		self.y += dir