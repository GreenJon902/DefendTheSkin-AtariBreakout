from kivy.uix.screenmanager import Screen


class PlayScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(PlayScreen, self).__init__(*args, **kwargs)

        self.ball = self.ids["Ball"]
        self.bind(size=self.ball.update_size)

        self.bigBrick = self.ids["BigBrick"]
        self.bigBrick.swipeDownCallback = self.ids["Racket"].swipe_down

        self.racket = self.ids["Racket"]
        self.racket.doesBrickFitCallback = self.brick_fit

        self.atariBricks = self.ids["AtariBricks"]

        self.health = self.ids["Health"]
        self.bind(size=self.health.update)

        self.ball.looseHeart = self.health.loose

    def on_enter(self):
        self.atariBricks.open()
        self.ball.update_size()


    def atari_opening_done(self):
        self.ball.appear(self.ball_opening_done)

    def ball_opening_done(self, _, _2):
        self.ball.start(self.ids["Racket"], self.brick_hit)

    def brick_fit(self, itDoes):
        if itDoes:
            pos = self.bigBrick.exit()
            self.ball.remove(pos[0])
            self.atariBricks.hide_brick(*pos)
            self.parent.score += 1


        else:
            self.bigBrick.racket_missed()

    def brick_hit(self, brickX, brickY):
        self.atariBricks.darken_brick(brickX, brickY, self.bigBrick.exit)
        self.bigBrick.append_to_queue((brickX, brickY))
