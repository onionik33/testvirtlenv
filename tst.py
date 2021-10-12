from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyCalc(MDApp):
    def build(self):
        return MDLabel(text="Hello Calc", halign='center')

def main():
    MyCalc().run()


if __name__ == "__main__":
    main()