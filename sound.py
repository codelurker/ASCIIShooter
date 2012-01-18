import pygame, var
from pygame.locals import *

def play_song(song):
	song = pygame.mixer.music.load(song)
	pygame.mixer.music.play()

def stop_song(fade=0):
	if fade: pygame.mixer.music.fadeout(fade)
	else: pygame.mixer.music.stop()

def play_sound(sound):
	sound.play()