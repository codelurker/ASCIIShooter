input = {'up':False,'down':False,'left':False,'right':False,'upleft':False,'upright':False,'downleft':False,'downright':False,'l':False,'z':False}
binds = {'up':'north','down':'south','left':'west','right':'east','upleft':'northwest','upright':'northeast','downleft':'southwest','downright':'southeast',\
	'l':'l','z':'z'}

win_size = (30,30)
fps = 120
movedelay = 1
movedelay_max = 3
cleaning = False
state = 'menu'

pause = False
score = 0
lives = 3
difficulty = 75

menu_select = 0

sound_volume = 0.3
music_volume = 1

ships = []
bullets = []
debris = []