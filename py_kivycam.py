from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SelfieCameraApp(App):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.camera_obj = Camera()

    def build(self):
        self.camera_obj.resolution = (800, 800)
        # button
        button_obj = Button(text="Click Here")
        button_obj.size_hint = (.5, .2)
        button_obj.pos_hint = {'x': .25, "y": .25}
        button_obj.blind(on_press=self.take_selfie)

        # layout
        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        return layout

    def take_selfie(self, *args):
        print("I am taking selfie")
        self.camera_obj.export_to_png("./selfie.png")
