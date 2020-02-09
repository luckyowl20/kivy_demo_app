from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from custom_widgets.ContentDisplay import ContentDisplay
from custom_widgets.MultipleChoice_text import MultipleChoiceT
from custom_widgets.MultipleChoice_image import MultipleChoiceI
from custom_widgets.ImageButton import ImageButton
ContentDisplay.chapter = "chapter1"
ContentDisplay.page = "page1"

class Window1(Screen):
    pass


class Window2(Screen):
    pass


class Window3(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MainApp().run()
