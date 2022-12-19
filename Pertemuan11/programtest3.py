# Heading
import tkinter as tk
from tkinter import ttk #Frame Input
from tkinter.messagebox import showinfo #Import Display Show Info

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("800x800")
window.resizable(False, False)
window.title("GUI GARDEN") #Judul

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Frame Input
input_frame = ttk.Frame(window)
#Penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen-komponen GUI
## Depan
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan: ")
nama_depan_label.pack(padx=10,fill="x",expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

## Belakang
# 1. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang: ")
nama_belakang_label.pack(padx=10,fill="x",expand=True)

# 2. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

## Tombol
def tombol_click():
    # print(NAMA_BELAKANG.get())
    # Fungsi di atas untuk memanggil nama belakang ke terminal
   
   #Fungsinya akan dipanggil oleh tombol di bawah!
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}!"
    showinfo(title="HASIL",message=pesan)

tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop()