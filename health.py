from kivy.uix.widget import Widget

from configurables import heartSize, healthDistance


class Health(Widget):
    def __init__(self, *args, **kwargs):
        super(Health, self).__init__(*args, **kwargs)

    def update(self, _=None, _2=None, _3=None):
        self.ids["heart_1"].size = self.parent.width * heartSize, self.parent.width * heartSize
        self.ids["heart_2"].size = self.parent.width * heartSize, self.parent.width * heartSize
        self.ids["heart_3"].size = self.parent.width * heartSize, self.parent.width * heartSize

        self.ids["heart_1"].right = self.parent.width - (self.parent.width * healthDistance)
        self.ids["heart_1"].top = self.parent.height - (self.parent.height * healthDistance)

        self.ids["heart_2"].right = self.parent.width - (self.parent.width * heartSize) - (self.parent.width * healthDistance * 2)
        self.ids["heart_2"].top = self.parent.height - (self.parent.height * healthDistance)

        self.ids["heart_3"].right = self.parent.width - (self.parent.width * heartSize * 2) - (self.parent.width * healthDistance * 3)
        self.ids["heart_3"].top = self.parent.height - (self.parent.height * healthDistance)
