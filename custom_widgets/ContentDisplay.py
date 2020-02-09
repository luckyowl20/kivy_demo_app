import kivy
import json
from kivy.properties import DictProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from custom_widgets import utils

Builder.load_file("C:/Users/Matthew/PycharmProjects/scratches/custom_widgets/ContentDisplay.kv")


class ContentDisplay(BoxLayout):

    chapter = StringProperty()  # current chapter to display
    page = StringProperty()  # current page in chapter
    settings = DictProperty()  # settings for widget
    content = DictProperty()  # content to display, collected based on the chapter and page

    def __init__(self, **kwargs):
        super(ContentDisplay, self).__init__(**kwargs)
        # self.app = App.get_running_app()

    # used to update the content and settings info if we need to see if it changed, or just to initialize it outside of
    # __init__
    def update_info(self):
        self.settings = utils.get_settings(utils.settings_path, "ContentDisplay")
        self.content = utils.get_content(utils.content_path, self.chapter, self.page)
        self.content["content"] = utils.content_to_text(self.content)

    # used to get the required dimensions of the NotePopup Button based on font size
    # def get_dimension(self, text, font_size):
    #     self.update_info()
    #     if len(text) < 25:
    #         width = ((len(text) / 2) * font_size) * 1.1
    #     else:
    #         width = (len(text) / 2) * font_size
    #
    #     height = font_size * 1.35
    #     return width * self.settings["btn_scalar"], height * self.settings["btn_scalar"]

    @staticmethod
    def get_settings():
        return utils.get_settings(utils.settings_path, "ContentDisplay")

    @staticmethod
    def get_content(chapter, page):
        return utils.get_c_content(utils.content_path, chapter, page)


class Test(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Test()


if __name__ == "__main__":
    MainApp().run()
