import tkinter as tk
from tkinter import Label
from tkinter.constants import RIDGE, TOP
from external.constants import FONT_FAMILY, FONT_SIZE

TEXT_LENGTH = 25
"""Maximum length of text used in TitleLabel object"""


class TitleLabel(object):
    """Class, which represents title label object"""

    background_color = "#FFFFFF"
    """Static property, which holds color of label background"""

    foreground_color = "#000000"
    """Static property, which holds color of label foreground (text)"""

    def __init__(self, parent_window):
        """Construct new TitleLabel object

        Params:
            parent_window (Tk): Window, which will be parent for this label"""
        self.__label = Label(
            parent_window,
            width=TEXT_LENGTH,
            padx=20,
            pady=10,
            border=5,
            relief=RIDGE,
            font=(FONT_FAMILY, FONT_SIZE),
            background=TitleLabel.background_color,
            foreground=TitleLabel.foreground_color,
        )
        self.__label.pack(side=TOP, pady=10)

    def move(self, x_coordinate, y_coordinate):
        """Move whole object into new place, specified with coordinates x and y
        Params:
            x_coordinate (int): New x coordinate as a pixel value
            y_coordinate (int): New y coordinate as a pixel value"""
        self.__label.place(x=x_coordinate, y=y_coordinate)

    def set_text(self, new_text):
        """Set new text on the label

        Params:
            new_text (str): Text, which will be set"""
        if len(new_text) < TEXT_LENGTH:
            self.__label.config(text=new_text)
        else:
            print(
                "Can't set: '",
                new_text,
                "'. Length must be less than ",
                TEXT_LENGTH,
                " characters",
            )
