from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class Container(GridLayout):

    view_in = ObjectProperty()
    my_lbl = ObjectProperty()

    def show_info(self):
        print(self.view_in.text)
        self.view_in.text = ''
        self.mylbl.text = '138539'
        print(self.view_in)

class MyApp(App):
    kv_directory = 'data'

    def build(self):
        return Container()

def main():
    MyApp().run()

if __name__ == "__main__":
    main()