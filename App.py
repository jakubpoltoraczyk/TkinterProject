import tkinter as tk
from external.constants import DEFAULT_BACKGROUND_COLOR

class App:
    """Class which represents main application window"""
    def __init__(self, root):
        """Construct new App object
        
        Params:
            root (tkinter): root application window"""
        self.__root = root
        self.__root.title("Project")
        self.__root.geometry("800x800")
        self.__root.config(
            background="#A49D8A", highlightthickness="10", highlightcolor="grey"
        )

    def run(self):
        """Method which display the window."""
        self.__root.mainloop()

    def get_root_window(self):
        """Provide root application window"""
        return self.__root
