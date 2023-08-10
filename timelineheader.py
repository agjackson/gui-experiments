#!/usr/bin/env python

import tkinter as tk
from tkinter import * 
from tkinter import (ttk, filedialog as fd)

class TimelineHeader(ttk.Frame):
    def __init__(self,master=None):

        self.root = tk.Tk()

        ttk.Frame.__init__(self, master)
        #self.pack(fill='x',anchor='center')
        self.pack(padx=5, pady=10)

        LABEL_WIDTH = 25  # we can change this
        PADDING = 5

        labelFrame = tk.Frame(self.root)
        labelFrame.columnconfigure(0, weight=1)
        labelFrame.columnconfigure(1, weight=1)
        labelFrame.columnconfigure(2, weight=1)
        labelFrame.columnconfigure(3, weight=1)

        # timeline colors
        self.bg_selected = 'orange'
        self.fg_selected = '#f9a602'
        self.bg_unselected = '#fce5cd'
        self.fg_unselected = '#b1560f'

        self.imp_text = 'Import data'
        self.import_label = ttk.Label(self,text=self.imp_text,font=('Arial', 14),width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.import_label['background'] = self.bg_selected
        self.import_label['foreground'] = self.fg_selected

        self.set_text = 'Redaction scope'
        self.settings_label = ttk.Label(self,text=self.set_text,font=('Arial', 14),width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.settings_label['background'] = self.bg_unselected
        self.settings_label['foreground'] = self.fg_unselected

        self.red_text = 'Review and revise'
        self.review_label = ttk.Label(self,text=self.red_text,font=('Arial', 14),width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.review_label['background'] = self.bg_unselected
        self.review_label['foreground'] = self.fg_unselected

        self.exp_text = 'Export data'
        self.export_label = ttk.Label(self,text=self.exp_text,font=('Arial', 14),width=LABEL_WIDTH,padding=PADDING,anchor='center')
        self.export_label['background'] = self.bg_unselected
        self.export_label['foreground'] = self.fg_unselected

        self.current_step = self.import_label

        """self.import_label.pack(padx=5, pady=5)
        self.settings_label.pack(padx=5, pady=5)
        self.review_label.pack(padx=5, pady=5)
        self.export_label.pack(padx=5, pady=5)"""

        self.import_label.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.settings_label.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.review_label.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.export_label.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.root.mainloop()


    def swap_active_color(self,lbl):
        self.current_step['background'] = self.bg_unselected
        self.current_step['foreground'] = self.fg_unselected
        self.current_step = lbl
        self.current_step['background'] = self.bg_selected
        self.current_step['foreground'] = self.fg_selected


    def next_step(self):
        txt = self.current_step['text']
        if(txt == self.imp_text):
            self.swap_active_color(self.settings_label)
        elif(txt == self.set_text):
            self.swap_active_color(self.review_label)
        elif(txt == self.red_text):
            self.swap_active_color(self.export_label)


    def prev_step(self):
        txt = self.current_step['text']
        if(txt == self.set_text):
            self.swap_active_color(self.import_label)
        elif(txt == self.red_text):
            self.swap_active_color(self.settings_label)
        elif(txt == self.exp_text):
            self.swap_active_color(self.review_label)


TimelineHeader()