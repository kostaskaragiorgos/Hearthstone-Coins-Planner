import csv
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg 
from tkinter import simpledialog
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
        self.coinshave = simpledialog.askinteger("COINS HAVE","How many coins do you have?",parent = self,minvalue = 0)
        while self.coinshave is None:
            self.coinshave = simpledialog.askinteger("COINS HAVE","How many coins do you have?",parent = self,minvalue = 0)   
        self.coinsget = simpledialog.askinteger("COINS REACH","How many coins do you want to reach?",parent=self , minvalue= self.coinshave+1)
        while self.coinsget is None:
            self.coinsget = simpledialog.askinteger("COINS REACH","How many coins do you want to reach?",parent=self , minvalue= self.coinshave+1)
        self.coinsperday = simpledialog.askinteger("COINS PER DAY","How many coins do you get per day?",parent = self , minvalue  = 1 , maxvalue = self.coinsget-self.coinshave)
        while self.coinsperday is None:
            self.coinsperday = simpledialog.askinteger("COINS PER DAY","How many coins do you get per day?",parent = self , minvalue  = 1 , maxvalue = self.coinsget-self.coinshave)
        diff = self.coinsget - self.coinshave
        msg.showinfo("DAYS YOU NEED","You need"+str(diff//self.coinsperday)+"days to get"+str(self.coinsget)+"from"+str(self.coinshave))
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
