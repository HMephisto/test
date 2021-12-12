from kivymd.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder


class Draw(Screen):
    pass

class Draw2(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return Builder.load_file("box.kv")


MyApp().run()

