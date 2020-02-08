import kivy
import json
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App

kivy.require("1.11.1")

Builder.load_file("MultipleChoice_text.kv")


class MultipleChoiceT(BoxLayout):

    # collects info from json file and assigns it to settings var
    with open('widget_settings.json', 'r') as file:
        settings = json.load(file)["MultipleChoice_settings"][0]

    print(settings)

    test = 'hello'

    def __init__(self, **kwargs):
        super(MultipleChoiceT, self).__init__(**kwargs)
        self.app = App.get_running_app()
        print(self.app)
        self.w_width = 0.5
        self.w_height = 1
        self.data = {'pressed_btn': 0, 'btn_text': None}

    # the function called for when the toggle button is on_state
    def pressed(self, instance):
        self.data['pressed_btn'] = self.get_id(instance)
        self.data['btn_text'] = instance.text
        print(self.data)

    # changes the bottom label when submit button is pressed
    def submit(self):
        self.bottom_label.text = f"ID: {self.data['pressed_btn']} TEXT: {self.data['btn_text']}"

    # returns the id of the given instance
    @staticmethod
    def get_id(instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    # null method for now, not implemented
    def change_question(self, new_text):
        self.question_label.text = str(new_text)

    # prints text when the next question button is pressed
    def next_question(self):
        print('next question pressed')

    # returns the dimensions for the toggle buttons based on their text length and font size defined in settings json
    def get_dimension(self, instance):
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
