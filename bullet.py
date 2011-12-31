import general

class bullet(general.active):
	def __init__(self):
		self.move_speed = 0
		self.move_speed_max = 0
		
		self.life = 0
		self.life_max = 0
		
		self.direction = ''
	
		#def tick(self):
		#	if not self.move_speed:
		#		self.move()
		#		self.move_speed = self.move_speed_max
	
class straight(bullet):
	def __init__(self,direction):
		bullet.__init__(self)
		
		self.direction = direction