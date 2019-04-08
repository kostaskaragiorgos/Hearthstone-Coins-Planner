import csv
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg 

class coin_planner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HEARTHSTONE COIN PLANNER")
        self.geometry("290x150")
        self.resizable(False,False)
        self.planyourcoins = tk.Button(self,text = "PLAN YOUR COINS",command = self.planc)
        self.planyourcoins.pack()
        self.menu = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File", menu = self.file_menu)

        self.help_menu = tk.Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label="Help",command=self.helpmenu)
        self.help_menu.add_command(label="About",command = self.aboutmenu)
        self.menu.add_cascade(label="Help",menu = self.help_menu)

        self.config(menu=self.menu)
    
    def planc(self):
        pass
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass
    
    

if __name__ =="__main__":
    cp = coin_planner()
    cp.mainloop()
