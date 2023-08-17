#!/usr/bin/env python

import tkinter as tk
from tkinter import * 
from tkinter import (ttk, filedialog as fd)

class SampleGUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        #self.pack(padx=5, pady=5)

        #---------------- STYLING
        s = ttk.Style()
        s.configure('mainframe.TFrame', background = '#102C57')

        #---------------- WIDGETS

        mainframe = ttk.Frame(self, padding="5", style='mainframe.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        """self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        headerFrame = ttk.Frame(mainframe, height = 20, relief="ridge", padding="5")
        #headerFrame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        #headerFrame.columnconfigure((0, 1, 2, 3), uniform="buttons")
        headerFrame.columnconfigure(0, weight=1)
        headerFrame.columnconfigure(1, weight=1)
        headerFrame.columnconfigure(2, weight=1)
        headerFrame.columnconfigure(3, weight=1)

        self.l1text = 'Label 1'
        self.l2text = 'Label 2'
        self.l3text = 'Label 3'
        self.l4text = 'Label 4'

        self.label1 = ttk.Label(headerFrame,text=self.l1text)
        self.label2 = ttk.Label(headerFrame,text=self.l2text)
        self.label3 = ttk.Label(headerFrame,text=self.l3text)
        self.label4 = ttk.Label(headerFrame,text=self.l4text)

        #---------------- GRID CONFIGURATION

        self.label1.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.label2.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.label3.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.label4.grid(row=0, column=3, sticky=tk.W+tk.E)"""


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("580x500")
    root.title("Sample GUI")

    sample = SampleGUI(master=root)
    sample.pack(fill="both", expand=True)

    root.mainloop()