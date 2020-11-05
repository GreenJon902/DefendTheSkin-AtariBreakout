from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager as Sm, FadeTransition

from configurables import fadeLength
from mainMenuScreen import MainMenuScreen
from playScreen import PlayScreen

from atariBricks import AtariBricks
from ball import Ball
from background import Background
from racket import Racket
from bigBrick import BigBrick
from health import Health


class ScreenManager(Sm):
    def __init__(self):
        super(ScreenManager, self).__init__()

        self.MainMenu = MainMenuScreen(name="MainMenu")
        self.add_widget(self.MainMenu)

        self.PlayScreen = PlayScreen(name="Play")
        self.PlayScreen.ids["Health"].resetCallback = self.reset
        self.add_widget(self.PlayScreen)

        self.transition = FadeTransition(duration=fadeLength)

    def reset(self, _=None, _2=None, _3=None):
        print(self.PlayScreen.ids)