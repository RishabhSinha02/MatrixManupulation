from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame7")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("History")
window.geometry("1000x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    97.0,
    43.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    407.0,
    image=image_image_2
)

canvas.create_text(
    824.0,
    35.0,
    anchor="nw",
    text="Rishabh Sinha",
    fill="#4C4C4C",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    400.0,
    95.0,
    anchor="nw",
    text="History",
    fill="#4C4C4C",
    font=("Inter Bold", 55 * -1)
)

canvas.create_text(
    274.0,
    279.0,
    anchor="nw",
    text="Add",
    fill="#4C4C4C",
    font=("Inter Bold", 30 * -1)
)

canvas.create_text(
    255.0,
    463.0,
    anchor="nw",
    text="Multiply",
    fill="#4C4C4C",
    font=("Inter Bold", 30 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    789.0,
    43.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=24.0,
    y=99.0,
    width=131.0,
    height=47.0
)

canvas.create_rectangle(
    740.0,
    219.0,
    779.0,
    261.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    750.0,
    222.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    790.0,
    219.0,
    829.0,
    261.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    800.0,
    222.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    691.0,
    219.0,
    729.0,
    261.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    700.0,
    222.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    740.0,
    270.0,
    779.0,
    311.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    750.0,
    273.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    740.0,
    320.0,
    779.0,
    361.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    750.0,
    323.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    790.0,
    270.0,
    829.0,
    311.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    800.0,
    273.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    790.0,
    320.0,
    829.0,
    361.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    800.0,
    323.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    691.0,
    270.0,
    729.0,
    311.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    700.0,
    273.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    691.0,
    320.0,
    729.0,
    362.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    700.0,
    323.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    740.0,
    407.0,
    779.0,
    449.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    750.0,
    410.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    790.0,
    407.0,
    829.0,
    449.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    800.0,
    410.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    691.0,
    407.0,
    729.0,
    449.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    700.0,
    410.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    740.0,
    458.0,
    779.0,
    499.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    750.0,
    461.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    740.0,
    508.0,
    779.0,
    549.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    750.0,
    511.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    790.0,
    458.0,
    829.0,
    499.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    800.0,
    461.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    790.0,
    508.0,
    829.0,
    549.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    800.0,
    511.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    691.0,
    458.0,
    729.0,
    499.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    700.0,
    461.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_rectangle(
    691.0,
    508.0,
    729.0,
    550.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    700.0,
    511.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)
window.resizable(False, False)
window.mainloop()
