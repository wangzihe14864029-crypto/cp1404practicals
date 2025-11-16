"""
CP1404 Practical
GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file('convert_miles_km.kv')

    def handle_convert(self):
        miles = self.get_validated_miles()
        result = miles * MILES_TO_KM
        self.output_km = str(result)

    def handle_increment(self, change):
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_validated_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()