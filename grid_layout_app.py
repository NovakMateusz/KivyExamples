import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


Builder.load_file('design_files/grid_layout.kv')


class MyGridLayout(Widget):
    def clear_text(self):
        self.ids.name.text = ''
        self.ids.surname.text = ''
        self.ids.age.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    app = MyApp()
    app.run()
