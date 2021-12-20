from tkinter import Toplevel
from external.constants import DEFAULT_BACKGROUND_COLOR
from title_label.TitleLabel import TitleLabel
from custom_entry.CustomEntry import CustomEntry
from custom_button.CustomButton import CustomButton


class PasswordWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self, background=DEFAULT_BACKGROUND_COLOR)

        self.__title_label = TitleLabel(self)
        self.__username_entry = CustomEntry(self, x_coordinate=40, y_coordinate=150)
        self.__password_entry = CustomEntry(self, x_coordinate=40, y_coordinate=200)
        self.__login_button = CustomButton(self, "Login", lambda: print("Hello"))
        self.__exit_button = CustomButton(self, "Exit", lambda: exit())
        
        self.__title_label.move(x_coordinate=65, y_coordinate=45)
        self.__title_label.set_text("Login window")
        self.__username_entry.set_text("Username: ")
        self.__password_entry.set_text("Password: ")
        self.__password_entry.set_mode(CustomEntry.Mode.PASSWORD)

