import kivy
import face_detection_attendace as fc
import cv2
kivy.require('1.9.0')
import If_Unkown_face as iu
# import dlib
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
import Camera as c
import time



class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class CameraClick(Screen):
    def capture(self):
        if self.ids.textx.text != "":
            '''
            Function to capture the images and give them the names
            according to their captured time and date.
            '''
            name = root.auth(SecondWindow.ids.namee.text)
            camera = self.ids['camera']
            camera.export_to_png("{}.png".format(self.ids.textx.text))
            print("Captured")

    ''' namee = ObjectProperty(None)
        def press(self):
            if self.ids.namee.text != "":
                # name  = self.namee
                # cf.New_Folder(self.namee.text)
                a = self.ids.namee.text
                self.camera(a)

                #c.camera(self.ids.namee.text)
                self.ids.namee.text = "" '''




class ThirdWindow(Screen):
    def press(self):
        iu.iuf()

    pass


class WindowManager(ScreenManager):
    pass


# Builder.load_file('water.kv')
kv1 = Builder.load_file('box.kv')


class MyBoxLayout(Widget):

    def press(self):
        name = self.name.text
        print(f'HI, I am  {name}')

    def clear(self):
        self.name.text = " "


class MyApp(App):
    def build(self):
        return kv1


a = iu.iuf()
if a == "Unknown":
    if __name__ == "__main__":
        MyApp().run()
