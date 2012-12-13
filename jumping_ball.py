import pygame
import sys

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

surface = pygame.Surface( (10, 10) )
surface.fill( pygame.Color("red") )

rect = surface.get_rect()

while True:
  rect = rect.move( 1, 0 )

  # neu: Bildschirm wieder schwarz machen
  screen.fill( (0, 0, 0) )
  screen.blit(surface, rect)

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
