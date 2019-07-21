import csv
import os
import datetime
from datetime import date
from tkinter import Menu
import tkinter as tk
from tkinter import messagebox as msg 
from tkinter import simpledialog
class coin_planner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HEARTHSTONE COIN PLANNER")
        self.geometry("500x70")
        self.resizable(False,False)
        self.welcomeleb = tk.Label(self,text ="Welcome to hearthstone coin planner\n An app that helps you to plan ahead for the next hearthstone expansion")
        self.welcomeleb.pack()
        self.planyourcoins = tk.Button(self,text = "PLAN YOUR COINS",command = self.planc)
        self.planyourcoins.pack()
        if os.path.exists('planning.csv') == False:
            with open('planning.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['COINS HAVE','COINS REACH','COINS PER DAY','DAYS NEEDED'])
                f.close()
                
        self.menu = Menu(self)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Plan your coins", accelerator = 'Ctrl+P',command = self.planc)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File", menu = self.file_menu)
        
        self.nextexpansion = Menu(self.menu,tearoff = 0)
        self.nextexpansion.add_command(label = "Release Date",accelerator = 'Ctrl+R',command = self.rday)
        self.nextexpansion.add_command(label = "Days from today",accelerator = 'Ctrl+D',command = self.difdays)
        self.menu.add_cascade(label = "Expansion",menu = self.nextexpansion)

        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label="Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.help_menu.add_command(label="About",accelerator = 'Ctrl+I',command = self.aboutmenu)
        self.menu.add_cascade(label="Help",menu = self.help_menu)
        
        self.config(menu=self.menu)
        self.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.bind('<Control-F1>',lambda event:self.helpmenu())
        self.bind('<Control-i>',lambda event: self.aboutmenu())
        self.bind('<Control-p>',lambda event: self.planc())
        self.bind('<Control-r>',lambda event:self.rday())
        self.bind('<Control-d>',lambda event:self.difdays())
    
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

    
    def rday(self):
        msg.showinfo("NEXT EXPANSION RELEASE DATE", "THE NEXT EXPANSION SAVIORS OF ULDUM WILL BE LIVE AT 06/09/2019")
    
    def difdays(self):
        reldate = date(2019,8,6)
        today = datetime.datetime.today()
        tday = today.day
        mday = today.month
        yday = today.year
        todaydate = date(yday,mday,tday)
        delta = reldate - todaydate 
        msg.showinfo("Release Date Difference","There are "+str(delta.days)+" days until the expansion release")
        
        
if __name__ =="__main__":
    cp = coin_planner()
    cp.mainloop()
