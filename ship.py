import general, weapon, debris, sound, var, shapes, random

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
		
		self.y_limit = -100
		
		self.life = 0
		self.life_max = 0
		
		self.move_speed = 0
		self.move_speed_max = 0
		
		self.weapons = []
		self.weapon = 0
		
		self.sprite = ''
		self.color = (0,0,0)
	
	def tick(self):
		if not self.move_speed and not var.cleaning and not self.player:
			if self.pos[0]<=0: self.direction = 'east';self.pos[1]+=1
			elif self.pos[0]>=var.win_size[0]-1: self.direction = 'west';self.pos[1]+=1
		elif not self.move_speed and self.player:
			if self.pos[0]<=0: self.pos[0]=1
			elif self.pos[0]>=var.win_size[0]-1: self.pos[0]=var.win_size[0]-2
		
		general.active.tick(self)
		
		if self.life <= 0: sound.play_sound(var.snd_explode1);self.destroy()
		
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
		
		if not self.player and not var.cleaning: var.score+=self.score
		
		var.ships.remove(self)

class fighter(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 5
		self.life = 1
		self.life_max = 1
		
		self.score = 10
		
		if player: self.sprite = '^';self.add_weapon(weapon.single_shot())
		else: self.sprite = 'v';self.add_weapon(weapon.single_shot_slow())
		self.color = (0,255,0)
		
	def tick(self):
		if not self.move_speed and not self.player:
			if self.pos[1] == self.y_limit and self.direction == 'south':
				self.direction = random.choice(['east','west'])
		
		ship.tick(self)

class bomber(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 15
		self.life = 2
		self.life_max = 2
		
		self.score = 20
		
		self.sprite = 'B'
		self.color = (255,0,0)
	
	def destroy(self):
		ship.destroy(self)
		
		_c = shapes.draw_circle(self.pos,10)
		
		if self.life<=0:
			for _s in var.ships:
				for pos in _c:
					pos = list(pos)
					if _s.pos == pos:
						_s.life = 0
			
			for pos in _c:
				debris.debris('',x=pos[0],y=pos[1],owner=self)

class rock(ship):
	def __init__(self,x=0,y=0,player=False):
		ship.__init__(self,x=x,y=y,player=player)
		
		self.move_speed_max = 3
		self.life = 1
		self.life_max = 1
		
		self.score = 5
		
		self.sprite = 'o'
		self.color = (105,105,105)