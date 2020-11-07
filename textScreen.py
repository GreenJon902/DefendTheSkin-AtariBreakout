from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class TextScreen(Screen):
    text = StringProperty("__text__")

    def on_touch_up(self, touch):
        self.parent.current = "MainMenu"


class HowToPlayScreen(TextScreen):
    pass


class FurtherReadingScreen(TextScreen):
    pass


class HowIsItRelatedToTheSkinImmuneSystemScreen(TextScreen):
    pass
