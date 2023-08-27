#!/usr/bin/env python

import tkinter as tk
import tkinter.messagebox
from tkinter import (ttk, filedialog as fd)

WHITE = '#FAF9F6'
SOFT_ORANGE = '#FBBF77'
ORANGE = '#F28500'
BLACK = '#0C0908'
GREY = '#545454'

class SampleGUI(ttk.Frame):
    def __init__(self):
        super().__init__()

        NORM_FONT = ('Arial', 20)
        HEADER_FONT = ('Arial', 18)
        SMALL_FONT = ('Arial', 16)
        BOLD_FONT = ('Arial', 20, 'bold')

        LABEL_WIDTH = 25 
        PADDING = 5

        #------- WIDGETS

        mainframe = ttk.Frame(self,borderwidth=3,padding="60 12 12 12", relief="ridge")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        headerframe = ttk.Frame(mainframe,borderwidth=3, padding="12 12 12 12")

        self.imp = ttk.Label(headerframe,text='Import data',font=HEADER_FONT,width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.imp['background'] = ORANGE
        self.imp['foreground'] = WHITE

        self.sett = ttk.Label(headerframe,text='Project settings',font=HEADER_FONT,width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.sett['background'] = SOFT_ORANGE
        self.sett['foreground'] = ORANGE

        self.rev = ttk.Label(headerframe,text='Review redactions',font=HEADER_FONT,width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.rev['background'] = SOFT_ORANGE
        self.rev['foreground'] = ORANGE

        self.exp = ttk.Label(headerframe,text='Export data',font=HEADER_FONT,width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.exp['background'] = SOFT_ORANGE
        self.exp['foreground'] = ORANGE

        self.selection = ttk.Label(mainframe, text='Select files to redact: ', font=NORM_FONT)

        self.browse = ttk.Button(mainframe, text='Browse')

        self.nofiles = ttk.Label(mainframe, text='No files selected', font=NORM_FONT)

        self.notice = ttk.Label(mainframe, text='Currently, we only accept CSV and TXT files.', font=SMALL_FONT)
        self.notice['foreground'] = GREY

        self.preview = ttk.Label(mainframe, text='File Preview', font=BOLD_FONT)

        self.file = ttk.Frame(mainframe, width=1000, height=400, borderwidth=5, relief="ridge")

        self.back = ttk.Button(mainframe, text='<< Go Back')

        self.cont = ttk.Button(mainframe, text='Save and Continue >>')

        #------- GRID CONFIGURATION

        mainframe.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
        headerframe.grid(column=0, row=0, columnspan=4, sticky=(tk.N,tk.W,tk.E,tk.S))

        self.imp.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.sett.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.rev.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.exp.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.selection.grid(column=0, row=1, sticky=(tk.N, tk.W), padx=5)
        self.browse.grid(column=1, row=1, sticky=(tk.N, tk.W), padx=5)
        self.nofiles.grid(column=2, row=1, columnspan=2,sticky=(tk.N, tk.W), padx=5)
        self.notice.grid(column=0, row=2, sticky=(tk.N, tk.W), padx=5)
        self.preview.grid(column=0, row=3, sticky=(tk.N, tk.W), padx=5)
        self.file.grid(column=0,row=4, columnspan=4, sticky=(tk.N, tk.W), padx=5)
        self.back.grid(column=0, row=5)
        self.cont.grid(column=4, row=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Arlie's GUI")

    root.configure(bg=WHITE)           # doesn't work with Tk 8.5

    width = root.winfo_screenwidth()               
    height = root.winfo_screenheight()               
    root.geometry("%dx%d" % (width, height))
    root.resizable(False,True)

    root.minsize(width=800,height=500)   

    app = SampleGUI()
    app.pack(fill="both", expand=True)

    root.mainloop()