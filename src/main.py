import tkinter
import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


app = customtkinter.CTk()
app.geometry('800x800')

def button_function():
    print('button pressed')

button = customtkinter.CTkButton(
        master=app,
        text="BUTTON",
        command=button_function
        )

button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
