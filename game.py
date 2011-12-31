import input, ship, var

def init():
	#Make player
	var.player = ship.fighter(player=True)

	#Game loop
	while 1:
		var.window.setscreencolors('white','black',clear=True)
		input.get_input()
		
		var.player.tick()
		var.player.draw()
		
		var.window.update()
