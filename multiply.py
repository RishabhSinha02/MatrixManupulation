from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("Multiply")
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
    364.0,
    123.0,
    anchor="nw",
    text="MULTIPLY",
    fill="#4C4C4C",
    font=("Inter Bold", 55 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    789.0,
    43.0,
    image=image_image_3
)

canvas.create_text(
    257.0,
    221.0,
    anchor="nw",
    text="Multiplication of Matrix A and Matrix B",
    fill="#838383",
    font=("Inter Bold", 25 * -1)
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
    x=612.0,
    y=20.0,
    width=131.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=24.0,
    y=99.0,
    width=131.0,
    height=47.0
)

canvas.create_rectangle(
    460.0,
    310.0,
    540.0,
    390.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    479.0,
    315.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    564.0,
    310.0,
    644.0,
    390.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    583.0,
    315.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    356.0,
    310.0,
    436.0,
    390.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    375.0,
    315.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    460.0,
    407.0,
    540.0,
    487.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    479.0,
    412.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    460.0,
    503.0,
    540.0,
    583.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    479.0,
    508.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    564.0,
    407.0,
    644.0,
    487.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    583.0,
    412.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    564.0,
    503.0,
    644.0,
    583.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    583.0,
    508.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    356.0,
    407.0,
    436.0,
    487.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    375.0,
    412.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)

canvas.create_rectangle(
    356.0,
    504.0,
    436.0,
    584.0,
    fill="#6C63FF",
    outline="")

canvas.create_text(
    375.0,
    509.0,
    anchor="nw",
    text="5",
    fill="#FFFFFF",
    font=("Inter Bold", 63 * -1)
)
window.resizable(False, False)
window.mainloop()
