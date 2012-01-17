import var

class active:
	def tick(self):
		if self.move_speed:
			self.move_speed -= 1
		else:
			self.move()
			self.move_speed = self.move_speed_max
		
		if self.pos[0]<0 or self.pos[0] > var.win_size[0]\
			or self.pos[1]<0 or self.pos[1] > var.win_size[1]:
			self.destroy()
		
	def move(self):
		if self.direction == 'north': self.pos[1]-=1
		elif self.direction == 'south': self.pos[1]+=1
		elif self.direction == 'east': self.pos[0]+=1
		elif self.direction == 'west': self.pos[0]-=1
		elif self.direction == 'northeast': self.pos[0]+=1;self.pos[1]-=1
		elif self.direction == 'northwest': self.pos[0]-=1;self.pos[1]-=1
		elif self.direction == 'southeast': self.pos[0]+=1;self.pos[1]+=1
		elif self.direction == 'southwest': self.pos[0]-=1;self.pos[1]+=1
		
		if not self.direction_lock: self.direction = ''
	
	def draw(self):
		var.window.putchar(self.sprite,fgcolor=self.color,x=self.pos[0],y=self.pos[1])