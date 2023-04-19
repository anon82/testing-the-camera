from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
 
from kivymd.uix.snackbar import Snackbar
from kivy.utils import get_color_from_hex
from pyzbar.pyzbar import ZBarSymbol
 
class Panel(MDFloatLayout,FakeRectangularElevationBehavior):
    pass

class TTApp(MDApp):
    
    def build(self):
        global SC 
        SC = ScreenManager()
        SC.add_widget(Builder.load_file("main.kv"))
        return SC
        
TTApp().run() 
