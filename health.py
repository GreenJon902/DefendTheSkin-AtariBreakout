from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

from configurables import heartSize, healthDistance, healthLeaveTime, healthGrowSize


class Health(Widget):
    health = NumericProperty(3)

    def __init__(self, *args, **kwargs):
        super(Health, self).__init__(*args, **kwargs)

        self.open_score_screen = None

        self.bind(health=self.update)

    def update(self, _=None, _2=None, _3=None):
        self.ids["heart_1"].size = self.parent.height * heartSize, self.parent.height * heartSize
        self.ids["heart_2"].size = self.parent.height * heartSize, self.parent.height * heartSize
        self.ids["heart_3"].size = self.parent.height * heartSize, self.parent.height * heartSize

        self.ids["heart_1"].right = self.parent.width - (self.parent.height * healthDistance)
        self.ids["heart_1"].top = self.parent.height - (self.parent.height * healthDistance)

        self.ids["heart_2"].right = self.parent.width - (self.parent.height * heartSize) - (
                    self.parent.width * healthDistance * 2)
        self.ids["heart_2"].top = self.parent.height - (self.parent.height * healthDistance)

        self.ids["heart_3"].right = self.parent.width - (self.parent.height * heartSize * 2) - (
                    self.parent.width * healthDistance * 3)
        self.ids["heart_3"].top = self.parent.height - (self.parent.height * healthDistance)

        self.ids["heart_1"].texture.min_filter = 'nearest'
        self.ids["heart_1"].texture.mag_filter = 'nearest'

        self.ids["heart_2"].texture.min_filter = 'nearest'
        self.ids["heart_2"].texture.mag_filter = 'nearest'

        self.ids["heart_3"].texture.min_filter = 'nearest'
        self.ids["heart_3"].texture.mag_filter = 'nearest'

        if self.health == 2:
            a = Animation(opacity=0,
                          width=self.parent.width * heartSize * healthGrowSize,
                          height=self.parent.width * heartSize * healthGrowSize,
                          x=self.ids["heart_3"].x - ((self.parent.width * heartSize * healthGrowSize) / 4),
                          y=self.ids["heart_3"].y - ((self.parent.width * heartSize * healthGrowSize) / 4),
                          duration=healthLeaveTime)

            a.start(self.ids["heart_3"])

        if self.health == 1:
            a = Animation(opacity=0,
                          width=self.parent.width * heartSize * healthGrowSize,
                          height=self.parent.width * heartSize * healthGrowSize,
                          x=self.ids["heart_2"].x - ((self.parent.width * heartSize * healthGrowSize) / 4),
                          y=self.ids["heart_2"].y - ((self.parent.width * heartSize * healthGrowSize) / 4),
                          duration=healthLeaveTime)

            a.start(self.ids["heart_2"])

        if self.health == 0:
            a = Animation(opacity=0,
                          width=self.parent.width * heartSize * healthGrowSize,
                          height=self.parent.width * heartSize * healthGrowSize,
                          x=self.ids["heart_1"].x - ((self.parent.width * heartSize * healthGrowSize) / 4),
                          y=self.ids["heart_1"].y - ((self.parent.width * heartSize * healthGrowSize) / 4),
                          duration=healthLeaveTime)
            a.bind(on_complete=lambda _=None, _2=None, _3=None: self.open_score_screen("Loose"))
            a.start(self.ids["heart_1"])


    def loose(self):
        for body in self.parent.AntiBodiesHolder.children:
            body.remove()

        self.parent.AntiBodiesHolder.clear_widgets()

        self.health -= 1
        i = False if self.health <= 0 else True
        return i
