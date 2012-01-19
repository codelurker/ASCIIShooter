import pygame, var
from pygame.locals import *

def play_song(song):
	song = pygame.mixer.music.load(song)
	pygame.mixer.music.set_volume(var.music_volume)
	pygame.mixer.music.play()

def pause_song():
	pygame.mixer.music.pause()

def unpause_song():
	pygame.mixer.music.unpause()

def stop_song(fade=0):
	if fade: pygame.mixer.music.fadeout(fade)
	else: pygame.mixer.music.stop()

def load_sound(file):
	_s = pygame.mixer.Sound('explode1.wav');
	_s.set_volume(var.sound_volume)
	
	return _s

def play_sound(sound):
	sound.play()