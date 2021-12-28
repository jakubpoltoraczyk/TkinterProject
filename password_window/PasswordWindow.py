from tkinter import Toplevel
from external.constants import DEFAULT_BACKGROUND_COLOR, DEFAULT_WINDOW_GEOMETRY_SIZE
from title_label.TitleLabel import TitleLabel
from custom_entry.CustomEntry import CustomEntry
from custom_button.CustomButton import CustomButton
from messagee_box.PasswordMessageBox import PasswordMessageBox
import json


class PasswordWindow(Toplevel):
    """Class, which represents password window. It inherits from Toplevel object"""

    def __init__(self, main_app):
        """Construct new PasswordWindow object

        Params:
            main_app (App): Main application object"""
        Toplevel.__init__(self, background=DEFAULT_BACKGROUND_COLOR)

        self.__main_app = main_app
        self.__main_app.get_root_window().withdraw()

        self.__title_label = TitleLabel(self)
        self.__title_label.move(x_coordinate=65, y_coordinate=45)
        self.__title_label.set_text("Login window")

        self.__username_entry = CustomEntry(self, x_coordinate=40, y_coordinate=150)
        self.__username_entry.set_text("Username: ")

        self.__password_entry = CustomEntry(self, x_coordinate=40, y_coordinate=200)
        self.__password_entry.set_text("Password: ")
        self.__password_entry.set_mode(CustomEntry.Mode.PASSWORD)

        self.__login_button = CustomButton(
            self,
            "Login",
            self.__login,
            DEFAULT_WINDOW_GEOMETRY_SIZE,
            DEFAULT_WINDOW_GEOMETRY_SIZE,
        )

        self.__exit_button = CustomButton(
            self,
            "Exit",
            lambda: exit(),
            DEFAULT_WINDOW_GEOMETRY_SIZE,
            DEFAULT_WINDOW_GEOMETRY_SIZE,
        )

        self.__password_message_box = PasswordMessageBox(
            "Oops!", "Wrong password! Try again!"
        )

        data_file = open(
            "data/login_data.json"
        )  # todo: this path doesn't work properly with desktop shortcut - fix it immediately
        self.__login_data = json.load(data_file)
        data_file.close()

        self.geometry(
            str(DEFAULT_WINDOW_GEOMETRY_SIZE) + "x" + str(DEFAULT_WINDOW_GEOMETRY_SIZE)
        )

    def __login(self):
        """Private method, used to check user login data"""
        correct_user_data = False
        for user_data in self.__login_data["login_data"]:
            if (
                user_data["login"] == self.__username_entry.get_text()
                and user_data["password"] == self.__password_entry.get_text()
            ):
                correct_user_data = True
        if correct_user_data:
            self.__main_app.get_root_window().deiconify()
            self.withdraw()
        else:
            self.__password_message_box.show()
