import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.window import Window  # Second method how to change bg color, first in the kv file


Builder.load_file('design_files/background_color.kv')


class BackgroundColorChange(Widget):
    def clear_text(self):
        self.ids.name.text = ''
        self.ids.surname.text = ''
        self.ids.age.text = ''


class MyApp(App):
    def build(self):
        Window.clearcolor = (10/255, 250/255, 189/255, 1)  # Second method how to change bg color, first in the kv file
        return BackgroundColorChange()


if __name__ == '__main__':
    app = MyApp()
    app.run()
