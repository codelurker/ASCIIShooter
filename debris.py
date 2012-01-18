import general, var, random

class debris(general.active):
	def __init__(self,direction,x=0,y=0,owner=None):
		var.debris.append(self)
		
		self.pos = [x,y]
		
		self.owner = owner
		
		self.move_speed = 3
		self.move_speed_max = 3
		
		self.life = 0
		self.life_max = 0
		
		self.direction = direction
		self.direction_lock = True
		
		self.sprite = ''
		self.color = (0,0,255)
		
		self.on_frame = 0
		self.sprite_frames = ['0','O','*','o','.']
	
	def destroy(self):
		var.debris.remove(self)

	def tick(self):
		general.active.tick(self)
		
		if self in var.debris and len(self.sprite_frames)>=2:
			if self.on_frame >= len(self.sprite_frames): self.destroy()
	
	def move(self):
		general.active.move(self)
		
		self.sprite = self.sprite_frames[self.on_frame]
		if len(self.sprite_frames)>=2: self.on_frame += 1

class star(debris):
	def __init__(self,direction='south'):
		debris.__init__(self,direction,x=random.randint(0,var.win_size[0]),y=0)
		
		_r = random.randint(-100,100)
		self.color = (150+_r,150+_r,150+_r)
		self.sprite_frames = ['\'']
		
		self.move_speed = random.randint(2,5)
		self.move_speed_max = random.randint(2,5)