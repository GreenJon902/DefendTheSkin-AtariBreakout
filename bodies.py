import math
from random import random

from kivy import Logger
from kivy.clock import Clock
from kivy.graphics import *
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from configurables import bodyRadius, bodyColors, antiantiBodyAmount, antiBodyDirectionChangeMax, \
    antiBodyDirectionChangeMax2, bodyMoveSpeed, bgSkinBottom, antiBodyCreationAmount

anti_bodies = list()


class Body(Widget):
    type = StringProperty("anti")
    types = "anti", "antianti"
    direction = 0

    def __init__(self, direction=int(random() * 360), *args, **kwargs):
        super(Body, self).__init__(*args, **kwargs)

        self.size_hint = bodyRadius, None
        self.move_clock = Clock.schedule_interval(self.move, 0)
        self.direction = direction

        self.bind(pos=self.update_canvas)

    def on_type(self, _, type):
        if type not in self.types:
            Logger.warn("Game: '{}' is not a type, terminating this Body".format(type))
            Clock.schedule_once(self.remove, 0)

    def remove(self, _=None):
        try:
            self.parent.remove_widget(self)
            self.move_clock.cancel()
            anti_bodies.remove(self)
        except ValueError:
            pass
        del self

    def update_canvas(self, _=None, _2=None):
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

            if 0 >= self.center_x >= self.parent.width:
                self.direction = (self.direction + 180) % 360

            elif 0 >= self.center_y >= (self.parent.height * bgSkinBottom):
                self.direction = (self.direction + 180) % 360

            if self.parent.ball.collide_widget(self):
                self.remove()

        else:
            if not self.parent.collide_point(self.x, self.y):
                self.remove()

            else:
                for body in anti_bodies:
                    if self.collide_widget(body):
                        body.remove()

        direction_radians = math.radians(self.direction)

        self.center_x += bodyMoveSpeed * math.sin(direction_radians)
        self.center_y -= bodyMoveSpeed * math.cos(direction_radians)

    def on_width(self, _=None, _2=None):
        self.height = self.width
        self.update_canvas()


def create_anti(parent, pos):
    for body in range(antiBodyCreationAmount):
        b = Body(type="anti", pos=pos)
        parent.add_widget(b)

        anti_bodies.append(b)


def create_antianti(parent, pos):
    directionChange = 1 / antiantiBodyAmount * 360

    for n in range(antiantiBodyAmount):
        parent.add_widget(Body(type="antianti", direction=directionChange * n, pos=pos))
