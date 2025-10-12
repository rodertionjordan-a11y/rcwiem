line = BoxLayout(orientation="vertical", padding=60, spacing=60, size_hint = (1, 0.2))
        h_line = BoxLayout()

        h_line.add_widget(Label(text="Удачи, брат!"))
        h_line.add_widget(ScreenButton("menu", self, "left", text="Choose\ncartoon"))
        h_line.add_widget(ScreenButton("menu", self, "right", text="After"))
