from kivy import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')


from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

from audio import Audio
from screenManager import ScreenManager


class DefendTheSkin(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.audio = Audio()

    def build(self):
        Window.minimum_width = 650
        Window.minimum_height = 670

        Window.size = 700, 1000

        self.audio.play()

        return ScreenManager()



if __name__ == '__main__':
    Builder.load_file("Resources/kv.kv")

    defendTheSkin = DefendTheSkin()
    defendTheSkin.run()
