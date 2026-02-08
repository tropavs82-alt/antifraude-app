from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import webbrowser

class MeuApp(App):
    def build(self):
        webbrowser.open("http://127.0.0.1:8080")
        return Label(text="Abrindo sistema...")

MeuApp().run()
