# Constantes globales
WIDTH = 1640
HEIGHT = 1480
SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50

class GameObject:

    def __init__(self, image, height, speed):

        self.speed = speed

        self.image = image

        self.pos = image.get_rect().move(0, height)

    def move(self, up=False, down=False, left=False, right=False):

        if right:

            self.pos.right += self.speed

        if left:

            self.pos.right -= self.speed

        if down:

            self.pos.top += self.speed

        if up:

            self.pos.top -= self.speed

        if self.pos.right > WIDTH:

            self.pos.left = 0

        if self.pos.top > HEIGHT-SPRITE_HEIGHT:

            self.pos.top = 0

        if self.pos.right < SPRITE_WIDTH:

            self.pos.right = WIDTH

        if self.pos.top < 0:

           self.pos.top = HEIGHT-SPRITE_HEIGHT