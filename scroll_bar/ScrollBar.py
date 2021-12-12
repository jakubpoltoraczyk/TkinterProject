import tkinter as tk
from tkinter import Canvas
from external.constants import FONT_FAMILY, FONT_SIZE

class ScrollBar:
    """Class, whick represents custom button."""

    __width = 620
    """Static private property which hold the width of scroll bar"""

    height = 40
    """Static property which hold the height of scroll bar"""

    __middle_position = int(0.5 * height)
    """Static private property which count the middle coordinate of items on canvas"""

    big_oval_size = 7
    """Static property which hold the size of moving oval"""

    small_oval_size = 4
    """Static property which hold the size of points ovals"""

    small_ovals_color = "red"
    """Static property which hold the color of points ovals"""

    big_oval_color = "pink"
    """Static property which hold the color of moving oval"""

    points_oval_color = "red"
    """Static property which hold color of points ovals"""

    def __init__(self, master, my_text, y_coordinate):
        """Construct new ScrollBar object

        Params:
            master (tkinter): parent of your app
            text (str): name of programming language
            y_coordinate (int): y coordinate in pixels of scrollbar"""
        self.__canvas = Canvas(
            master, width=ScrollBar.__width, height=ScrollBar.height, bg="#D9D9D9"
        )
        self.__canvas.create_text(
            30,
            ScrollBar.__middle_position,
            text=my_text,
            fill="black",
            font=("Helvetica", 12),
        )
        self.__canvas.create_line(
            105,
            ScrollBar.__middle_position,
            530,
            ScrollBar.__middle_position,
            fill="black",
        )
        self.__oval = self.__canvas.create_oval(
            90,
            ScrollBar.__middle_position - ScrollBar.big_oval_size,
            105,
            ScrollBar.__middle_position + ScrollBar.big_oval_size,
            fill=ScrollBar.big_oval_color,
        )
        self.__oval_position_index = 0
        position = 48
        self.__canvas_list = []
        for index in range(10):
            position += 48
            if self.__oval_position_index == index:
                self.__canvas_list.append(
                    self.__canvas.create_oval(
                        position,
                        ScrollBar.__middle_position - ScrollBar.small_oval_size,
                        position + 8,
                        ScrollBar.__middle_position + ScrollBar.small_oval_size,
                        fill=ScrollBar.big_oval_color,
                        width=0,
                    )
                )
                continue
            self.__canvas_list.append(
                self.__canvas.create_oval(
                    position,
                    ScrollBar.__middle_position - ScrollBar.small_oval_size,
                    position + 8,
                    ScrollBar.__middle_position + ScrollBar.small_oval_size,
                    fill=ScrollBar.small_ovals_color,
                    width=0,
                )
            )
        self.__canvas.create_oval(
            ScrollBar.__width - ScrollBar.height - 4,
            5,
            ScrollBar.__width - 14,
            ScrollBar.height - 5,
            fill=ScrollBar.points_oval_color,
        )
        self.__points = self.__canvas.create_text(
            ScrollBar.__width - int(0.5 * ScrollBar.height) - 10,
            ScrollBar.__middle_position + 1,
            text=self.__oval_position_index + 1,
            fill="black",
            font=(FONT_FAMILY, FONT_SIZE),
        )

        master.bind("<ButtonPress-1>", lambda event: self.__capture(master, True))
        master.bind("<ButtonRelease-1>", lambda event: self.__capture(master, False))
        self.__canvas.place(x=50, y=y_coordinate)

    def __motion(self, event):
        """Method which move a moving oval

        Args:
            event (class): tkinter module"""
        coordinate = self.__canvas.coords(self.__oval)
        x_move = event.x - coordinate[0]
        y_move = event.y - coordinate[1]
        if (
            event.x in range(70, 540)
            and abs(x_move) in range(45, 90)
            and abs(y_move) in range(0, 15)
        ):
            if x_move > 0:
                self.__canvas.move(self.__oval, 48, 0)
                self.__oval_position_index += 1
                self.__canvas.itemconfig(
                    self.__canvas_list[self.__oval_position_index],
                    fill=ScrollBar.big_oval_color,
                )
                self.__canvas.itemconfig(
                    self.__canvas_list[self.__oval_position_index - 1],
                    fill=ScrollBar.small_ovals_color,
                )
                self.__canvas.itemconfig(
                    self.__points, text=self.__oval_position_index + 1
                )
            else:
                self.__canvas.move(self.__oval, -48, 0)
                self.__oval_position_index -= 1
                self.__canvas.itemconfig(
                    self.__canvas_list[self.__oval_position_index],
                    fill=ScrollBar.big_oval_color,
                )
                self.__canvas.itemconfig(
                    self.__canvas_list[self.__oval_position_index + 1],
                    fill=ScrollBar.small_ovals_color,
                )
                self.__canvas.itemconfig(
                    self.__points, text=self.__oval_position_index + 1
                )

    def __capture(self, master, flag):
        """Method which move a moving oval

        Args:
            master (tkinter): parent of your app
            flag (bool): a True/False value which is responsible for tracking moving oval"""
        if flag:
            master.bind("<Motion>", lambda event: self.__motion(event))
        else:
            master.unbind("<Motion>")
