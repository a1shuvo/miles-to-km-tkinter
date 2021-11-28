from tkinter import *

FONT = ("Arial", 15, "bold")


def convert_mile_to_km():
    mile = float(mile_entry.get())
    km = mile * 1.609
    converted_km.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# mile Entry
mile_entry = Entry()
mile_entry.grid(column=1, row=0)

# mile Label
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

# is_equal_to Label
is_equal_to = Label(text="Is Equal To")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)

# converted_km Label
converted_km = Label(text="0", font=FONT)
converted_km.grid(column=1, row=1)

# km Label
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Calculate Button
calculate_button = Button(text="Calculate", command=convert_mile_to_km, font=FONT)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

window.mainloop()
