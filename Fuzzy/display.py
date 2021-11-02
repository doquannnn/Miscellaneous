import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tipping import FIS
import matplotlib.pyplot as plt

window = Tk()
window.title("How much will you tip?")
window.geometry("400x700")

lbl1 = tkinter.Label(window, text="QUALITY", fg="red", font=("Arial", 30))
lbl1.pack(fill=BOTH, expand=True)
# lbl1.grid(column=0, row=0)
txt1 = Entry(window, width=20, justify="center")
txt1.pack(fill=BOTH, expand=True)
# txt1.grid(column=0, row=1)

lbl2 = tkinter.Label(window, text="SERVICE", fg="red", font=("Arial", 30))
lbl2.pack(fill=BOTH, expand=True)
# lbl2.grid(column=0, row=2)
txt2 = Entry(window, width=20, justify="center")
txt2.pack(fill=BOTH, expand=True)
# txt2.grid(column=0, row=3)

lbl3 = tkinter.Label(window, text="TIME", fg="red", font=("Arial", 30))
lbl3.pack(fill=BOTH, expand=True)
# lbl3.grid(column=0, row=4)
txt3 = Entry(window, width=20, justify="center")
txt3.pack(fill=BOTH, expand=True)
# txt3.grid(column=0, row=5)

lbl4 = tkinter.Label(window, text="SIZE", fg="red", font=("Arial", 30))
lbl4.pack(fill=BOTH, expand=True)
# lbl4.grid(column=0, row=6)
txt4 = Entry(window, width=20, justify="center")
txt4.pack(fill=BOTH, expand=True)
# txt4.grid(column=0, row=7)

lbl5 = tkinter.Label(window, text="DAY", fg="red", font=("Arial", 30))
lbl5.pack(fill=BOTH, expand=True)
# lbl5.grid(column=0, row=8)
txt5 = Entry(window, width=20, justify="center")
txt5.pack(fill=BOTH, expand=True)
# txt5.grid(column=0, row=9)

frame = tkinter.Frame(window)
frame.pack()

img = Image.open("images/blank.png")
img = img.resize((400, 300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

panel = Label(window)
panel.config(image=img)
panel.image = img

panel.pack()

def handdleButton():
    qual = int(txt1.get())
    ser = int(txt2.get())
    ti = int(txt3.get())
    s = int(txt4.get())
    d = int(txt5.get())
    tipping, tip = FIS(qual, ser, ti, s, d)
    tip.view(sim=tipping)
    plt.savefig('images/tipping.png')
    plt.close()
    img = Image.open("images/tipping.png")
    img = img.resize((400, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img


    text = f"Recommended tip: {tipping.output['tip']}"
    messagebox.showinfo(message=text)



btn = Button(window, text="CRUNCH!!!", font=("Arial", 20), command=handdleButton)
btn.pack(fill=BOTH, expand=True)




window.mainloop()



