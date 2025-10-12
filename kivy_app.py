from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ScreenButton(Button):
    def __init__(self, screen_name, screen, direction, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name
        self.screen = screen
        self.direction = direction

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.screen_name

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line = BoxLayout(orientation='vertical')
        line.add_widget(Label(text='Перейти', halign='left'))
        line.add_widget(ScreenButton('choosers', self, 'left', text='Перейти'))
        self.add_widget(line)

class HelpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line = BoxLayout(orientation='vertical')
        line.add_widget(Label(text='Помощь нет! Ересь наступает!', halign='left'))
        line.add_widget(ScreenButton('start', self, 'down', text='Вернуться'))
        self.add_widget(line)

class ChooserScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        line = BoxLayout(orientation='vertical')
        line.add_widget(Label(text='Помощь нет! Ересь наступает!', halign='left'))
        line.add_widget(ScreenButton('start', self, 'left', text='Вернуться'))
        self.add_widget(line)

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(StartScreen(name='start'))
        screen_manager.add_widget(ChooserScreen(name='choosers'))
        screen_manager.add_widget(HelpScreen(name='help'))
        return screen_manager
