import math
from random import random

from kivy import Logger
from kivy.clock import Clock
from kivy.graphics import *
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from configurables import bodyRadius, bodyColors, antiantiBodyAmount, antiBodyDirectionChangeMax, \
    antiBodyDirectionChangeMax2, bodyMoveSpeed, bgSkinBottom, antiBodyCreationAmount


class Body(Widget):
    type = StringProperty("anti")
    types = "anti", "antianti"
    direction = 0

    def __init__(self, looseHealth, AntiBodiesHolder, direction=int(random() * 360), *args, **kwargs):
        super(Body, self).__init__(*args, **kwargs)

        self.size_hint = None, None

        self.move_clock = Clock.schedule_interval(self.move, 0)
        self.direction = direction

        self.looseHealth = looseHealth
        self.AntiBodiesHolder = AntiBodiesHolder

        self.bind(pos=self.update_canvas)

    def on_type(self, _, type):
        if type not in self.types:
            Logger.warn("Game: '{}' is not a type, terminating this Body".format(type))
            Clock.schedule_once(self.remove, 0)

    def remove(self, _=None):
        self.canvas.clear()
        self.move_clock.cancel()
        self.parent.remove_widget(self)

        del self


    def update_canvas(self, _=None, _2=None):
        try:
            if min(self.parent.width, self.parent.height) == self.parent.width:
                self.size = self.parent.width * bodyRadius, self.parent.width * bodyRadius
            else:
                self.size = self.parent.height * bodyRadius, self.parent.height * bodyRadius

        except AttributeError:
            pass


        self.canvas.clear()
        with self.canvas:
            StencilPush()
            Color(*bodyColors[self.type])
            Ellipse(pos=self.pos, size=self.size)

            StencilUse()
            Rectangle(pos=self.pos, size=self.size)

            StencilUnUse()
            StencilPop()

    def move(self, _=None, _2=None):

        if self.type == "anti":
            self.direction = (int(random() * antiBodyDirectionChangeMax2) +
                              self.direction - antiBodyDirectionChangeMax) % 360

            if 0 >= self.center_x:
                self.direction = (self.direction + 180) % 360
                self.x = 0

            elif self.center_x >= self.parent.width:
                self.direction = (self.direction + 180) % 360
                self.right = self.parent.width

            elif 0 >= self.center_y:
                self.direction = (self.direction + 180) % 36
                self.y = 0

            elif self.center_y >= (self.parent.height * bgSkinBottom):
                self.direction = (self.direction + 180) % 36
                self.top = (self.parent.height * bgSkinBottom)

            if self.parent.ball.collide_widget(self):
                self.remove()

            elif self.parent.racket.collide_widget(self):
                self.looseHealth()
                self.remove()

        else:
            if not self.parent.collide_point(self.x, self.y):
                self.remove()

            else:
                for body in self.AntiBodiesHolder.children:
                    if self.collide_widget(body):
                        body.remove()

        direction_radians = math.radians(self.direction)

        self.center_x += bodyMoveSpeed * math.sin(direction_radians)
        self.center_y -= bodyMoveSpeed * math.cos(direction_radians)


def create_anti(parent, pos):
    for body in range(antiBodyCreationAmount):
        b = Body(parent.health.loose, parent.AntiBodiesHolder, type="anti", pos=pos)
        parent.add_widget(b)


def create_antianti(parent, pos):
    directionChange = 1 / antiantiBodyAmount * 360

    for n in range(antiantiBodyAmount):
        parent.add_widget(Body(parent.health.loose, parent.AntiBodiesHolder, type="antianti", direction=directionChange * n, pos=pos))
