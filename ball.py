import bisect
import math
from random import randint

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget

from configurables import ballSize, bgSkinBottom, atariGridPos, atariGridSize, atariGridShape, \
    ballSpeedUp, ballStartSpeed


def round_down_to_set_out_puts(n, outputs):
    if n < outputs[0]:
        print("wtf, im worried noe, my code is crap")
        return outputs[0]

    i = bisect.bisect_right(outputs, n)
    return outputs[i - 1]


def round_up_to_set_out_puts(n, outputs):
    if n > outputs[-1]:
        print("wtf, im worried noe, my code is crap")
        return outputs[-1]

    i = bisect.bisect_right(outputs, n)
    try:
        return outputs[i + 1]
    except IndexError:
        return outputs[-1]


class Ball(Widget):
    #  Physics
    direction = -45 if randint(0, 1) == 0 else 45
    speed = ballStartSpeed

    def move(self):
        direction_radians = math.radians(self.direction)

        self.center_x += self.speed * math.sin(direction_radians)
        self.center_y -= self.speed * math.cos(direction_radians)

    # Ball
    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)

        self.opacity = 0
        self.size = 0, 0

        self.racket = None
        self.hideBrickFunc = None
        self.looseHeart = None
        self.can_bounce = True
        self.atariGrid = {}
        self.atariGridXCoords = {}
        self.atariGridRightCoords = {}
        self.atariGridXWidth = 0
        self.atariGridYCoords = {}

        for brickX in range(atariGridShape[0]):
            self.atariGrid[brickX] = atariGridShape[1]

    def update_size(self, _=None, _2=None):
        if self.opacity != 0:
            self.size = ballSize * Window.width, ballSize * Window.width

        for brickX in range(atariGridShape[0]):
            self.atariGridXCoords[brickX] = (Window.size[0] * atariGridSize[0] / atariGridShape[0]) * brickX + \
                                            Window.width * atariGridPos["x"]

        self.atariGridXWidth = Window.size[0] * atariGridSize[0] / atariGridShape[0]

        for brickX in range(atariGridShape[0]):
            self.atariGridRightCoords[brickX] = self.atariGridXCoords[brickX] + self.atariGridXWidth

        for brickY in range(atariGridShape[1]):
            self.atariGridYCoords[brickY] = (Window.size[1] * atariGridSize[1] / atariGridShape[1]) * brickY + \
                                            Window.height * atariGridPos["y"]


    def appear(self, ball_opening_done):
        self.size = 0, 0
        self.x = self.x + ((ballSize * Window.width) / 2)
        self.y = self.y + ((ballSize * Window.width) / 2)

        a = Animation(opacity=1,
                      size=(ballSize * Window.width,
                            ballSize * Window.width),
                      x=self.x - ((ballSize * Window.width) / 2),
                      y=self.y - ((ballSize * Window.width) / 2))
        a.bind(on_complete=ball_opening_done)
        a.start(self)

    def start(self, racket, hideBrickFunc):
        self.racket = racket
        self.hideBrickFunc = hideBrickFunc

        Clock.schedule_interval(self.update, 0)

    def bounce(self, diff):
        self.speed *= ballSpeedUp

        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self, _=None):
        self.move()

        # Hit Boxes YAY

        # Racket
        if self.can_bounce and self.collide_widget(self.racket):
            self.can_bounce = False

            offset = (self.center_x - self.racket.center_x) / (self.racket.width / 2)
            self.bounce(offset)

            #self.velocity_y *= -1

        elif not self.collide_widget(self.racket) and not self.can_bounce:
            self.can_bounce = True

        if self.top >= self.parent.height * bgSkinBottom:
            # AtariGrid Y
            shouldBreak = False

            for brickX in range(atariGridShape[0]):
                for brickY in range(self.atariGrid[brickX]):
                    x = self.atariGridXCoords[brickX]
                    x2 = self.atariGridRightCoords[brickX]
                    y = self.atariGridYCoords[atariGridShape[1] - brickY - 1]

                    if ((x <= self.x <= x2) or (x <= self.right <= x2)) and self.top >= y:
                        shouldBreak = True
                        self.top = y-1
                        self.hideBrickFunc(brickX, atariGridShape[1] - brickY - 1)

                        self.bounce(0)


                if shouldBreak:
                    break

        # Sides
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        elif self.right >= Window.width:
            self.direction = (360 - self.direction) % 360
            self.right = Window.width

        # Bottom
        if self.y <= 0:
            if self.looseHeart():
                self.center = self.parent.width / 2, self.parent.height / 2


    def remove(self, x):
        self.atariGrid[x] -= 1

