import bullet

class weapon:
	def __init__(self):
		self.name = ''
		self.owner = None
		
		self.reload = 0
		self.reload_max = 0
		
		self.sprite = ''
	
	def tick(self):
		if self.reload: self.reload-=1
	
	def fire(self):
		if not self.reload:
			bullet.straight(self.owner,'north',x=self.owner.pos[0],y=self.owner.pos[1])
			self.reload = self.reload_max

class single_shot(weapon):
	def __init__(self):
		weapon.__init__(self)
		
		self.name = 'Single Shot'
		
		self.reload_max = 10