from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class MainMenuScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(MainMenuScreen, self).__init__(*args, **kwargs)

        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, _, pos):
        if self.ids["PlayButton"].collide_point(*pos):
            self.ids["bg"].mouseOver = True

        if not self.ids["PlayButton"].collide_point(*pos):
            self.ids["bg"].mouseOver = False

    def start_game(self):
        self.parent.current = "Play"
