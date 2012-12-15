import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

sound = pygame.mixer.Sound("/usr/share/pyshared/pygame/examples/data/whiff.wav")

clock = pygame.time.Clock()

def randomdirection():
    return random.choice((-1, 1))

def randomspeed():
    return random.randint(2, 5)

class Ball(pygame.sprite.Sprite):

    def __init__(self, area):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/usr/share/doc/python-pygame/tut/intro/ball.gif").convert()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(random.randint(0, area.right - 1 - self.rect.right),
                                   random.randint(0, area.bottom - 1 -self.rect.bottom))
        self.area = area
        self.x_direction = randomdirection()
        self.y_direction = randomdirection()
        self.x_speed = randomspeed()
        self.y_speed = randomspeed()

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

        self.rect = self.rect.move(self.x_direction * self.x_speed, self.y_direction * self.y_speed)

ball = Ball(pygame.display.get_surface().get_rect())
allsprites = pygame.sprite.RenderPlain((ball))

while True:

    allsprites.update()
    screen.fill((0,0,0))
    allsprites.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            allsprites.add(Ball(pygame.display.get_surface().get_rect()))

    clock.tick(80)
