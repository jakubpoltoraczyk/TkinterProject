import tkinter as tk
from tkinter import *


class CustomButton:
    """Class, whick represents custom button.
    This is derived class, which inherits from tkinter Button Class"""

    color = "#21A2F1"
    font = ("Helvetica", "12")
    activebackground = "white"
    width = 70
    height = 40
    index = 0
    """Static arguments which represent button

    Params:
        color (str): background colour of button
        font (tuple): text font in button
        activebackground (str): colour of activebackground
        width (int): the value of width of button
        height (int): the value of height of button
        index (int): the index of the button"""

    def __init__(self, master, your_text, button_list, button_command):
        """Construct new Custom_Button object

        Params:
            master (tkinter): base for your app
            your_text (str): text on the button
            button_list (tuple): board which comprises all buttons on the window
            button_command (function): command of button"""
        Custom_Button.index += 1
        self.__index = Custom_Button.index
        self.__frame = Frame(master,
            highlightthickness="3", highlightbackground="#FF453E", bd=0
        )
        self.__frame.place(
            x=self.coo_creatorx(),
            y=500,
            width=Custom_Button.width,
            height=Custom_Button.height,
        )
        self.__button = Button(
            self.__frame,width=Custom_Button.width, height=Custom_Button.height
        )
        self.__button.config(
            text=your_text,
            background=Custom_Button.color,
            font=Custom_Button.font,
            activebackground=Custom_Button.activebackground,
            highlightthickness=0,
            command=button_command,
        )
        self.__button.pack()
        Custom_Button.set_all_buttons(button_list)

    def frame_getter(self):
        """Provide frame of button

        Returns:
            Frame of button"""
        return self.__frame

    def __get_button(self):
        """Provide button

        Returns:
            Button"""
        return self.__button

    def coo_creatorx(self, geometry=700):
        """Calculate the x coordinate of button

        Args:
            geometry (int): the value of x of window

        Returns:
            Position of the button"""
        width = Custom_Button.width
        self.__xaxis = geometry / (Custom_Button.index + 2)
        self.__xaxis += geometry / (Custom_Button.index + 2) * self.__index
        self.__xaxis -= 0.5 * (geometry / (Custom_Button.index + 2))
        self.__xaxis -= 0.5 * width
        return self.__xaxis

    def change_color(color, button_list):
        """Set new colour of buttons

        Args:
            color (str): New colour of buttons
            button_list (tuple): board with all the buttons"""
        Custom_Button.color = color
        for x in button_list:
            x.__get_button().config(background=Custom_Button.color)

    def change_font(font, button_list):
        """Set new fontof buttons

        Args:
            color (str): New font of buttons
            button_list (tuple): board with all the buttons"""
        Custom_Button.font = font
        for x in button_list:
            x.__get_button().config(font=Custom_Button.font)

    def change_activebackground(activebackground, button_list):
        """Set new activebackground of buttons

        Args:
            color (str): New activebackground of buttons
            button_list (tuple): board with all the buttons"""
        Custom_Button.activebackground = activebackground
        for x in button_list:
            x.__get_button().config(activebackground=Custom_Button.activebackground)

    def change_width(width, button_list):
        """Set new widht of buttons

        Args:
            color (str): New width of buttons
            button_list (tuple): board with all the buttons"""
        Custom_Button.width = width
        Custom_Button.set_all_buttons(button_list)

    def change_height(height, button_list):
        """Set new height of buttons

        Args:
            color (str): New height of buttons
            button_list (tuple): board with all the buttons"""
        Custom_Button.height = height
        Custom_Button.set_all_buttons(button_list)

    def set_all_buttons(button_list):
        """Set all buttons

        Args:
            button_list (tuple): List of buttons"""
        for x in button_list:
            x.__frame.place(
                x=x.coo_creatorx(),
                y=500,
                width=Custom_Button.width,
                height=Custom_Button.height,
            )
