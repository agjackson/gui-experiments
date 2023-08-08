#!/usr/bin/env python

import tkinter as tk
from tkinter import *
from tkinter import ttk

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

        """     Some popular available events:
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
        <Leave>: Mouse pointer leaves widget."""

EventBinding()