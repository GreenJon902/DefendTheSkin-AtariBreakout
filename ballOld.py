import bisect

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from configurables import ballSize, bgSkinBottom, atariGridPos, atariGridSize, atariGridShape, \
    ballSpeedUp, ballStartSpeed


def round_down_to_set_out_puts(n, outputs):
    if n < outputs[0]:
        print("wtf, im worried noe, my code is crap")

    i = bisect.bisect_right(outputs, n)
    return outputs[i-1]


class Ball(Widget):
    #  Physics
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = (Vector(self.velocity[0], self.velocity[1]) * ballStartSpeed + self.pos)

    # Ball
    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)

        self.opacity = 0
        self.size = 0, 0

        self.racket = None
        self.hideBrickFunc = None
        self.can_bounce = True
        self.atariGrid = {}
        self.atariGridXCoords = {}
        self.atariGridXWidth = 0
        self.atariGridYCoords = {}

        for brickX in range(atariGridShape[0] + 1):  # +1 because of hitboxes things
            self.atariGrid[brickX] = atariGridShape[1]

    def update_size(self, _=None, _2=None):
        if self.opacity != 0:
            self.size = ballSize * Window.width, ballSize * Window.width

        for brickX in range(atariGridShape[0]):
            self.atariGridXCoords[brickX] = (Window.size[0] * atariGridSize[0] / atariGridShape[0]) * brickX + \
                                            Window.width * atariGridPos["x"]

        self.atariGridXWidth = Window.size[0] * atariGridSize[0] / atariGridShape[0]

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
        self.velocity_y = -1
        self.velocity_x = -1
        self.racket = racket
        self.hideBrickFunc = hideBrickFunc

        Clock.schedule_interval(self.update, 0)

    def update(self, _=None):
        self.move()

        # Hit Boxes YAY

        # Racket
        if self.can_bounce and self.collide_widget(self.racket):
            vx, vy = self.velocity
            offset = (self.center_x - self.racket.center_x) / (self.racket.width / 2)
            bounced = Vector(vx, vy * -1)
            vel = bounced * ballSpeedUp
            self.velocity = vel.x, vel.y + offset
            self.can_bounce = False

        elif not self.collide_widget(self.racket) and not self.can_bounce:
            self.can_bounce = True


        if self.top >= self.parent.height * bgSkinBottom:

            # Side Skin
            if (self.x < (Window.width * atariGridPos["x"]) or
                    self.right > (Window.width * (atariGridPos["x"] + atariGridSize[0]))):
                self.velocity_y *= -1

            elif ((self.x < (Window.width * atariGridPos["x"]) < self.right) or
                  (self.right > (Window.width * atariGridPos["x"] + atariGridSize[0]) > self.x)):
                self.velocity_x *= -1


            # AtariGrid Y
            else:
                shouldBreak = False

                for brickY in range(atariGridShape[1]):

                    for brickX in range(atariGridShape[0]):
                        if (atariGridShape[1] - brickY == self.atariGrid[brickX]) and \
                                (self.atariGridXCoords[brickX] <= self.x <= (
                                        self.atariGridXCoords[brickX] + self.atariGridXWidth)) and (
                                self.atariGridXCoords[brickX] <= self.right <= (
                                self.atariGridXCoords[brickX] + self.atariGridXWidth)):

                            if self.top >= self.atariGridYCoords[brickY]:
                                self.atariGrid[brickX] -= 1
                                self.hideBrickFunc(brickX, self.atariGrid[brickX])

                                self.velocity_y *= -1

                                shouldBreak = True
                                break

                        elif (atariGridShape[1] - brickY == self.atariGrid[brickX]) and \
                                (self.atariGrid[brickX] == self.atariGrid[brickX + 1]) and \
                                (self.atariGridXCoords[brickX] <= self.center_x <= (
                                        self.atariGridXCoords[brickX] + self.atariGridXWidth)):

                            if self.top >= self.atariGridYCoords[brickY]:
                                self.atariGrid[brickX] -= 1
                                self.hideBrickFunc(brickX, self.atariGrid[brickX])

                                self.velocity_y *= -1

                                shouldBreak = True
                                break

                        elif (atariGridShape[1] - brickY == self.atariGrid[brickX]) and \
                                (self.atariGrid[brickX] > self.atariGrid[brickX + 1]) and \
                                (self.atariGridXCoords[brickX] <= self.center_x <= (
                                        self.atariGridXCoords[brickX] + self.atariGridXWidth)):

                            if self.top >= self.atariGridYCoords[brickY]:
                                self.atariGrid[brickX] -= 1
                                self.hideBrickFunc(brickX, self.atariGrid[brickX])

                                self.velocity_y *= -1

                                shouldBreak = True
                                break

                    if shouldBreak:
                        break

        # Sides
        if self.x <= 0:
            self.velocity_x *= -1

        elif self.right >= Window.width:
            self.velocity_x *= -1
