import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700)
Builder.load_file('design_files/calculator.kv')


class AppLayout(Widget):
    def clear(self):
        self.ids.input_value.text = '0'

    def clear_last_digit(self):
        text = self.ids.input_value.text
        if len(text) == 0 or 'Error' in text:
            self.ids.input_value.text = '0'
        else:
            self.ids.input_value.text = text[:-1]

    def add_digit(self, digit: str):
        if self.ids.input_value.text == '0':
            self.ids.input_value.text = digit
        else:
            self.ids.input_value.text += digit

    def add_symbol(self, symbol):
        self.ids.input_value.text += symbol

    def calculate(self):
        try:
            result = str(eval(self.ids.input_value.text))
        except SyntaxError:
            self.ids.input_value.text = "Syntax Error"
        except ZeroDivisionError:
            self.ids.input_value.text = "Zero Division Error"
        else:
            self.ids.input_value.text = result if result != '0.0' else '0'

    def swap_symbol(self):
        self.calculate()
        self.ids.input_value.text = str(eval(self.ids.input_value.text) * -1)

    def percent(self):
        self.calculate()
        result = str(eval(self.ids.input_value.text) / 100)
        self.ids.input_value.text = result if result != '0.0' else '0'


class CalculatorApp(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
