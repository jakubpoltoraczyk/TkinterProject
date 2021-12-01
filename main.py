import tkinter as tk
from custom_button.CustomButton import CustomButton
from App import App

def changing_information(button_list):
    for button in button_list:
        button.get_button().config(
            background=CustomButton.color,
            activebackground=CustomButton.activebackground,
        )
        button.get_frame().place(
            x=button.calculate_x_coordinate(),
            width=CustomButton.width,
            height=CustomButton.height,
        )

master = tk.Tk()
button_list = []
button_list.append(
    CustomButton(
        master,
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        button_command=lambda: changing_information(button_list),
    )
)
button_list.append(CustomButton(master, "aaa", button_command=None))
button_list.append(CustomButton(master, "aaa", button_command=None))
button_list.append(CustomButton(master, "aaa", button_command=None))
button_list.append(CustomButton(master, "aaa", button_command=None))

app = App(master)
app.run()
