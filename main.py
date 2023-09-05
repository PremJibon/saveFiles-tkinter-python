from tkinter import filedialog
from tkinter import *


def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[
        ("Text file",".txt"),
        ("HTML file",".html"),
        ("All files",".*"),
    ])
    fileText = str(text.get(1.0,END))
    file.write(fileText)
    file.close()
    

window = Tk()
window.title("Hero Khor")

button = Button(text='save',command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()