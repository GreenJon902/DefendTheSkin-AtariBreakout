from kivy.clock import Clock
from kivy.core.audio import SoundLoader


class Audio:
    def __init__(self):
        self.sound = SoundLoader.load("Resources/backingTrack.mp3")

    def loop(self, _=None):
        self.sound.play()

    def play(self):
        self.sound.play()
        Clock.schedule_interval(self.loop, self.sound.length + 5)
