import general, weapon, debris, var, random

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
		
		self.player = player
		
		self.life = 0
		self.life_max = 0
		
		self.move_speed = 0
		self.move_speed_max = 0
		
		self.weapons = []
		self.weapon = 0
		
		self.sprite = ''
		self.color = (0,0,0)
	
	def tick(self):
		if not self.move_speed:
			if self.pos[0]<=0: self.direction = 'east';self.pos[1]+=1
			elif self.pos[0]>=var.win_size[0]-1: self.direction = 'west';self.pos[1]+=1
		
		general.active.tick(self)
		
		if self.life <= 0: self.destroy()
		
		self.last_pos = [self.pos[0],self.pos[1]]
		
		for wep in self.weapons:
			wep.tick()
			if not self.player and self.pos[1]>=self.y_limit: self.shoot('south')
		
		for b in var.bullets:
			if b.owner.player == self.player: continue
			
			if b.pos == self.pos or b.pos == self.last_pos:
				self.life-=1
				b.destroy()
	
	def shoot(self,direction):
		self.weapons[self.weapon].fire(direction)
	
	def add_weapon(self,weapon):
		self.weapons.append(weapon)
		weapon.owner = self
	
	def destroy(self):
		for dir in ['north','northwest','northeast','east','west','southwest','southeast','south']:
			debris.debris(dir,x=self.pos[0],y=self.pos[1],owner=self)
		
		if not self.player: var.score+=self.score
		
		var.ships.remove(self)

class fighter(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 5
		self.life = 1
		self.life_max = 1
		
		self.score = 10
		
		if player: self.sprite = '^'
		else: self.sprite = 'v'
		self.color = (0,255,0)
		
		self.y_limit = random.randint(10,20)
		
		self.add_weapon(weapon.single_shot_slow())
	
	def tick(self):
		if not self.move_speed and not self.player:
			if self.pos[1] == self.y_limit and self.direction == 'south':
				self.direction = random.choice(['east','west'])
		
		ship.tick(self)

class bomber(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 15
		self.life = 3
		self.life_max = 3
		
		self.score = 20
		
		self.sprite = 'B'
		self.color = (255,0,0)