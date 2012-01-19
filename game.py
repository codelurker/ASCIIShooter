import input, logic, ship, weapon, debris, sound, var

def init():
	#Make player
	var.player = ship.fighter(x=15,y=25,player=True)
	var.player.move_speed_max = 3
	
	ship_spawner = logic.spawner()
	star_spawner = logic.star_spawner()
	
	sound.play_song('endofstory.mod')

	#Game loop
	while 1:
		var.window.setscreencolors('white','black',clear=True)
		input.get_input()
		
		for d in var.debris:
			if not var.pause or d.owner==var.player:
				d.tick()
			
			d.draw()

		for b in var.bullets:
			if not var.pause: b.tick()
			b.draw()
		
		for s in var.ships:
			if not var.pause: s.tick()
			s.draw()
		
		if not var.player in var.ships and not var.lives:
			var.pause = True
			
			_count = 0
			for d in var.debris:
				if d.owner==var.player: _count+=1
			
			if not _count:
				var.window.putchars('YOU ARE DEAD',fgcolor=(255,255,255),x=9,y=15)
		elif not var.player in var.ships and var.lives and not var.cleaning:
			var.cleaning = True
			
			sound.stop_song()
			
			for d in var.debris:
				if d.owner==var.player: continue
				
				d.move_speed_max = d.move_speed_max/2
				d.move_speed = 0
			
			for s in var.ships:
				s.move_speed_max = 1#s.move_speed_max/2
				s.move_speed = 0
				s.direction = 'south'
				s.y_limit = var.win_size[1]+1
		
		if var.cleaning:
			var.window.putchars('LIFE -1',fgcolor=(255,255,255),x=12,y=15)
			
			if not len(var.ships):
				var.player = ship.fighter(x=15,y=25,player=True)
				var.player.move_speed_max = 3
				
				var.lives-=1
				var.cleaning = False
		elif var.pause and var.player in var.ships:
			var.window.putchars('PAUSED',fgcolor=(255,255,255),x=12,y=15)
		
		var.window.putchars('Score %s' % (var.score),fgcolor=(255,255,255),x=0,y=0)
		var.window.putchars('Lives %s' % (var.lives),fgcolor=(255,255,255),x=23,y=0)
			
		if not var.pause and not var.cleaning: ship_spawner.tick()
		if not var.pause: star_spawner.tick()

		var.window.update()
		var.clock.tick(var.fps)
