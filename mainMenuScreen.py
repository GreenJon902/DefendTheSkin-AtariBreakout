from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

from configurables import buttonColorChange


class MainMenuScreen(Screen):
    b1Color = ListProperty([1, 1, 1])
    b2Color = ListProperty([1, 1, 1])
    b3Color = ListProperty([1, 1, 1])

    def __init__(self, *args, **kwargs):
        super(MainMenuScreen, self).__init__(*args, **kwargs)

        self.sm = None



        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, _, pos):
        if self.ids["PlayButton"].collide_point(*pos):
            self.ids["bg"].mouseOver = True

        elif not self.ids["PlayButton"].collide_point(*pos):
            self.ids["bg"].mouseOver = False

        if self.ids["HowToPlay"].collide_point(*pos):
            self.b1Color = buttonColorChange

        elif not self.ids["HowToPlay"].collide_point(*pos):
            self.b1Color = 1, 1, 1

        if self.ids["HowIsItRelatedToTheSkinImmuneSystem"].collide_point(*pos):
            self.b2Color = buttonColorChange

        elif not self.ids["HowIsItRelatedToTheSkinImmuneSystem"].collide_point(*pos):
            self.b2Color = 1, 1, 1

        if self.ids["FurtherReading"].collide_point(*pos):
            self.b3Color = buttonColorChange

        elif not self.ids["FurtherReading"].collide_point(*pos):
            self.b3Color = 1, 1, 1

    def start_game(self):
        self.parent.current = "Play"

    def further_buttons_set_screen(self, s):
        self.sm.current = s
