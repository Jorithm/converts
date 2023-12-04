import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile = entry_int.get()
    km = (mile) * 1.61
    out_string.set(km)

window = ttk.Window(themename="darkly")
window.title("Convert")
window.geometry("400x300")

title = ttk.Label(master=window, text= "Miles to kilometers", font="arial 24 bold")#, foreground="blue" )r
title.pack(pady=5)

frame = ttk.Frame(master=window)
label = ttk.Label(master=frame, text= "value")
entry_int = tk.IntVar()
entry = ttk.Entry(master=frame, textvariable=entry_int)
button = ttk.Button(master=frame, text="convert", command=convert)

label.pack(side="left", padx=5)
entry.pack(side="left", padx=5)
button.pack()
frame.pack(pady=15)

out_string = tk.StringVar()
out = ttk.Label(master=window,textvariable=out_string, font="arial 24 bold", foreground="crimson")
out.pack(pady=5)

window.mainloop()