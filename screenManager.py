from kivy.uix.screenmanager import ScreenManager as Sm, FadeTransition

from configurables import fadeLength
from mainMenuScreen import MainMenuScreen
from playScreen import PlayScreen
from scoreScreen import ScoreScreen

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
        self.PlayScreen.ids["Health"].dead = self.dead
        self.add_widget(self.PlayScreen)

        self.ScoreScreen = ScoreScreen(name="Score")
        self.add_widget(self.ScoreScreen)

        self.transition = FadeTransition(duration=fadeLength)

    def dead(self, _=None, _2=None, _3=None):
        self.current = "Score"

        self.remove_widget(self.PlayScreen)
        self.PlayScreen = PlayScreen(name="Play")
        self.PlayScreen.ids["Health"].dead = self.dead
        self.add_widget(self.PlayScreen)
