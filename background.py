from kivy.graphics import *
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget

from configurables import bgBloodColor, bgSkinColor1, bgSkinBottom, bgSkinTop, bgSkinColor2, atariGridSize


class Background(Widget):
    playing = BooleanProperty(False)
    mouseOver = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(Background, self).__init__(*args, **kwargs)

        self.bind(size=self.update)
        self.bind(mouseOver=self.update)

    def update(self, _, size):
        with self.canvas:
            self.canvas.clear()

            if self.playing or self.mouseOver:
                Color(*bgSkinColor2)
                Rectangle(pos=(0, self.height*bgSkinBottom),
                          size=(self.width, self.height*bgSkinTop))

            else:
                Color(*bgSkinColor1)
                Rectangle(pos=(0, self.height * bgSkinBottom),
                          size=(self.width, self.height * bgSkinTop))


            Color(*bgBloodColor)
            Rectangle(pos=(0, self.height * bgSkinTop), size=(self.width, self.height * (1 - bgSkinTop)))

