import tkinter as tk
from tkinter import messagebox

class MessageBox:
    """Class, which represents message box object"""

    def __init__(self, text, title):
        """Construct new message box
        Params:
            text(str): text of message
            title(str): title of message"""

        self.__text = text
        self.__title = title

    def show(self):
        """Method which shows message box"""

        messagebox.showinfo(self.__text, self.__title)
