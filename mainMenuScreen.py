from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from configurables import buttonColorChange


class MainMenuScreen(Screen):
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
            self.ids["HowToPlay"].background_color = buttonColorChange

        elif not self.ids["HowToPlay"].collide_point(*pos):
            self.ids["HowToPlay"].background_color = 1, 1, 1, 0

        if self.ids["HowIsItRelatedToTheSkinImmuneSystem"].collide_point(*pos):
            self.ids["HowIsItRelatedToTheSkinImmuneSystem"].background_color = buttonColorChange

        elif not self.ids["HowIsItRelatedToTheSkinImmuneSystem"].collide_point(*pos):
            self.ids["HowIsItRelatedToTheSkinImmuneSystem"].background_color = 1, 1, 1, 0

        if self.ids["FurtherReading"].collide_point(*pos):
            self.ids["FurtherReading"].background_color = buttonColorChange

        elif not self.ids["FurtherReading"].collide_point(*pos):
            self.ids["FurtherReading"].background_color = 1, 1, 1, 0

    def start_game(self):
        self.parent.current = "Play"

    def further_buttons_set_screen(self, s):
        self.sm.current = s
