import pygame
import sys
import time # fuer sleep

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

surface = pygame.image.load("/usr/share/doc/python-pygame/tut/intro/ball.gif")
rect = surface.get_rect()

sound = pygame.mixer.Sound("/usr/share/pyshared/pygame/examples/data/whiff.wav")

x_direction = 1
y_direction = 1

while True:
  if rect.right > 640 or rect.left < 0:
    x_direction = x_direction * -1
    sound.play()

  if rect.bottom > 480 or rect.top < 0:
    y_direction = y_direction * -1
    sound.play()

  rect = rect.move(x_direction, y_direction)
  screen.fill((0,0,0))
  screen.blit(surface, rect)
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  time.sleep(0.0018)
