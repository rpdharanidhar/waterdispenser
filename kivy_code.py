import kivy
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import Create_folder as cf
#import Camera as c
kivy.require('1.10.1')

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    namee = ObjectProperty()
    def press(self):
        if self.namee.text != "":
            #name  = self.namee
            cf.New_Folder(self.namee.text)
            self.namee.text = ""



class ThirdWindow(Screen):
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


if __name__ == "__main__":
    MyApp().run()
