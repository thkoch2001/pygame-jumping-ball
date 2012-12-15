import pygame
import sys
import time # fuer sleep

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

sound = pygame.mixer.Sound("/usr/share/pyshared/pygame/examples/data/whiff.wav")

class Ball(pygame.sprite.Sprite):

    def __init__(self, area):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/usr/share/doc/python-pygame/tut/intro/ball.gif").convert()
        self.rect = self.image.get_rect()
        self.area = area
        self.x_direction = 1
        self.y_direction = 1

    def toggle_x_direction(self):
        self.x_direction *= -1

    def toggle_y_direction(self):
        self.y_direction *= -1

    def update(self):
        global sound

        if self.rect.left < self.area.left or self.rect.right > self.area.right:
            self.toggle_x_direction()
            sound.play()

        if self.rect.top < self.area.top or self.rect.bottom > self.area.bottom:
            self.toggle_y_direction()
            sound.play()

        self.rect = self.rect.move(self.x_direction, self.y_direction)

ball = Ball(pygame.display.get_surface().get_rect())
allsprites = pygame.sprite.RenderPlain((ball))

while True:

    allsprites.update()
    screen.fill((0,0,0))
    allsprites.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    time.sleep(0.0018)
