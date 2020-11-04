from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

from screenManager import ScreenManager
from audio import Audio


class DefendTheSkin(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.audio = Audio()

    def build(self):
        Window.minimum_width = 500
        Window.minimum_height = 500

        Window.size = 700, 1000

        self.audio.play()

        return ScreenManager()


if __name__ == '__main__':
    Builder.load_file("kv.kv")

    defendTheSkin = DefendTheSkin()
    defendTheSkin.run()
