from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image  import Image
from src.screen_button import ScreenButton


class HChooserScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        line = BoxLayout(orientation="vertical", padding=60, spacing=60, size_hint = (1, 0.2))
        h_line = BoxLayout()

        h_line.add_widget(Label(text="Удачи, брат!"))
        h_line.add_widget(ScreenButton("menu", self, "left", text="Choose\ncartoon"))
        h_line.add_widget(ScreenButton("menu", self, "right", text="After"))

        self.image = Image()

        line.add_widget(h_line)
        line.add_widget(self.image)
        self.add_widget(line)




from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from .screen_button import ScreenButton


class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        line = BoxLayout(orientation="vertical", padding=60, spacing=60)
        line.add_widget(Label(text="Сделай свой мем!"))
        line.add_widget(ScreenButton("chooser", self, "right", text="Дальше"))
        line.add_widget(ScreenButton("help",    self, "up",    text="Помощь"))

        self.add_widget(line)




from kivy.uix.button import Button


class ScreenButton(Button):
    def __init__(self, screen_name, screen, direction, **kw):
        super().__init__(**kw)
        self.screen_name = screen_name
        self.screen = screen
        self.direction = direction

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.screen_name




from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image  import Image
from src.screen_button import ScreenButton


class HChooserScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        line = BoxLayout(orientation="vertical", padding=60, spacing=60, size_hint = (1, 0.2))
        h_line = BoxLayout()

        h_line.add_widget(Label(text="Удачи, брат!"))
        h_line.add_widget(ScreenButton("menu", self, "left", text="Choose\ncartoon"))
        h_line.add_widget(ScreenButton("menu", self, "right", text="After"))

        self.image = Image()

        line.add_widget(h_line)
        line.add_widget(self.image)
        self.add_widget(line)



from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.menu_screen import MenuScreen
from src.help_screen import HelpScreen
from src.screen_button import ScreenButton
from src.chooser_screen import ChosserScreen

class MemoApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(MenuScreen(name="menu"))
        screen_manager.add_widget(HelpScreen(name="help"))
        screen_manager.add_widget(MenuScreen(name="menu"))
        return screen_manager


app = MemoApp()
app.run()




from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image  import Image
from kivy.uix.button import Button
from src.screen_button import ScreenButton


class MemScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        line = BoxLayout(orientation="vertical", padding=60, spacing=60, size_hint = (1, 0.2))
        
        line.add_widget(ScreenButton("chooser", self, "down", text=""))
        line.add_widget(Button(text='Cutythbhjdfnm'))
        line.add_widget(Image())
        self.add_widget(line)
