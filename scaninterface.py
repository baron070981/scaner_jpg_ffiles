import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



class ScanWindow(tk.Tk):
    def __init__(self):
        super(ScanWindow, self).__init__()
        
        self.label_path = tk.Label(text = 'Путь к файлам')
        self.entry_path = tk.Entry()
        self.label_toch = tk.Label(text = 'точность поиска(0-100)')
        self.entry_toch = tk.Entry()
        
        self.start_btn = tk.Button(text = 'start')
        self.stop_btn = tk.Button(text = 'stop')
        
        
        self.label_path.grid(column = 0, row = 0)
        self.entry_path.grid(column = 1, row = 0)
        self.label_toch.grid(column = 0, row = 1)
        self.entry_toch.grid(column = 1, row = 1)
        self.start_btn.grid(column = 0, row = 2)
        self.stop_btn.grid(column = 1, row = 2)
    
    
    def init_widgets(self):
        pass









if __name__ == '__main__':
    root = ScanWindow()
    
    
    root.mainloop()



