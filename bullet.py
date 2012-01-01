import general, var

class bullet(general.active):
	def __init__(self,owner,x=0,y=0):
		var.bullets.append(self)
		
		self.owner = owner
		
		self.pos = [x,y]
		self.last_pos = [x,y]
		self.start_pos = [x,y]
		
		self.move_speed = 0
		self.move_speed_max = 0
		
		self.life = 0
		self.life_max = 0
		
		self.direction = ''
		self.direction_lock = True
		
		self.sprite = ''
		self.color = (0,0,0)
	
	def destroy(self):
		var.bullets.remove(self)
	
class straight(bullet):
	def __init__(self,owner,direction,x=0,y=0):
		bullet.__init__(self,owner,x=x,y=y)
		
		self.direction = direction
		
		self.move_speed_max = 2
		
		self.sprite = 'O'
		self.color = (255,0,0)