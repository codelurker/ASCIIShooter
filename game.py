import input, ship, weapon, var

def init():
	#Make player
	var.player = ship.fighter(x=15,y=25,player=True)
	
	#Test enemies
	e1 = ship.fighter(x=15,y=3)
	for b in range(0,15):
		ship.bomber(x=2+b,y=15-b)
	
	var.player.add_weapon(weapon.single_shot())

	#Game loop
	while 1:
		var.window.setscreencolors('white','black',clear=True)
		input.get_input()
		
		for b in var.bullets:
			b.tick()
			b.draw()
		
		for s in var.ships:
			s.tick()
			s.draw()
			
		var.window.update()
		var.clock.tick(var.fps)
