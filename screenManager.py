from kivy.uix.screenmanager import ScreenManager as Sm, FadeTransition

from configurables import fadeLength, howToPlayScreenText, furtherReadingScreenText, \
    howIsItRelatedToTheSkinImmuneSystemScreenText
from mainMenuScreen import MainMenuScreen
from playScreen import PlayScreen
from scoreScreen import ScoreScreen
from textScreen import FurtherReadingScreen, HowToPlayScreen, HowIsItRelatedToTheSkinImmuneSystemScreen

from atariBricks import AtariBricks
from ball import Ball
from background import Background
from racket import Racket
from bigBrick import BigBrick
from health import Health


class ScreenManager(Sm):
    def __init__(self):
        super(ScreenManager, self).__init__()

        self.score = 0

        self.MainMenu = MainMenuScreen(name="MainMenu")
        self.add_widget(self.MainMenu)

        self.PlayScreen = PlayScreen(name="Play")
        self.PlayScreen.ids["Health"].open_score_screen = self.open_score_screen
        self.PlayScreen.ids["Ball"].open_score_screen = self.open_score_screen
        self.add_widget(self.PlayScreen)

        self.ScoreScreen = ScoreScreen(name="Score")
        self.add_widget(self.ScoreScreen)

        self.HowToPlayScreen = HowToPlayScreen(name="HowToPlay", text=howToPlayScreenText)
        self.add_widget(self.HowToPlayScreen)
        self.FurtherReadingScreen = FurtherReadingScreen(name="FurtherReading", text=furtherReadingScreenText)
        self.add_widget(self.FurtherReadingScreen)
        self.HowIsItRelatedToTheSkinImmuneSystemScreen = \
            HowIsItRelatedToTheSkinImmuneSystemScreen(name="HowIsItRelatedToTheSkinImmuneSystem",
                                                      text=howIsItRelatedToTheSkinImmuneSystemScreenText)
        self.add_widget(self.HowIsItRelatedToTheSkinImmuneSystemScreen)

        self.transition = FadeTransition(duration=fadeLength)

    def open_score_screen(self, title, _=None, _2=None, _3=None):
        self.ScoreScreen.score = self.score
        self.ScoreScreen.title = title
        self.current = "Score"

        self.remove_widget(self.PlayScreen)
        self.PlayScreen = PlayScreen(name="Play")
        self.PlayScreen.ids["Health"].open_score_screen = self.open_score_screen
        self.add_widget(self.PlayScreen)
        self.score = 0
