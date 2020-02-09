import kivy
import json
from kivy.properties import DictProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App
from custom_widgets import utils

kivy.require("1.11.1")
Builder.load_file("C:/Users/Matthew/PycharmProjects/scratches/custom_widgets/MultipleChoice_text.kv")


class MultipleChoiceT(BoxLayout):

    chapter = StringProperty()
    page = StringProperty()
    settings = DictProperty()
    content = DictProperty()

    def __init__(self, **kwargs):
        super(MultipleChoiceT, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.data = {'pressed_btn': None, 'btn_text': None}

    # the function called for when the toggle button is on_state
    def pressed(self, instance):
        if instance.state == 'down':
            self.data['pressed_btn'] = self.get_id(instance)
            self.data['btn_text'] = instance.text

        else:
            self.data['pressed_btn'] = None
            self.data['btn_text'] = None

    def update_info(self):
        self.settings = utils.get_settings(utils.settings_path, "MultipleChoiceT")
        self.content = utils.get_sub_content(utils.content_path, self.chapter, self.name, "quiz")
        print(self.content)

    # changes the bottom label when submit button is pressed
    def submit(self):
        self.bottom_label.text = f"ID: {self.data['pressed_btn']} TEXT: {self.data['btn_text']}"

    # returns the id of the given instance
    @staticmethod
    def get_id(instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def get_dimension(self, instance):
        self.update_info()
        if len(instance.text) < 25:
            width = ((len(instance.text) / 2) * instance.font_size) * 1.1
        else:
            width = (len(instance.text) / 2) * instance.font_size

        height = instance.font_size * 1.35
        return width * self.settings["btn_scalar"], height * self.settings["btn_scalar"]


class Test(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Test()


if __name__ == "__main__":
    MainApp().run()
