import input, logic, ship, weapon, debris, var

def init():
	#Make player
	var.player = ship.fighter(x=15,y=25,player=True)
	
	spawner = logic.spawner()
	
	var.player.add_weapon(weapon.single_shot())

	#Game loop
	while 1:
		var.window.setscreencolors('white','black',clear=True)
		input.get_input()
		
		for d in var.debris:
			d.tick()
			d.draw()

		for b in var.bullets:
			b.tick()
			b.draw()
		
		for s in var.ships:
			s.tick()
			s.draw()
		
		spawner.tick()
		var.window.update()
		var.clock.tick(var.fps)
