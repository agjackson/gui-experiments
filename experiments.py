#!/usr/bin/env python
import tkinter as tk
from tkinter import *
from tkinter import ttk

class StyleExp:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Style Experiments")

        # ------------------- STYLING
        s = ttk.Style()
        s.configure('mainFrame.TFrame', background = '#759304')
        s.configure('frame2.TFrame', background = '#F83FF3')


        # ------------------- WIDGETS
        mainFrame = ttk.Frame(self.root, width=250, height=250, style='mainFrame.TFrame')
        mainFrame.grid()

        frame2 = ttk.Frame(mainFrame, width= 100, height=100, style='frame2.TFrame')
        frame2.grid(padx = 10, pady = 10)

        # ------------------- GRID CONFIGURATION



        self.root.resizable(width=False, height=False)
        self.root.mainloop()

#StyleExp()

class DropDownMenu:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Menu")
        self.root.geometry( "200x200" )
  
        # Change the label text
        def show():
            label.config(text = clicked.get())
  
        options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  
        clicked = StringVar()
        clicked.set( "Monday" )
  
        # Create Dropdown menu
        drop = OptionMenu(self.root, clicked, *options)
        drop.pack()
  
        # Create button, it will change label text
        button = Button(self.root , text = "Show Choice", command = show).pack()
  
        # Create Label
        label = Label(self.root, text = " ")
        label.pack()

        self.root.mainloop()

#DropDownMenu()

class DifferentWidgets:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Widget Experiments")

        content = ttk.Frame(self.root, padding=(3,3,12,12))
        frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
        namelbl = ttk.Label(content, text="Name")
        name = ttk.Entry(content)

        onevar = BooleanVar()
        twovar = BooleanVar()
        threevar = BooleanVar()

        onevar.set(True)
        twovar.set(False)
        threevar.set(True)

        one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
        ok = ttk.Button(content, text="Okay")
        cancel = ttk.Button(content, text="Cancel")

        content.grid(column=0, row=0, sticky=(N, S, E, W))
        frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
        name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
        one.grid(column=0, row=3)
        two.grid(column=1, row=3)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=3)
        cancel.grid(column=4, row=3)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=3)
        content.columnconfigure(1, weight=3)
        content.columnconfigure(2, weight=3)
        content.columnconfigure(3, weight=1)
        content.columnconfigure(4, weight=1)
        content.rowconfigure(1, weight=1)

        self.root.mainloop()

DifferentWidgets()

class EventBinding:
    def __init__(self):
        
        self.root = tk.Tk()
        l =ttk.Label(self.root, text="Starting...")
        l.grid()
        l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
        l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
        l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
        l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
        l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
        l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
        self.root.mainloop()

        """Other events:
        <Activate>: Window has become active.
        <Deactivate>: Window has been deactivated.
        <MouseWheel>: Scroll wheel on mouse has been moved.
        <KeyPress>: Key on keyboard has been pressed down.
        <KeyRelease>: Key has been released.
        <ButtonPress>: A mouse button has been pressed.
        <ButtonRelease>: A mouse button has been released.
        <Motion>: Mouse has been moved.
        <Configure>: Widget has changed size or position.
        <Destroy>: Widget is being destroyed.
        <FocusIn>: Widget has been given keyboard focus.
        <FocusOut>: Widget has lost keyboard focus.
        <Enter>: Mouse pointer enters widget.
        <Leave>: Mouse pointer leaves widget"""

#EventBinding()
