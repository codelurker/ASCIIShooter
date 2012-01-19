import pygame, time, game, var, sys
from pygame.locals import *

def parse_input(key):
	if var.state == 'game':
		if key in ['north','northeast','northwest','east','west','south','southeast','southwest']:
			var.player.direction = key
		
		if key == 'z':
			var.player.shoot('north')
		
		if key == 'p':
			if var.pause: var.pause = False
			else: var.pause = True
	elif var.state == 'menu':
		if key == 'south' and var.menu_select<len(var.main_menu)-1:
			var.menu_select+=1
		elif key == 'north' and var.menu_select>0:
			var.menu_select-=1
		elif key == 'enter' and var.state=='menu':
			var.state = var.main_menu[var.menu_select]['action']
			game.setup()

def get_input():
	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key in [K_ESCAPE,K_q]:
			pygame.quit()
			sys.exit()
			
		elif event.type == KEYDOWN:
			if event.key == K_UP or event.key == K_KP8:
				if not var.input['up']:
					var.input['up'] = True
					var.movedelay = -90
			elif event.key == K_DOWN or event.key == K_KP2:
				if not var.input['down']:
					var.input['down'] = True
					var.movedelay = -90
			elif event.key == K_LEFT or event.key == K_KP4:
				if not var.input['left']:
					var.input['left'] = True
					var.movedelay = -90
			elif event.key == K_RIGHT or event.key == K_KP6:
				if not var.input['right']:
					var.input['right'] = True
					var.movedelay = -90
			elif event.key == K_KP7:
				if not var.input['upleft']:
					var.input['upleft'] = True
					var.movedelay = -90
			elif event.key == K_KP9:
				if not var.input['upright']:
					var.input['upright'] = True
					var.movedelay = -90
			elif event.key == K_KP1:
				if not var.input['downleft']:
					var.input['downleft'] = True
					var.movedelay = -90
			elif event.key == K_KP3:
				if not var.input['downright']:
					var.input['downright'] = True
					var.movedelay = -90
			elif event.key == K_z:
				if not var.input['z']:
					var.input['z'] = True
					#parse_input('z')
			elif event.key == K_p:
				parse_input('p')
			elif event.key == K_RETURN:
				parse_input('enter')
		
		elif event.type == KEYUP:
			if event.key == K_UP or event.key == K_KP8:
				var.input['up'] = False
			elif event.key == K_DOWN or event.key == K_KP2:
				var.input['down'] = False
			elif event.key == K_LEFT or event.key == K_KP4:
				var.input['left'] = False
			elif event.key == K_RIGHT or event.key == K_KP6:
				var.input['right'] = False
			elif event.key == K_KP7:
				var.input['upleft'] = False
			elif event.key == K_KP9:
				var.input['upright'] = False
			elif event.key == K_KP1:
				var.input['downleft'] = False
			elif event.key == K_KP3:
				var.input['downright'] = False
			elif event.key == K_z:
				var.input['z'] = False
	
	_draw = False
	for key in var.input.iterkeys():
			if var.input[key]:
				if var.movedelay <= 0:
					parse_input(var.binds[key])
					if var.movedelay == -90:
						var.movedelay = var.movedelay_max
				else:
					var.movedelay -= 1
				_draw = True
	
	var.clock.tick(var.fps)