import os
import sqlite3 
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg 

class coinplanner(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("HEARTHSTONE COIN PLANNER")
        self.geometry("300x300")
        self.resizable(False,False)
        coinshave = tk.Label(self,text = "How many coins do you have?")
        coinshave.pack(side=tk.TOP)
        self.coinshaveen =tk.Text(self,height = 1)
        self.coinshaveen.pack(side=tk.TOP)

        self.menu = tk.Menu(self,bg = "lightgray" , fg = "black")
        self.file_menu = tk.Menu(self.menu,tearoff = 0, bg = "lightgray",fg = "black" )
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File", menu = self.file_menu)

        self.help_menu = tk.Menu(self.menu , tearoff =0, bg = "lightgray", fg = "black")
        self.help_menu.add_command(label="Help",accelerator= 'Alt+H',command=self.helpmenu)
        self.help_menu.add_command(label="About",command = self.aboutmenu)
        self.menu.add_cascade(label="Help",menu = self.help_menu)

        self.config(menu=self.menu)
   
        global ok1
        self.ok1 =False
        global ok2
        self.ok2 = False
        global ok3
        self.ok3 = False

        global checkch
        global checkre

        global  checkcpd

        self.coins_have_check_button= tk.Button(text= "CHECK",
                                                command=self.checkbcoinshave)
        self.coins_have_check_button.pack()

        self.coins_have_reset_button= tk.Button(text= "RESET",
                                                command=self.resetbcoinshave)
        self.coins_have_reset_button.pack()

        coinsreach = tk.Label(self,text = "How many coins do you want to reach?")
        coinsreach.pack()
        self.coinsreachen = tk.Text(self,height = 1,state="disabled")
        self.coinsreachen.pack()



        self.coins_reach_check_button = tk.Button(text= "CHECK",
                                                   command = self.checkbcoinsreach,state="disabled")
        self.coins_reach_check_button.pack()

        self.coins_reach_reset_button = tk.Button(text= "RESET",
                                                   command = self.resetbcoinsreach,state="disabled")
        self.coins_reach_reset_button.pack()


        coinsperday = tk.Label(self,text = "How many coins do you earn per day?")
        coinsperday.pack(side=tk.TOP)
        self.coinsperdayen = tk.Text(self,height = 1,state="disabled")
        self.coinsperdayen.pack(side=tk.TOP)

        self.coins_perday_check_button = tk.Button(text= "CHECK",
                                                   command = self.checkbcoinsperday,state="disabled")
        self.coins_perday_check_button.pack(side=tk.TOP)

        self.coins_perday_reset_button = tk.Button(text= "RESET",
                                                   command = self.resetbcoinsperday ,state="disabled")
        self.coins_perday_reset_button.pack(side=tk.TOP)

        self.computebutton = tk.Button(text="COMPUTE", command = self.conpute,state="disabled")
        self.computebutton.pack(side=tk.TOP)

    def checkbcoinshave(self):
        self.coinsreachen.configure(state="normal")
        self.coins_reach_check_button.configure(state="normal")
        self.coins_reach_reset_button.configure(state="normal")
        self.checkch = self.coinshaveen.get(1.0,tk.END)
        self.inplist= self.coinshaveen.get(1.0,tk.END)
        try:
            int(self.checkch)
        except:
            self.coinshaveen.delete(1.0,tk.END)
            msg.showinfo("ERROR","YOU HAVE TO ENTER A  NUMBER")
        else:
            if int(self.checkch) >= 0:
                self.ok1 = True
            else:
                self.ok1 = False
                self.coinshaveen.delete(1.0,tk.END)
                msg.showinfo("ERROR","YOU HAVE TO ENTER A POSITIVE  NUMBER")



    def resetbcoinshave(self):
        self.coinshaveen.delete(1.0,tk.END)


    def checkbcoinsreach(self):
        self.coinsperdayen.configure(state="normal")
        self.coins_perday_check_button.configure(state="normal")
        self.coins_perday_reset_button.configure(state="normal")
        self.checkre = self.coinsreachen.get(1.0,tk.END)
        try:
            int(self.checkre)
        except:
            self.coinsreachen.delete(1.0,tk.END)
            msg.showinfo("ERROR","YOU HAVE TO ENTER A  NUMBER")
        else:
            if int(self.checkre) > int(self.checkch):
                self.ok2 = True
            else:
                self.ok2 = False
                self.coinsreachen.delete(1.0,tk.END)
                msg.showinfo("ERROR", "YOU HAVE TO ENTER A NUMBER BIGGER THAN THE COINS YOU HAVE ")

    def resetbcoinsreach(self):
        self.coinsreachen.delete(1.0,tk.END)

    def checkbcoinsperday(self):
        self.checkcpd = self.coinsperdayen.get(1.0,tk.END)
        self.computebutton.configure(state = "normal")
        try:
            int(self.checkcpd)
        except:
            self.coinsperdayen.delete(1.0,tk.END)
            msg.showinfo("ERROR","YOU HAVE TO ENTER A  NUMBER")
        else:
            if int(self.checkcpd) > 0:
                self.ok3 = True
            else:
                self.ok3 = False
                self.coinsperdayen.delete(1.0,tk.END)
                msg.showinfo("ERROR","YOU HAVE TO ENTER A POSITIVE  NUMBER")
                    
        
    def resetbcoinsperday(self):
        self.coinsperdayen.delete(1.0,tk.END)

    def conpute(self):
        self.diff =   int(self.checkre)-int(self.checkch)
        self.daysneed =int(self.diff)//int(self.checkcpd)
        if self.ok1 == self.ok2 == self.ok3 == True:
            msg.showinfo("COMPUTE", "YOU HAVE:"+self.coinshaveen.get(1.0,tk.END)+"COINS.TO GET"+self.coinsreachen.get(1.0,tk.END)+"YOU HAVE TO PLAY HEARTHSTONE FOR"
                         +str(self.daysneed)+"DAYS EARNING "+self.coinsperdayen.get(1.0,tk.END) + "PER DAY")

    def aboutmenu(self):
        msg.showinfo("About HEARTHSTONE COIN PLANNER 1.0","Hearthstone Coin Planner\n"+"Version: 1.0\n"+"Credits:Kostas karagiorgos\n"
                     +"Hearthstone is a card game from Blizzard\n"+"Hearthstone official site:https://playhearthstone.com/en-us/")

    def helpmenu(self):
        msg.showinfo("Help","The purpose of this app is to help hearthstone players calculate the days needed to earn a desirable amount of gold.\n"
                     +"You have to enter 3 integers answering the questions."
                     +"You have to check every value in order to compute.")

    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.destroy()
        
if __name__ =="__main__":
    cp = coinplanner()
    cp.mainloop()
