import pandas as pd
from typing import Text
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from matplotlib.pyplot import text
from pyrsistent import s
from kivy.uix.button import Button


class mygrid(GridLayout):

    def __init__(self, **kwargs):
        self.df1 = [["Stock Name", "Buy Price",
                     "Stop Loss", "percentage risk"]]
        super(mygrid, self).__init__()
        self.cols = 2
        self.risk = 0

        self.add_widget(Label(text="Stock Name:"))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="No. of shares bought:"))
        self.s_number = TextInput()
        self.add_widget(self.s_number)

        self.add_widget(Label(text="Stock bought at price(in INR):"))
        self.s_buyprice = TextInput()
        self.add_widget(self.s_buyprice)

        self.add_widget(Label(text="Stop Loss(in INR):"))
        self.s_stoploss = TextInput()
        self.add_widget(self.s_stoploss)

        self.storebutton = Button(text="Store in df")
        self.storebutton.bind(on_press=self.store)
        self.add_widget(self.storebutton)

        self.exportbutton = Button(text="Export in excel")
        self.exportbutton.bind(on_press=self.export)
        self.add_widget(self.exportbutton)

        self.calcbutton = Button(text="calculaterisk")
        self.calcbutton.bind(on_press=self.calculaterisk)
        self.add_widget(self.calcbutton)
        self.add_widget(Label(text="Stock Market risk calc app"))

    def store(self, instance):
        temp = [self.s_name.text, self.s_buyprice.text,
                self.s_stoploss.text, self.risk]
        self.df1.append(temp)

    def export(self, instance):
        df2 = pd.DataFrame(self.df1)
        df2.to_excel("output.xlsx", header=False)

    def calculaterisk(self, instance):
        self.risk = ((int(self.s_buyprice.text)-int(self.s_stoploss.text)) /
                     int(self.s_buyprice.text))*100
        self.add_widget(Label(text="(%) risk of " + self.s_name.text))
        self.add_widget(Label(text=self.displayrisk()))

    def displayrisk(self):
        return str(self.risk)


class myapp(App):

    def build(self):
        return mygrid()
