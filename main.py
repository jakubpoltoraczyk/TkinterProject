import tkinter as tk
from custom_button.CustomButton import CustomButton
from App import App
from title_label.TitleLabel import TitleLabel

def move_button(button_list):
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

def move_label(label_list):
    for label in label_list:
        label.get_label().config(
            background=TitleLabel.background_color,
            foreground=TitleLabel.foreground_color,
        )

master = tk.Tk()
button_list = []
label_list = []
button_list.append(
    CustomButton(
        master,
        "00",
        button_command=lambda: move_button(button_list),
    )
)
label_list.append(TitleLabel(master))
label_list.append(TitleLabel(master))
button_list.append(CustomButton(master, "01", button_command=None))
button_list.append(
    CustomButton(master, "06", button_command=lambda: move_label(label_list))
)
button_list.append(
    CustomButton(
        master,
        "02",
        button_command=lambda: setattr(TitleLabel, "background_color", "red"),
    )
)
button_list.append(
    CustomButton(
        master, "03", button_command=lambda: setattr(CustomButton, "color", "red")
    )
)
button_list.append(
    CustomButton(
        master, "04", button_command=lambda: label_list[1].set_text("czekoladowe")
    )
)
button_list.append(
    CustomButton(master, "05", button_command=lambda: label_list[0].set_text("mleko"))
)
label_list[0].move(50, 20)
label_list[1].move(400, 20)

app = App(master)
app.run()
