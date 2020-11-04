from kivy.uix.screenmanager import ScreenManager as Sm, FadeTransition

from configurables import fadeLength
from mainMenuScreen import MainMenuScreen
from playScreen import PlayScreen

from atariBricks import AtariBricks
from ball import Ball
from background import Background
from racket import Racket
from bigBrick import BigBrick


class ScreenManager(Sm):
    def __init__(self):
        super(ScreenManager, self).__init__()

        self.MainMenu = MainMenuScreen(name="MainMenu")
        self.add_widget(self.MainMenu)

        self.PlayScreen = PlayScreen(name="Play")
        self.add_widget(self.PlayScreen)

        self.transition = FadeTransition(duration=fadeLength)
