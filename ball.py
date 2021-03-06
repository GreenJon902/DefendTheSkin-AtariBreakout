import bisect
from random import randint

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.vector import Vector

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
    velocityX = 1 if randint(0, 1) == 1 else -1
    velocityY = -1
    speed = ballStartSpeed

    def move(self):
        self.pos = (Vector(self.velocityX, self.velocityY) * ballStartSpeed + self.pos)

    # Ball
    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)

        self.opacity = 0
        self.size = 0, 0

        self.racket = None
        self.hideBrickFunc = None
        self.looseHeart = None
        self.canBounce = True
        self.canLooseHealth = True
        self.open_score_screen = None
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

    def update(self, _=None):
        self.move()

        # Hit Boxes YAY

        # Racket
        if self.canBounce and self.collide_widget(self.racket):
            self.canBounce = False

            vx, vy = self.velocityX, self.velocityY
            offset = (self.center_x - self.racket.center_x) / (self.racket.width / 2)
            bounced = Vector(vx, vy * -1)
            vel = bounced * ballSpeedUp
            self.velocityX, self.velocityY = vel.x, vel.y + offset
            self.canBounce = False

        elif not self.collide_widget(self.racket) and not self.canBounce:
            self.canBounce = True

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
                        self.velocityY *= -1

                        pass


                if shouldBreak:
                    break

        # Sides
        if self.x <= 0:
            self.velocityX *= -1
            self.x = 1

        elif self.right >= Window.width:
            self.velocityX *= -1
            self.right = Window.width

        # Bottom
        if self.y <= 0 and self.canLooseHealth:
            if self.looseHeart():
                self.center = self.parent.width / 2, self.parent.height / 2
                self.appear(self.regen)
                self.canLooseHealth = False


        # Top
        if self.y >= self.parent.height:
            self.open_score_screen("Win")


    def remove(self, x):
        self.atariGrid[x] -= 1

    def regen(self, _=None, _2=None):
        self.velocityX = 1 if randint(0, 1) == 1 else -1
        self.velocityY = -1
        self.canLooseHealth = True
