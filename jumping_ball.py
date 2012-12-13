import pygame
import sys # fuer sys.exit()

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

# neu: surface = Oberflaeche, kann spaeter auch ein Bild sein
surface = pygame.Surface( (10, 10) )
surface.fill( pygame.Color("red") )

# neu: Rechteck hat Position und Groesse
rect = surface.get_rect()

while True:
  rect = rect.move( 1, 0 ) # neues, verschobenes Rechteck

  # Zeichne Oberflaeche in Rechteck
  screen.blit( surface, rect )

  # aktualisiere Bildschirm
  pygame.display.flip()

  # neu: Auf Quit event des Fensters reagieren.
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
