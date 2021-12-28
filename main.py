from App import App
from password_window.PasswordWindow import PasswordWindow
from tkinter import Tk, Toplevel
import signal

signal.signal(signal.SIGINT, lambda signalNumber, frame: exit())

app = App(Tk())

passwordWindow = PasswordWindow(app)

app.run()
