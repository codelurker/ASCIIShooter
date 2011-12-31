import general

class ship(general.active):
	def __init__(self,x=0,y=0,player=False):
		self.pos = [x,y]
		
		self.direction = ''
		
		self.move_speed = 0
		self.move_speed_max = 0
		
		self.weapons = []
		
		self.sprite = ''
	
	def add_weapon(self,weapon):
		self.weapons.append(weapon)

class fighter(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 3
		
		self.sprite = '^'