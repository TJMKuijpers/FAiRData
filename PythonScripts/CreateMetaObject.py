import tkinter as tk

root = tk.Tk()

canvas_gui=tk.Canvas(root,width=400,height=300)
canvas_gui.pack()

# Add the entry fields for standard documentation
entry_title=tk.Entry(root)
canvas_gui.create_window(200,140,window=entry_title)