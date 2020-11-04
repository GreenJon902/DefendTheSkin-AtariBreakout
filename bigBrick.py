from random import randint

from kivy.animation import Animation
from kivy.graphics import *
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.widget import Widget

from configurables import atariColorGrid, racketSize, bigBrickHoleColorChange, \
    bigBrickMoveTime, bigBrickFlashTime, bigBrickFlashTransition


class BigBrick(Widget):
    brickQueue = ListProperty()
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(0)
    r2 = NumericProperty(0)
    g2 = NumericProperty(0)
    b2 = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(BigBrick, self).__init__(*args, **kwargs)

        self.bind(brickQueue=self.update_canvas)
        self.bind(size=self.update_queue_sizes)
        self.bind(size=self.update_canvas)
        self.bind(pos=self.update_canvas)
        self.update_canvas()

        self.swipeDownCallback = None
        self.notSwipeDowned = True

    def enter(self, base_widget):
        self.append_to_queue((1, 3))
        self.append_to_queue((2, 2))

    def update_canvas(self, _=None, _1=None, _2=None):
        self.canvas.clear()

        if len(self.brickQueue) == 0:
            pass

        else:
            with self.canvas:

                Color(self.r, self.g, self.b)
                Rectangle(pos=self.pos, size=self.size)

                Color(self.r2, self.g2, self.b2)
                Rectangle(pos=(self.x + self.brickQueue[0]["holePos"],
                               self.height - (self.parent.height * racketSize[1]) + self.y),
                          size=(self.parent.width * racketSize[0], self.parent.height * racketSize[1]))

    def append_to_queue(self, pos):
        length = len(self.brickQueue)

        self.brickQueue.append({"brickPos": pos,
                                "holePos": randint(0, int(self.width - (self.width * racketSize[0])))})

        if length == 0:
            print("None")
            self.enter()

    def update_queue_sizes(self, _=None, _2=None):
        for brick in range(len(self.brickQueue)):
            self.brickQueue[brick]["holePos"] = randint(0, int(self.width - (self.width * racketSize[0])))

    def on_touch_move(self, touch):
        if "y" in self.pos_hint:
            if self.collide_point(*touch.pos) and self.notSwipeDowned:
                self.notSwipeDowned = False

                self.swipeDownCallback(self.brickQueue[0]["holePos"] + self.x,
                                       self.height - (self.parent.height * racketSize[1]),
                                       self.height)

            elif not self.collide_point(*touch.pos) and not self.notSwipeDowned:
                self.notSwipeDowned = True

    def exit(self):
        del self.pos_hint["y"]
        self.y = 0

        a = Animation(y=self.height * -1, duration=bigBrickMoveTime)
        a.bind(on_complete=self.has_hidden)
        a.start(self)

        return self.brickQueue[0]["brickPos"]

    def enter(self):
        self.r, self.g, self.b = atariColorGrid[self.brickQueue[0]["brickPos"][1]]
        self.r2, self.g2, self.b2 = Color(*atariColorGrid[self.brickQueue[0]["brickPos"][1]],
                                          v=1 - bigBrickHoleColorChange).rgb

        del self.pos_hint["y"]
        self.y = self.height * -1

        a = Animation(y=0, duration=bigBrickMoveTime)
        a.bind(on_complete=self.has_shown)
        a.start(self)

    def has_shown(self, _=None, _2=None):
        self.pos_hint["y"] = 0

    def has_hidden(self, _=None, _2=None):
        del self.brickQueue[0]

        self.pos_hint["y"] = self.height * -1

        if len(self.brickQueue) != 0:
            self.enter()

    def racket_missed(self):
        r = self.r
        g = self.g
        b = self.b

        self.r = 1
        self.g = 0
        self.b = 0

        r2 = self.r2
        g2 = self.g2
        b2 = self.b2

        self.r2 = 1
        self.g2 = 0
        self.b2 = 0

        a = Animation(r=r, g=g, b=b, r2=r2, g2=g2, b2=b2, duration=bigBrickFlashTime,
                      transition=bigBrickFlashTransition)
        a.bind(on_progress=self.update_canvas)
        a.start(self)
