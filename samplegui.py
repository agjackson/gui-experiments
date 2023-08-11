#!/usr/bin/env python

import tkinter as tk
from tkinter import * 
from tkinter import (ttk, filedialog as fd)

class SampleGUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        #self.pack(padx=5, pady=10)

        mainframe = ttk.Frame(self, padding="5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        headerFrame = ttk.Frame(mainframe, padding="5")
        headerFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        headerFrame.columnconfigure(0, weight=1)
        headerFrame.columnconfigure(1, weight=1)
        headerFrame.columnconfigure(2, weight=1)
        headerFrame.columnconfigure(3, weight=1)

        headerFrame.b1text = 'Button 1'
        headerFrame.b2text = 'Button 2'
        headerFrame.b3text = 'Button 3'
        headerFrame.b4text = 'Button 4'

        # add button style

        button1 = ttk.Button(headerFrame,text=headerFrame.b1text,width=12,padding=5)
        button2 = ttk.Button(headerFrame,text=headerFrame.b2text,width=12,padding=5)
        button3 = ttk.Button(headerFrame,text=headerFrame.b3text,width=12,padding=5)
        button4 = ttk.Button(headerFrame,text=headerFrame.b4text,width=12,padding=5)

        button1.grid(row=0, column=0, sticky=tk.W+tk.E)
        button2.grid(row=0, column=1, sticky=tk.W+tk.E)
        button3.grid(row=0, column=3, sticky=tk.W+tk.E)
        button4.grid(row=0, column=4, sticky=tk.W+tk.E)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("580x500")
    root.title("Sample GUI")

    sample = SampleGUI(master=root)
    sample.pack(fill="both", expand=True)

    root.mainloop()