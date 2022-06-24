from breezypythongui import EasyFrame
from tkinter import *

root = Tk()
root.geometry("230x130")

class Button(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.label = self.addLabel(text="God is Great!",
                                   row=0, column=0,
                                   columnspan=2, sticky="NSEW")

        self.prevBtn = self.addButton(text="Previous",
                                       row=1, column=0,
                                       state="disabled",
                                       command=self.prev)
        self.nextBtn = self.addButton(text="Next",
                                         row=1, column=1,
                                         command=self.next)

    def prev(self):
        self.label["text"] = "God is Good"
        self.prevBtn["state"] = "disabled"
        self.nextBtn["state"] = "normal"

    def next(self):
        self.label["text"] = "All the Time!"
        self.prevBtn["state"] = "normal"
        self.nextBtn["state"] = "disabled"

b = Button()
root.mainloop()