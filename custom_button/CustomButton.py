import tkinter as tk
from tkinter import *
from external.constants import FONT_FAMILY, FONT_SIZE

class CustomButton:
    """Class, whick represents custom button."""

    color = "#21A2F1"
    activebackground = "white"
    width = 70
    height = 40
    index = 0
    """Static arguments which represent button

    Params:
        color (str): background colour of button
        activebackground (str): colour of activebackground
        width (int): the value of width of button
        height (int): the value of height of button
        index (int): the index of the button"""

    def __init__(self, master, your_text, button_command):
        """Construct new CustomButton object

        Params:
            master (tkinter): base for your app
            your_text (str): text on the button
            button_list (tuple): board which comprises all buttons on the window
            button_command (function): command of button"""
        CustomButton.index += 1
        self.__index = CustomButton.index
        self.__frame = Frame(
            master, highlightthickness="3", highlightbackground="#FF453E", bd=0
        )
        self.__frame.place(
            x=self.calculate_x_coordinate(),
            y=500,
            width=CustomButton.width,
            height=CustomButton.height,
        )
        self.__button = Button(
            self.__frame, width=CustomButton.width, height=CustomButton.height
        )
        self.__button.config(
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
            Frame of button"""
        return self.__frame

    def get_button(self):
        """Provide button

        Returns:
            Button"""
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

    def set_all_buttons(button_list):
        """Set all buttons

        Args:
            button_list (tuple): List of buttons"""
        for x in button_list:
            x.__frame.place(
                x=x.coo_creatorx(),
                y=500,
                width=CustomButton.width,
                height=CustomButton.height,
            )

    def set_text(self, new_text):
        """Set new text on the button

        Params:
            new_text (str): Text, which will be set"""
        self.__button.config(text=new_text)
