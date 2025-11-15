"""
CP1404 Practical
Dynamically create buttons based on content of dictionary
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve"]


class DynamicLabelsApp(App):
    """Main program - create labels dynamically."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = NAMES

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels for each name and add to GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()