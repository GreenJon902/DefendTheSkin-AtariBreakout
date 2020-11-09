from kivy.uix.screenmanager import Screen


class ScoreScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(ScoreScreen, self).__init__(*args, **kwargs)

        self.score = 0
        self.text = "Loose"

    def on_pre_enter(self, *args):
        self.ids["Score"].text = "Your Score Is {}".format(self.score)
        self.ids["Title"].text = "You {}!".format(self.title)

    def next(self):
        self.parent.current = "MainMenu"
