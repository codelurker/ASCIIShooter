import var

class active:
	def tick(self):
		if self.move_speed:
			self.move_speed -= 1
		else:
			self.move()
			self.move_speed = self.move_speed_max
	
	def move(self):
		if self.direction == 'north': self.pos[1]-=1
		elif self.direction == 'south': self.pos[1]+=1
		elif self.direction == 'east': self.pos[0]+=1
		elif self.direction == 'west': self.pos[0]-=1
		
		self.direction = ''
	
	def draw(self):
		var.window.putchar(self.sprite,fgcolor=(255,0,0),x=self.pos[0],y=self.pos[1])