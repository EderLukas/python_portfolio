from tkinter import *

FONT = ("Courier", 14, "normal")


def calculate():
    """Converts Miles to Kilometers and sets label text to calculated value"""
    miles = float(input_field.get())
    lbl_km.config(text=str(miles*1.609))


# Create window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)

# Create gui components
input_field = Entry(width=7, font=FONT)
input_field.grid(column=1, row=0, padx=(25, 10), pady=(25, 10))

lbl_miles = Label(text="Miles", font=FONT)
lbl_miles.grid(column=2, row=0, pady=(25, 10))

lbl_is_equal_to = Label(text="is equal to", font=FONT)
lbl_is_equal_to.grid(column=0, row=1)

lbl_km = Label(text="0", font=FONT)
lbl_km.grid(column=1, row=1)

lbl_kilometer = Label(text="Km", font=FONT)
lbl_kilometer.grid(column=2, row=1)

btn_calculate = Button(text="Calculate", font=FONT, command=calculate)
btn_calculate.grid(column=1, row=2)

window.mainloop()
