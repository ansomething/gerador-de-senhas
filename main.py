# NOTE: Configurações gerais da tela
from kivy.config import Config

Config.set("graphics", "width", "400")
Config.set("graphics", "height", "500")
Config.set("graphics", "resizable", "0")
Config.set("kivy", "window_icon", "widgets/icon-chave.ico")

from kivy.core.window import Window
Window.clearcolor = (242 / 255, 242 / 255, 242 / 255, 1)

# NOTE: Módulo para gerar a senha
import password as pw

# NOTE: Módulos Kivy
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.clipboard import Clipboard


class MainLayout(Widget):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.hiddenbox = self.ids.secondbox
        self.hiddenbox.remove_widget(self.ids.btncopiar)
        self.hiddenbox.remove_widget(self.ids.pwoutput)

    # NOTE: Eventos de botão
    def gerar_on_press(self):
        self.ids.btngerarimg.source = "widgets/btn-gerar-light.png"

    def gerar_on_release(self):
        self.ids.btngerarimg.source = "widgets/btn-gerar-dark.png"

    def copiar_on_press(self):
        self.ids.btncopiarimg.source = "widgets/btn-copiar-light.png"

    def copiar_on_release(self):
        self.ids.btncopiarimg.source = "widgets/btn-copiar-dark.png"

    # NOTE: Função para gerar a senha
    def generated_password(self):
        genpassword = pw.password_generator()

        # NOTE: Inicialmente o botão de copiar e o frame estão escondidos
        self.hiddenbox.remove_widget(self.ids.btncopiar)
        self.hiddenbox.remove_widget(self.ids.pwoutput)

        # NOTE: Mostra a senha na tela
        self.outputpassword = self.ids.pwoutput
        self.outputpassword.text = genpassword

        # NOTE: Mostra o botão de copiar e o frame
        self.hiddenbox.add_widget(self.ids.btncopiar)
        self.hiddenbox.add_widget(self.ids.pwoutput)

    # NOTE: Função para copiar a senha
    def copy_password(self):
        self.copypw = Clipboard.copy(self.outputpassword.text)


class MainApp(App):
    def build(self):
        self.title = "Gerador de Senhas"
        return MainLayout()


# NOTE: Módulos para executar o programa sem problemas com arquivos temporários criados
import os, sys
from kivy.resources import resource_add_path, resource_find

if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run()
