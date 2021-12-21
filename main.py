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
            x=button.calculate_x_coordinate(700),
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
        lambda: move_button(button_list), 700, 700
    )
)
label_list.append(TitleLabel(master))
label_list.append(TitleLabel(master))
button_list.append(CustomButton(master, "01", None, 700, 700))
button_list.append(
    CustomButton(master, "06", lambda: move_label(label_list), 700, 700)
)
button_list.append(
    CustomButton(
        master,
        "02",
        lambda: setattr(TitleLabel, "background_color", "red"), 700, 700
    )
)
button_list.append(
    CustomButton(
        master, "03", lambda: setattr(CustomButton, "color", "red"), 700, 700
    )
)
button_list.append(
    CustomButton(
        master, "04", lambda: label_list[1].set_text("czekoladowe"), 700, 700
    )
)
button_list.append(
    CustomButton(master, "05", lambda: label_list[0].set_text("mleko"), 700, 700)
)
label_list[0].move(50, 20)
label_list[1].move(400, 20)

app = App(master)
app.run()
