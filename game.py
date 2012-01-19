import input, logic, ship, weapon, debris, sound, random, var

def setup():
	if var.state=='game':
		var.player = ship.fighter(x=15,y=25,player=True)
		var.player.move_speed_max = 3
		var.ship_spawner = logic.spawner()
		sound.play_song('title.xm')
	elif var.state=='menu':
		sound.play_song('endofstory.mod')
	
	init()

def init():	
	star_spawner = logic.star_spawner()

	#Game loop
	while 1:
		var.window.setscreencolors('white','black',clear=True)
		input.get_input()
		
		for d in var.debris:
			if not var.pause or d.owner==var.player:
				d.tick()
			
			d.draw()

		for b in var.bullets:
			if not var.pause and var.state=='game': b.tick()
			b.draw()
		
		for s in var.ships:
			if not var.pause and var.state=='game': s.tick()
			s.draw()
		
		if var.state=='game' and not var.player in var.ships and not var.lives:
			var.pause = True
			
			_count = 0
			for d in var.debris:
				if d.owner==var.player: _count+=1
			
			if not _count:
				var.window.putchars('YOU ARE DEAD',fgcolor=(255,255,255),x=9,y=15)
		elif var.state=='game' and not var.player in var.ships and var.lives and not var.cleaning:
			var.cleaning = True
			
			sound.pause_song()
			
			for d in var.debris:
				if d.owner==var.player: continue
				
				d.move_speed_max = d.move_speed_max/2
				d.move_speed = 0
			
			for s in var.ships:
				s.move_speed_max = 1#s.move_speed_max/2
				s.move_speed = 0
				s.direction = 'south'
				s.y_limit = var.win_size[1]+1
		elif var.state=='menu':
			_r = random.randint(-55,0)
			var.window.putchars('ASCII SHOOTER',fgcolor=(255+_r,255+_r,255+_r),x=9,y=13-(len(var.main_menu)/2))
			for entry in var.main_menu:
				_i = var.main_menu.index(entry)
				if _i == var.menu_select:
					var.window.putchars('> '+entry['text'],fgcolor=(255,255,255),x=12,y=15-(len(var.main_menu)/2)+_i)
				else:
					var.window.putchars(entry['text'],fgcolor=(255,255,255),x=12,y=15-(len(var.main_menu)/2)+_i)
		
		if var.cleaning:
			var.window.putchars('LIFE -1',fgcolor=(255,255,255),x=12,y=15)
			
			if not len(var.ships):
				var.player = ship.fighter(x=15,y=25,player=True)
				var.player.move_speed_max = 3
				
				var.lives-=1
				sound.unpause_song()
				
				var.cleaning = False
		elif var.pause and var.player in var.ships:
			var.window.putchars('PAUSED',fgcolor=(255,255,255),x=12,y=15)
		
		var.window.putchars('Score %s' % (var.score),fgcolor=(255,255,255),x=0,y=0)
		var.window.putchars('Lives %s' % (var.lives),fgcolor=(255,255,255),x=23,y=0)
			
		if not var.pause and not var.cleaning and var.state=='game': var.ship_spawner.tick()
		if not var.pause: star_spawner.tick()

		var.window.update()
		var.clock.tick(var.fps)
