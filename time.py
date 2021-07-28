from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("GUI Test Time")

def waktu():
    date_time = strftime("%m/%d/%Y, %H:%M:%S") #cek waktu
    label.config(text=date_time)
    label.after(1000, waktu) #setiap 1000ms memanggil fungsi waktu
    
label = Label(root, background="black", foreground="white")
label.pack(anchor='center')
waktu()

mainloop()
