import general, var

class ship(general.active):
	def __init__(self,x=0,y=0,player=False):
		var.ships.append(self)
		
		self.pos = [x,y]
		
		self.direction = ''
		self.direction_lock = False
		
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
		
		for wep in self.weapons:
			wep.tick()
		
		for b in var.bullets:
			if b.owner == self: continue
			
			if b.pos == self.pos:
				b.destroy()
	
	def shoot(self):
		self.weapons[self.weapon].fire()
	
	def add_weapon(self,weapon):
		self.weapons.append(weapon)
		weapon.owner = self
	
	def destroy(self):
		var.ships.remove(self)

class fighter(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 3
		self.life = 3
		self.life_max = 3
		
		if player: self.sprite = '^'
		else: self.sprite = 'v'
		self.color = (0,255,0)

class bomber(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 6
		self.life = 5
		self.life_max = 5
		
		self.sprite = 'B'
		self.color = (255,0,0)