import general, debris, var

class ship(general.active):
	def __init__(self,x=0,y=0,player=False):
		var.ships.append(self)
		
		self.pos = [x,y]
		self.last_pos = [x,y]
		self.start_pos = [x,y]
			
		if player:
			self.direction = ''
			self.direction_lock = False
		else:
			self.direction = 'south'
			self.direction_lock = True
		
		self.life = 0
		self.life_max = 0
		
		self.move_speed = 0
		self.move_speed_max = 0
		
		self.weapons = []
		self.weapon = 0
		
		self.sprite = ''
		self.color = (0,0,0)
	
	def tick(self):
		general.active.tick(self)
		
		if self.life <= 0: self.destroy()
		
		self.last_pos = [self.pos[0],self.pos[1]]
		
		for wep in self.weapons:
			wep.tick()
		
		for b in var.bullets:
			if b.owner == self: continue
			
			if b.pos == self.pos or b.pos == self.last_pos:
				self.life-=1
				b.destroy()
	
	def shoot(self):
		self.weapons[self.weapon].fire()
	
	def add_weapon(self,weapon):
		self.weapons.append(weapon)
		weapon.owner = self
	
	def destroy(self):
		for dir in ['north','northwest','northeast','east','west','southwest','southeast','south']:
			debris.debris(dir,x=self.pos[0],y=self.pos[1])
		
		var.ships.remove(self)

class fighter(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 3
		self.life = 1
		self.life_max = 1
		
		if player: self.sprite = '^'
		else: self.sprite = 'v'
		self.color = (0,255,0)

class bomber(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 15
		self.life = 3
		self.life_max = 3
		
		self.sprite = 'B'
		self.color = (255,0,0)
	
#	def tick(self):
#		ship.__tick__(self)
#		
#		if not player:
			