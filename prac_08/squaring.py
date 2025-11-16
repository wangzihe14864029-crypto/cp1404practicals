"""
CP1404 Practical
Kivy GUI program to square a number
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number"""

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (400, 200)
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation and update the output label"""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid"


SquareNumberApp().run()
