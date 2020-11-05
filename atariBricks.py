from copy import copy

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import *
from kivy.properties import DictProperty
from kivy.uix.widget import Widget

from configurables import atariGridPos, atariGridSize, atariGridShape, atariColorGrid, brickOpeningDelay, \
    brickFallTime, atariIdToPosGridInverted, brickFallTransition, posToAtariIdGrid, atariHitColorChange, \
    atariHitRegenTime


class AtariBricks(Widget):
    darkened = DictProperty()

    def __init__(self, *args, **kwargs):
        super(AtariBricks, self).__init__(*args, **kwargs)

        self.hasOpened = True
        self.openingBrick = Widget()
        self.openedTimes = 0
        self.currentOpeningPos = 0, 0
        self.openedTimesMax = (atariGridShape[0] * atariGridShape[1]) - 1

        self.pos_hint = atariGridPos
        self.size_hint = atariGridSize

        self.atariBrickSize = 0, 0
        self.atariGrid = {}

        for i in range(atariGridShape[0] * atariGridShape[1]):
            self.darkened[i] = 1

        for brickX in range(atariGridShape[0]):
            self.atariGrid[brickX] = {}
            for brickY in range(atariGridShape[1]):
                self.atariGrid[brickX][brickY] = {"visible": False, "color": atariColorGrid[brickY]}

        self.bind(size=self.update_canvas)
        self.bind(size=self.update_atari_brick_size)

    def update_canvas(self, _=None, _size=None, _2=None):
        self.canvas.clear()

        with self.canvas:
            for brickX in self.atariGrid:
                for brickY in self.atariGrid[brickX]:
                    Color(*self.atariGrid[brickX][brickY]["color"], v=self.darkened[posToAtariIdGrid[brickX][brickY]])
                    if self.atariGrid[brickX][brickY]["visible"]:
                        Rectangle(pos=(brickX * self.atariBrickSize[0] + self.pos[0],
                                       brickY * self.atariBrickSize[1] + self.pos[1]),
                                  size=self.atariBrickSize)

        if not self.hasOpened:
            with self.canvas:
                Color(*self.atariGrid[self.currentOpeningPos[0]][self.currentOpeningPos[1]]["color"])
                Rectangle(pos=(self.currentOpeningPos[0] * self.atariBrickSize[0] + self.pos[0],
                               self.currentOpeningPos[1] * self.atariBrickSize[1] + self.openingBrick.y),
                          size=self.atariBrickSize)

    def update_atari_brick_size(self, _=None, _size=None):
        self.atariBrickSize = Window.size[0] * atariGridSize[0] / atariGridShape[0], \
                              Window.size[1] * atariGridSize[1] / atariGridShape[1]

    def open(self):
        self.hasOpened = False

        self.add_widget(self.openingBrick)
        Clock.schedule_once(self.open_brick, brickOpeningDelay)

    def open_brick(self, _=None, _2=None):
        self.openingBrick.y = self.parent.height

        if self.openedTimes == self.openedTimesMax:
            self.hasOpened = True
            self.remove_widget(self.openingBrick)

            self.atariGrid[atariIdToPosGridInverted[self.openedTimes][0]] \
                [atariIdToPosGridInverted[self.openedTimes][1]]["visible"] = True

            self.parent.atari_opening_done()

        else:
            Clock.schedule_once(self._open_brick, 0)

            self.atariGrid[atariIdToPosGridInverted[self.openedTimes][0]] \
                [atariIdToPosGridInverted[self.openedTimes][1]]["visible"] = True

            self.openedTimes += 1
            try:
                self.currentOpeningPos = atariIdToPosGridInverted[self.openedTimes]
            except KeyError:
                pass

    def _open_brick(self, _=None):
        a = Animation(y=self.parent.height * atariGridPos["y"], duration=brickFallTime,
                      t=brickFallTransition)
        a.bind(on_complete=self.open_brick)
        a.bind(on_progress=self.update_canvas)
        a.start(self.openingBrick)

    def darken_brick(self, brickX, brickY, regenedCallback):
        self.darkened[posToAtariIdGrid[brickX][brickY]] = 1 - atariHitColorChange

        d = copy(self.darkened)
        d[posToAtariIdGrid[brickX][brickY]] = 1

        a = Animation(darkened=d, duration=atariHitRegenTime)
        a.bind(on_progress=self.update_canvas)
        a.bind(on_complete=(lambda _=None, _2=None, _3=None:
                            regenedCallback() if self.atariGrid[brickX][brickY]["visible"] else _))
        a.start(self)

    def hide_brick(self, brickX, brickY):
        self.atariGrid[brickX][brickY]["visible"] = False

        self.update_canvas()

