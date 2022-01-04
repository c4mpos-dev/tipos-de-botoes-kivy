from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDFloatingActionButton, MDRectangleFlatButton, MDRaisedButton, MDRectangleFlatIconButton

class TesteApp(MDApp):
    Window.size = (300, 600)

    def build(self):
        boxLayout = MDBoxLayout(
            orientation="vertical",
            spacing=15,
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        )

        btn1 = MDFlatButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        btn2 = MDIconButton(
            icon="folder",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        btn3 = MDFloatingActionButton(
            icon="plus",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        btn4 = MDRectangleFlatButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        btn5 = MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        btn6 = MDRectangleFlatIconButton(
            text="Página Inicial",
            icon="home",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        boxLayout.add_widget(btn1)
        boxLayout.add_widget(btn2)
        boxLayout.add_widget(btn3)
        boxLayout.add_widget(btn4)
        boxLayout.add_widget(btn5)
        boxLayout.add_widget(btn6)

        return boxLayout

TesteApp().run()