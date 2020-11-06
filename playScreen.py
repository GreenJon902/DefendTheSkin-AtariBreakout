from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from bodies import create_anti, create_antianti, anti_bodies
from configurables import atariGridSize, atariGridPos, atariGridShape, antiBodyCreationTime


class PlayScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(PlayScreen, self).__init__(*args, **kwargs)

        for body in anti_bodies:
            body.remove()

        self.ball = self.ids["Ball"]
        self.bind(size=self.ball.update_size)

        self.bigBrick = self.ids["BigBrick"]
        self.bigBrick.swipeDownCallback = self.ids["Racket"].swipe_down

        self.racket = self.ids["Racket"]
        self.racket.doesBrickFitCallback = self.brick_fit
        self.racket.bigBrick = self.bigBrick
        self.racket.antiBodies = anti_bodies

        self.atariBricks = self.ids["AtariBricks"]

        self.health = self.ids["Health"]
        self.bind(size=self.health.update)

        self.ball.looseHeart = self.health.loose
        self.racket.looseHeart = self.health.loose

    def on_enter(self):
        self.atariBricks.open()
        self.ball.update_size()

        Clock.schedule_interval(lambda _=None: create_anti(self, (self.width / 2, self.height / 2)),
                                antiBodyCreationTime)

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

            create_antianti(self, ((Window.size[0] * atariGridSize[0] / atariGridShape[0]) * pos[0] + ((Window.size[0] * atariGridSize[0] / atariGridShape[0])/2) +
                                   Window.width * atariGridPos["x"],
                                   (Window.size[1] * atariGridSize[1] / atariGridShape[1]) * pos[1] + ((Window.size[1] * atariGridSize[1] / atariGridShape[1])/2) +
                                   Window.height * atariGridPos["y"]))

        else:
            create_anti(self, (self.width / 2, self.height / 2))
            print("fe")

            self.bigBrick.racket_missed()

    def brick_hit(self, brickX, brickY):
        self.atariBricks.darken_brick(brickX, brickY, self.regen)
        self.bigBrick.append_to_queue((brickX, brickY))

    def regen(self):
        create_anti(self, (self.width / 2, self.height / 2))
        self.bigBrick.exit()
