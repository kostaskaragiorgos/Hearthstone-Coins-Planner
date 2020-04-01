"""
helps you to plan your coins for the next hearthstone expansion and the solo run
"""
import csv
import os
import datetime
from tkinter import Menu
from tkinter import messagebox as msg 
from tkinter import simpledialog
import tkinter as tk
import pandas as pd
def soloplan():
    df = pd.read_csv('soloplanning.csv')
    df = df.drop_duplicates(keep="first")
    msg.showinfo("SOLO PLANS", str(df))
def showplan():
    df = pd.read_csv('planning.csv')
    df = df.drop_duplicates(keep="first")
    msg.showinfo("COIN PLANS", str(df))
def helpmenu():
    """ help menu function"""
    msg.showinfo("Help", "Hearthstone coin planner help\n 1.Press the button PLAN YOUR COINS\n 2. Answer all the pop up questions \n 3. A pop up window will give you the answer you want. \n 4. Every plan is saved to a csv file")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About HEARTHSTONE COIN PLANNER 2.0", "Hearthstone Coin Planner\n"+"Version: 2.0\n"+"Credits:Kostas karagiorgos\n"
                 +"Hearthstone is a card game from Blizzard\n"+"Hearthstone official site:https://playhearthstone.com/en-us/")
class coin_planner(tk.Tk):
    """ coin_planner class """
    def __init__(self):
        super().__init__()
        self.title("HEARTHSTONE COIN PLANNER")
        self.geometry("500x100")
        self.resizable(False, False)
        now = datetime.date.today()
        self.daydiff = datetime.date(2019, 8, 6) - now
        self.welcomeleb = tk.Label(self, text="Welcome to hearthstone coin planner\n An app that helps you to plan ahead for the next hearthstone expansion")
        self.welcomeleb.pack()
        self.planyourcoins = tk.Button(self, text="PLAN YOUR COINS", command=self.coin_plan)
        self.planyourcoins.pack()
        self.planyoursolo = tk.Button(self, text="PLAN YOUR SOLO", command=self.plansolo)
        self.planyoursolo.pack()
        if not os.path.exists('planning.csv'):
            with open('planning.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['COINS HAVE', 'COINS REACH', 'COINS PER DAY', 'DAYS NEEDED'])        
        if not os.path.exists('soloplanning.csv'):
            with open('soloplanning.csv', 'a+') as e:
                thewriter = csv.writer(e)
                thewriter.writerow(['COINS HAVE', 'COINS TO REACH FOR 1 SOLO', 'COINS TO REACH FOR THE FULL SOLO', 'COINS PER DAY', 'DAYS NEEDED FOR 1 SOLO', 'DAYS NEEDED FOR THE FULL SOLO'])
        self.menu = Menu(self)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Plan your coins", accelerator='Ctrl+P', command=self.coin_plan)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.nextexpansion = Menu(self.menu, tearoff=0)
        self.nextexpansion.add_command(label="Release Date", accelerator='Ctrl+R', command=self.rday)
        self.nextexpansion.add_command(label="Days from today", accelerator='Ctrl+D', command=self.difdays)
        self.menu.add_cascade(label="Expansion", menu=self.nextexpansion)
        self.showplans = Menu(self.menu, tearoff=0)
        self.showplans.add_command(label="Show Plans", accelerator='Alt+P', command=showplan)
        self.showplans.add_command(label="Show Solo Plans", accelerator='Alt+S', command=soloplan)
        self.menu.add_cascade(label="Show", menu=self.showplans)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.help_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.config(menu=self.menu)
        self.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.bind('<Control-F1>', lambda event: helpmenu())
        self.bind('<Control-i>', lambda event: aboutmenu())
        self.bind('<Control-p>', lambda event: self.coin_plan())
        self.bind('<Alt-s>', lambda event: soloplan())
        self.bind('<Control-r>', lambda event: self.rday())
        self.bind('<Control-d>', lambda event: self.difdays())
        self.bind('<Alt-p>', lambda event: showplan())
    def plansolo(self):
        """ plan for the solo"""
        self.solo1 = 700
        self.solototal = 700*4
        self.coinshavesolo = simpledialog.askinteger("COINS HAVE", "How many coins do you have?", parent=self, minvalue=0)
        while self.coinshavesolo is None:
            self.coinshavesolo = simpledialog.askinteger("COINS HAVE", "How many coins do you have?", parent=self, minvalue=0)
        self.solocoinsperday = simpledialog.askinteger("COINS PER DAY", "How many coins do you get per day?", parent = self, minvalue=1, maxvalue=1000)
        while self.solocoinsperday is None:
            self.solocoinsperday = simpledialog.askinteger("COINS PER DAY", "How many coins do you get per day?", parent=self, minvalue=1, maxvalue=1000)
        diffsolo1 = self.solo1 - self.coinshavesolo
        msg.showinfo("DAYS YOU NEED", "You need "+str(diffsolo1//self.solocoinsperday)+" days to get "+str(self.solo1)+" from "+str(self.coinshavesolo)+" earning " +str(self.solocoinsperday)+" coins per day.")
    def coin_plan_user_input(self):
        self.coinshave = simpledialog.askinteger("COINS HAVE", "How many coins do you have?", parent=self, minvalue=0)
        while self.coinshave is None:
            self.coinshave = simpledialog.askinteger("COINS HAVE", "How many coins do you have?", parent=self, minvalue=0)   
        self.coinsget = simpledialog.askinteger("COINS REACH", "How many coins do you want to reach?", parent=self, minvalue=self.coinshave+1)
        while self.coinsget is None:
            self.coinsget = simpledialog.askinteger("COINS REACH", "How many coins do you want to reach?", parent=self, minvalue=self.coinshave+1)
        self.coinsperday = simpledialog.askinteger("COINS PER DAY", "How many coins do you get per day?", parent=self, minvalue=1, maxvalue=self.coinsget-self.coinshave)
        while self.coinsperday is None:
            self.coinsperday = simpledialog.askinteger("COINS PER DAY", "How many coins do you get per day?", parent=self, minvalue=1, maxvalue=self.coinsget-self.coinshave)
    def coin_plan(self):
        self.coin_plan_user_input()
        if self.daydiff.days > 0 and (self.coinsget - self.coinshave) > self.daydiff:
            msg.showinfo("DAYS YOU NEED", "You need "+str((self.coinsget - self.coinshave)//self.coinsperday)+" days to get "+str(self.coinsget)+" from "+str(self.coinshave)+" earning " +str(self.coinsperday)+" coins per day.You will not be able to collect the coins you want on time for the new expansion.")
        elif self.daydiff.days > 0 and  (self.coinsget - self.coinshave) > self.daydiff:
            msg.showinfo("DAYS YOU NEED", "You need "+str((self.coinsget - self.coinshave)//self.coinsperday)+" days to get "+str(self.coinsget)+" from "+str(self.coinshave)+" earning " +str(self.coinsperday)+" coins per day.You will be able to collect the coins you want on time for the new expansion.")
        else:
            msg.showinfo("DAYS YOU NEED", "You need "+str((self.coinsget - self.coinshave)//self.coinsperday)+" days to get "+str(self.coinsget)+" from "+str(self.coinshave)+" earning " +str(self.coinsperday)+" coins per day.")
        with open('planning.csv', 'a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([str(self.coinshave), str(self.coinsget), str(self.coinsperday), str((self.coinsget - self.coinshave)//self.coinsperday)])
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.destroy()
    def rday(self):
        """ the release date of the expansion """
        if self.daydiff.days < 0:
            msg.showinfo("Release Date", "The new expansion has not been announced")
        else:
            msg.showinfo("NEXT EXPANSION RELEASE DATE", "THE NEXT EXPANSION SAVIORS OF ULDUM WILL BE LIVE AT 06/09/2019")
    def difdays(self):
        """ release date difference"""
        if self.daydiff.days < 0:
            msg.showinfo("Release Date", "The new expansion has not been announced")
        else:
            msg.showinfo("Release Date Difference", "There are "+str(self.daydiff.days)+" days until the expansion release")
if __name__ == "__main__":
    cp = coin_planner()
    cp.mainloop()
