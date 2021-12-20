import signal
from App import App
from PasswordWindow import PasswordWindow
from custom_button.CustomButton import CustomButton
from tkinter import *
from custom_entry.CustomEntry import CustomEntry
from title_label.TitleLabel import TitleLabel

signal.signal(signal.SIGINT, lambda signalNumber, frame: exit())

master = Tk()
app = App(master)

passwordWindow = Toplevel(master)
passwordWindow.geometry("400x400")

custom_entry = CustomEntry(passwordWindow, x_coordinate=10, y_coordinate=20)
title_label = TitleLabel(passwordWindow)
custom_button = CustomButton(passwordWindow, "Text", lambda: exit())

app.run()
