import ship, debris, var, random

class spawner:
	def __init__(self):
		self.schedule = []
	
	def to_spawn(self):
		_c = 0
	
		for action in self.schedule:
			action = action['action'].split(':')
			
			if action[0]=='single':_c+=1
			elif action[0]=='wave':_c+=int(action[2])
		
		return _c				
	
	def add(self,entry):
		self.schedule.append({'time':random.randint(5,10),'action':entry})
	
	def execute(self,action):
		action = action.split(':')
		
		#<single,wave>:<type>:<opt>
		#Options:
		#	wave: number
		_s = None
		
		if action[0]=='single':
			if action[1]=='fighter': _s = ship.fighter(x=random.randint(1,var.win_size[1]-1),y=0)
			elif action[1]=='bomber': _s = ship.bomber(x=random.randint(1,var.win_size[1]-1),y=0)
			elif action[1]=='rock': _s = ship.rock(x=random.randint(0,var.win_size[1]-1),y=0)
			
			if _s and action[1]=='fighter': _s.y_limit = random.randint(5,5+(var.score/var.difficulty))
			
		elif action[0]=='wave':
			action[2] = int(action[2])
			x_spawn = random.randint(1,(var.win_size[0]-1)-action[2])
			
			for n in range(action[2]):
				if action[1]=='fighter': _s=ship.fighter(x=x_spawn+n,y=0)
				elif action[1]=='bomber': _s=ship.bomber(x=x_spawn+n,y=0)
				
				if _s: _s.y_limit = random.randint(5,5+(var.score/var.difficulty))
	
	def tick(self):
		for entry in self.schedule:
			if entry['time']: entry['time']-=1
			else: self.execute(entry['action']);self.schedule.remove(entry)
		
		if len(var.ships)<5+(var.score/var.difficulty) and self.to_spawn()<3+(var.score/var.difficulty) and len(self.schedule)<3+(var.score/var.difficulty):
			self.add(random.choice(['single:%s' % random.choice(['fighter','bomber','rock']),'wave:fighter:%s' % str(random.randint(3,6))]))
			
class star_spawner():
	def __init__(self):
		self.tick_max = 3
		self.ticks = 0
	
	def tick(self):
		if not self.ticks: debris.star();self.ticks=self.tick_max
		else: self.ticks-=1