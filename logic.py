import ship, random, var

class spawner:
	def __init__(self):
		self.schedule = []
	
	def add(self,entry):
		self.schedule.append({'time':random.randint(1,10),'action':entry})
	
	def execute(self,action):
		action = action.split(':')
		
		#<single,wave>:<type>:<opt>
		#Options:
		#	wave: number
		if action[0]=='single':
			if action[1]=='fighter': ship.fighter(x=random.randint(0,var.win_size[1]),y=-1)
			elif action[1]=='bomber': ship.bomber(x=random.randint(0,var.win_size[1]),y=0)
	
	def tick(self):
		for entry in self.schedule:
			if entry['time']: entry['time']-=1
			else: self.execute(entry['action']);self.schedule.remove(entry)
		
		if len(var.ships)<5 and len(self.schedule)<5:
			self.add('single:fighter')