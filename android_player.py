from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer
from kivy.utils import platform
from kivy import Config

class MainApp(MDApp):
    title = "Simple Video"
    def build(self):
        if platform == 'android':
            # Путь к внутреннему хранилищу приложения на Android
            root_path = Config.get('kivy', 'videos')
            print(root_path)
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "BlueGray" 
            player = VideoPlayer(source = f"{root_path}/2023-02-19 02-41-20.mkv")
            player.state = 'play'
            player.options = {'eos':'loop'}
            player.allow_stretch = True
            return player
        
MainApp().run()
