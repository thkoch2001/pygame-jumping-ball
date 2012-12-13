import pygame
import sys

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

surface = pygame.Surface( (10, 10) )
surface.fill(pygame.Color("red"))
rect = surface.get_rect()

x_direction = 1

while True:
  if rect.right > 640:
    x_direction = -1
  if rect.left < 0:
    x_direction = 1

  rect = rect.move(x_direction, 0)
  screen.fill((0,0,0))
  screen.blit(surface, rect)
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
