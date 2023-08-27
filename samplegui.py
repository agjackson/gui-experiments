#!/usr/bin/env python

import tkinter as tk
import tkinter.messagebox
from tkinter import (ttk, filedialog as fd)

WHITE = '#FAF9F6'
SOFT_ORANGE = '#FBBF77'
ORANGE = '#F28500'
BLACK = '#0C0908'
GRAY = '#545454'

class SampleGUI(ttk.Frame):
    def __init__(self):
        super().__init__()

        BOLD_FONT = ('Arial', 22, 'bold')
        NORM_FONT = ('Arial', 20)
        SMALL_FONT = ('Arial', 16)

        LABEL_WIDTH = 25 
        PADDING = 5

        # ------------------- STYLING
        s = ttk.Style()
        s.configure('selected.TLabel', foreground = WHITE,background = ORANGE, font = BOLD_FONT)
        s.configure('deselected.TLabel', foreground = ORANGE, background = SOFT_ORANGE, font = BOLD_FONT)

        s.configure('norm.TLabel', font = NORM_FONT)
        s.configure('small.TLabel', foreground = GRAY, font = SMALL_FONT)

        #------- WIDGETS

        mainframe = ttk.Frame(self,borderwidth=3,padding="60 12 12 12", relief="ridge")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        headerframe = ttk.Frame(mainframe,borderwidth=3, padding="24 12 12 12")

        self.imp = ttk.Label(headerframe,text='Import data',style='selected.TLabel',width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.sett = ttk.Label(headerframe,text='Project settings',style='deselected.TLabel',width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.rev = ttk.Label(headerframe,text='Review redactions',style='deselected.TLabel',width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.exp = ttk.Label(headerframe,text='Export data',style='deselected.TLabel',width=LABEL_WIDTH,padding=PADDING,anchor='center')

        spacer1 = ttk.Label(mainframe, text='')

        self.selection = ttk.Label(mainframe, text='Select files to redact: ', style='norm.TLabel')
        self.browse = ttk.Button(mainframe, text='Browse')
        self.nofiles = ttk.Label(mainframe, text='No files selected', style='norm.TLabel')
        self.notice = ttk.Label(mainframe, text='Currently, we only accept CSV and TXT files.', style='small.TLabel')

        spacer2 = ttk.Label(mainframe, text='')

        self.preview = ttk.Label(mainframe, text='File Preview', font=BOLD_FONT)
        self.file = ttk.Frame(mainframe, width=1000, height=400, borderwidth=5, relief="ridge")

        self.back = ttk.Button(mainframe, text='<< Go Back')
        self.cont = ttk.Button(mainframe, text='Save and Continue >>')
        self.cont.state(['disabled']) 

        #------- GRID CONFIGURATION

        mainframe.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))


        headerframe.grid(column=0, row=0, columnspan=4, sticky=(tk.N,tk.W,tk.E,tk.S))

        self.imp.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.sett.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.rev.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.exp.grid(row=0, column=3, sticky=tk.W+tk.E)

        spacer1.grid(column=0, row=1, columnspan=4, pady=26)

        self.selection.grid(column=0, row=2, sticky=(tk.N, tk.W), pady=5)
        #self.selection.pack(padx=5,pady=15,side=tk.LEFT)
        self.browse.grid(column=1, row=2, sticky=(tk.N, tk.W), pady=5)
        self.nofiles.grid(column=2, row=2, columnspan=2,sticky=(tk.N, tk.W), pady=5)
        self.notice.grid(column=0, row=3, sticky=(tk.N, tk.W), padx=5)

        spacer2.grid(column=0, row=4, columnspan=4, pady=26)

        self.preview.grid(column=0, row=5, sticky=(tk.N, tk.W), padx=5)
        self.file.grid(column=0,row=6, columnspan=4, sticky=(tk.N, tk.W), padx=5)

        self.back.grid(column=0, row=7,sticky=(tk.N, tk.W), pady=18)
        self.cont.grid(column=3, row=7,sticky=(tk.N, tk.E), pady=18)

        


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Arlie's GUI")

    root.configure(bg=WHITE)           # doesn't work with Tk 8.5

    width = root.winfo_screenwidth()               
    height = root.winfo_screenheight()               
    root.geometry("%dx%d" % (width, height))
    root.resizable(False,True)

    app = SampleGUI()
    app.pack(fill="both", expand=True)

    root.mainloop()