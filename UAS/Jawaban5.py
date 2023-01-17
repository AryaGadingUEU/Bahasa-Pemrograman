from tkinter import *

root = Tk()
root.title("Jawaban UAS Ke-5")
root.geometry("190x50")

app = Frame(root)
app.grid()

label = Label(app, text="Program sukses dijalankan!")
label.grid()

def end_program():
    root.destroy()

oke_button = Button(app, text="Oke!", command=end_program)
oke_button.grid()

root.mainloop()

