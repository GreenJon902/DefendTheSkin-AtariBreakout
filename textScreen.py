from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class TextScreen(Screen):
    text = StringProperty("__text__")


class HowToPlayScreen(TextScreen):
    pass


class FurtherReadingScreen(TextScreen):
    pass


class HowItsRelatedToTheSkinImmuneSystemScreen(TextScreen):
    pass
