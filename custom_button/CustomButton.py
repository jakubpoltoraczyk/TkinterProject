import tkinter as tk
from tkinter import Button, Frame
from external.constants import FONT_FAMILY, FONT_SIZE


class CustomButton:
    """Class, whick represents custom button."""

    color = "#21A2F1"
    """Static property which hold the color of button"""

    activebackground = "white"
    """Static property which hold the activebackgroud color of button"""

    width = 70
    """Static property which hold the width of button"""

    height = 40
    """Static property which hold the height of button"""

    index = 0
    """Static property which hold the index of button"""

    def __init__(self, master, your_text, button_command):
        """Construct new CustomButton object

        Params:
            master (tkinter): parent of your app
            your_text (str): text on the button
            button_command (function): command of button"""
        CustomButton.index += 1
        self.__index = CustomButton.index
        self.__frame = Frame(
            master, highlightthickness=3, highlightbackground="#FF453E", bd=0
        )
        self.__frame.place(
            x=self.calculate_x_coordinate(),
            y=500,
            width=CustomButton.width,
            height=CustomButton.height,
        )
        self.__button = Button(
            self.__frame,
            width=CustomButton.width,
            height=CustomButton.height,
            text=your_text,
            background=CustomButton.color,
            font=(FONT_FAMILY, FONT_SIZE),
            activebackground=CustomButton.activebackground,
            highlightthickness=0,
            command=button_command,
        )
        self.__button.pack()

    def get_frame(self):
        """Provide frame of button

        Returns:
            instance of frame of button"""
        return self.__frame

    def get_button(self):
        """Provide button

        Returns:
            instance of button"""
        return self.__button

    def calculate_x_coordinate(self, geometry=700):
        """Calculate the x coordinate of button

        Args:
            geometry (int): the value of x of window

        Returns:
            Position of the button"""
        width = CustomButton.width
        self.__xaxis = geometry / (CustomButton.index + 2)
        self.__xaxis += geometry / (CustomButton.index + 2) * self.__index
        self.__xaxis -= 0.5 * (geometry / (CustomButton.index + 2))
        self.__xaxis -= 0.5 * width
        return self.__xaxis

    def set_text(self, new_text):
        """Set new text on the button

        Params:
            new_text (str): Text, which will be set"""
        self.__button.config(text=new_text)
