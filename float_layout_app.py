import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


Builder.load_file('design_files/float_layout.kv')


class MyFloatLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyFloatLayout()


if __name__ == '__main__':
    app = MyApp()
    app.run()

