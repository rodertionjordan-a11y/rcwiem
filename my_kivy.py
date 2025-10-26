from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.menu_screen import MenuScreen
from src.help_screen import HelpScreen
from src.screen_button import ScreenButton
from src.chooser_screen import ChooserScreen
from src.mem_screen import MemScreen

class MemoApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(MenuScreen(name="menu"))
        screen_manager.add_widget(HelpScreen(name="help"))
        screen_manager.add_widget(ChooserScreen(name="chooser"))
        screen_manager.add_widget(MemScreen(name="generator"))
        return screen_manager


app = MemoApp()
app.run()







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

from .screen_button import ScreenButton


class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        line = BoxLayout(orientation="vertical", padding=60, spacing=60)
        line.add_widget(Label(text="Сделай свой мем!"))
        line.add_widget(ScreenButton("chooser", self, "left", text="Дальше"))
        line.add_widget(ScreenButton("help", self, "up", text="Помощь"))

        self.add_widget(line)










import os
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from PIL import Image as PIL.Image, ImageDraw, ImageFont
import os

from .screen_button import ScreenButton


class MemScreen(Screen):
    image = Image()

    def __init__(self, **kw):
        super().__init__(**kw)
        line = BoxLayout(orientation="vertical", padding=60, spacing=10)
        h_line = BoxLayout(spacing=60, size_hint=(1, 0.15))
        h_line.add_widget(ScreenButton("chooser", self, "right", text="Назад"))
        h_line.add_widget(Button(text="Сгенерировать", on_press=self.gaymem))
        self.text_top = TextInput(hint_text="Введите текст", size_hint_y=None, height=35)
        self.text_bottom = TextInput(hint_text="Введите текст", size_hint_y=None, height=35)
        line.add_widget(h_line)
        line.add_widget(self.text_top)
        line.add_widget(self.image)
        line.add_widget(self.text_bottom)

        self.add_widget(line)
    def gaymem(self, _):
        if not MemScreen.image.source:
            return
        pil_image = PILImage.open(MemScreen.image.source)
        pil_image = pil_image.convert("RGB")

        draw = ImageDraw.Draw(pil_image)
        width, height = pil_image.size
        font = ImageFont.truetype("arial.ttf", size = height//10)


        top = self.text_top.text.strip()
        bottom = self.text_bottom.text.strip()

        if top:
            box = draw.textbbox((0,0), top, font=font)
            text_width = box[2]-box[0]
            x = (width - text_width)/2
            y=10
            draw.text((x,y), top, font=font, fill = 'black')
        if bottom:
            box1 = draw.textbbox((0,0), bottom, font=font)
            text_width = box1[2]-box1[0]
            text_height = box[3]-box[1]
            x = (width - text_width)/2
            y = height - text_height - 10
            draw.text((x,y), bottom, font=font, fill = 'black')
        path = os.path.join(os.getcmd(), "autodraw_21.10.2025_(2).png")
        pil_image.save(path)
        
        MemScreen.image.source = path
        MemScreen.image.reload()








from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from .screen_button import ScreenButton


class HelpScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        help_text = (
            "Добро пожаловать в Генератор мемов!\n\n"
            "1. Нажмите «Выбрать картинку», чтобы загрузить изображение.\n"
            "2. После выбора фото вы попадёте в редактор:\n"
            "   — введите текст сверху и снизу картинки;\n"
            "   — настройте шрифт и цвет (если доступно);\n"
            "   — сохраните готовый мем на устройство.\n\n"
            "Если что-то пошло не так — просто вернитесь в меню и начните заново.\n"
            "Приятного мемогенерирования!"
        )

        line = BoxLayout(orientation="vertical", padding=60, spacing=60)
        line.add_widget(Label(text=help_text))
        line.add_widget(
            ScreenButton(
                "menu",
                self,
                "down",
                text="Назад",
                size_hint=(0.5, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )

        self.add_widget(line)




import os

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

from .screen_button import ScreenButton
from .generator_screen import GeneratorScreen


class ChooserScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        line = BoxLayout(orientation="vertical", padding=60, spacing=60)
        h_line = BoxLayout(spacing=60, size_hint=(1, 0.2))

        h_line.add_widget(ScreenButton("menu", self, "right", text="Назад"))
        h_line.add_widget(
            Button(text="Выбрать\nкартинку", on_press=self.open_file_chooser)
        )
        h_line.add_widget(ScreenButton("generator", self, "left", text="Далее"))

        self.image = Image()
        line.add_widget(h_line)
        line.add_widget(self.image)

        self.add_widget(line)

    def open_file_chooser(self, button):
        def select_image(instance):
            if filechooser.selection:
                GeneratorScreen.image.source = filechooser.selection[0]
                GeneratorScreen.image.reload()
                self.image.source = filechooser.selection[0]
                self.image.reload()
            popup.dismiss()

        line = BoxLayout(orientation="vertical")
        filechooser = FileChooserListView(
            filters=["*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp"], path=os.getcwd()
        )
        line.add_widget(filechooser)
        popup = Popup(title="Выберите изображение", content=line, size_hint=(0.9, 0.9))

        select_btn = Button(text="Выбрать", on_press=select_image)
        cancel_btn = Button(text="Отмена", on_press=popup.dismiss)

        h_line = BoxLayout(size_hint_y=None, height=40)
        h_line.add_widget(select_btn)
        h_line.add_widget(cancel_btn)
        line.add_widget(h_line)
        popup.open()
