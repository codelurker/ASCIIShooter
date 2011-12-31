import pygcurse, pygame, game, var
from pygame.locals import *

pygame.font.init()
_font = pygame.font.Font('ProggySquare.ttf', 24)

var.clock = pygame.time.Clock()
var.window = pygcurse.PygcurseWindow(var.win_size[0], var.win_size[1],font=_font,caption='ASCIItest')
var.window.autoupdate = False

game.init()