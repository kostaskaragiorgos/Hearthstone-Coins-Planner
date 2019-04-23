import csv
import os
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg 
from tkinter import simpledialog
class coin_planner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HEARTHSTONE COIN PLANNER")
        self.geometry("290x100")
        self.resizable(False,False)
        self.planyourcoins = tk.Button(self,text = "PLAN YOUR COINS",command = self.planc)
        self.planyourcoins.pack()
        if os.path.exists('planning.csv') == False:
            with open('planning.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['COINS HAVE','COINS REACH','COINS PER DAY','DAYS NEEDED'])
                f.close()
        self.menu = Menu(self)
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File", menu = self.file_menu)

        self.help_menu = Menu(self.menu,tearoff = 0)
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
        msg.showinfo("DAYS YOU NEED","You need "+str(diff//self.coinsperday)+" days to get "+str(self.coinsget)+" from "+str(self.coinshave)+" earning " +str(self.coinsperday)+" coins per day.")
        with open('planning.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([str(self.coinshave),str(self.coinsget),str(self.coinsperday),str(diff//self.coinsperday)])
            d.close()
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.destroy()
    
    def helpmenu(self):
        msg.showinfo("Help" ,"Hearthstone coin planner help\n 1.Press the button PLAN YOUR COINS\n 2. Answer all the pop up questions \n 3. A pop up window will give you the answer you want. \n 4. Every plan is saved to a csv file")
    
    def aboutmenu(self):
        msg.showinfo("About HEARTHSTONE COIN PLANNER 2.0","Hearthstone Coin Planner\n"+"Version: 2.0\n"+"Credits:Kostas karagiorgos\n"
                     +"Hearthstone is a card game from Blizzard\n"+"Hearthstone official site:https://playhearthstone.com/en-us/")

    
    

if __name__ =="__main__":
    cp = coin_planner()
    cp.mainloop()
