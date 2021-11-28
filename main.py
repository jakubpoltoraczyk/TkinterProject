import tkinter as tk
from tkinter import *
from task03 import Custom_Button

class App:
    def __init__(self, master):
        self.__master = master
        self.__master.title("Project")
        self.__master.geometry("700x700")
        self.__master.config(
            background="#A49D8A", highlightthickness="10", highlightcolor="grey"
        )
    def run(self):
        self.__master.mainloop()
master = tk.Tk()
app = App(master)
app.run()
