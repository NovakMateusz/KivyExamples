import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('design_files/update_label.kv')


class MyUpdateLabel(Widget):
    def update_name_label(self):
        self.ids.name.text = f"Hello there! Mr. {self.ids.user_input.text}!"


class MyApp(App):
    def build(self):
        return MyUpdateLabel()


if __name__ == '__main__':
    app = MyApp()
    app.run()
