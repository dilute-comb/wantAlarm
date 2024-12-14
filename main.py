import pygame
import time

file = 'changes.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

time.sleep(10)
pygame.mixer.music.pause()