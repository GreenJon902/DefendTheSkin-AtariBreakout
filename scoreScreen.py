from kivy.uix.screenmanager import Screen


class ScoreScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(ScoreScreen, self).__init__(*args, **kwargs)

        self.score = 0

    def on_pre_enter(self, *args):
        self.ids["Score"].text = "Your Score Is {}".format(self.score)
