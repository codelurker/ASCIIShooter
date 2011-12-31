class weapon:
	def __init__(self):
		self.name = ''
		
		self.reload = 0
		self.reload_max = 0
		
		self.sprite = ''
		self.color = (0,255,0)
	
	def tick(self):
		if self.reload: self.reload-=1
	
	def fire(self):
		if not self.reload:
			#fire
			self.reload = self.reload_max

class single_shot(weapon):
	def __init__(self):
		weapon.__init__(self)
		
		self.name = 'Single Shot'
		
		self.reload_max = 4