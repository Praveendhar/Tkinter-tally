from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk

# def account():
#     global Canvas1
#     Canvas1 = tk.Canvas( background="#3a646b", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
#     Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)


#     global Canvas2
#     Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
#     Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

#     global Canvas3
#     Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
#     Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)
def chartofaccounts():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)
    Canvas1

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white").place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)

    global canvas4
    Canvas4 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0.550, rely=0.4, relheight=0.200, relwidth=.150)

    Label1 = Label(Canvas3,text='List of masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.400,relwidth=.150)
    # Label2 = Label(Canvas3,text='Accounting masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.450,relwidth=.150)
    # Label3 = Label(Canvas3,text='Inventory masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.402,relwidth=.150)
    b1 = Button(Canvas3,text = "Groups",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.551, rely=0.450,relwidth=.148)
    b2 = Button(Canvas3,text = "Ledgers",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.480,relwidth=.148)
    b3 = Button(Canvas3,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.520,relwidth=.148)

global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#3a646b")
screen.configure(cursor="arrow")

global Canvas1
Canvas1 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)

global canvas4
Canvas4 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas4.place(relx=0.550, rely=0.4, relheight=0.200, relwidth=.150)

name = Label(screen, text="TallyPrime", fg='pink',bg='#3a646b',font=("Arial", 13),anchor='w').place(x = 1,y = 0)

b1 = Button(screen,text = "Company",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=120,y=33)
b2 = Button(screen,text = "Data",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=275,y=33)
b3 = Button(screen,text = "Exchange",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=395,y=33)
b4 = Button(screen,text = " Go To ",activeforeground = "black", activebackground = "white",fg='black',bg='white',borderwidth=0,underline=2,font=('Arial 10 bold'),).place (x=565,y=33)
b5 = Button(screen,text = "Import",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=825,y=33)
b6 = Button(screen,text = "Export",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=925,y=33)
b7 = Button(screen,text = "E-mail",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1025,y=33)
b8 = Button(screen,text = "Print",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1127,y=33)
b9 = Button(screen,text = "Help",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1227,y=33)

Label6 = Label(screen,text='Gateway of tally', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.400,relwidth=.150)
b10 = Button(screen,text = "Chart of accounts",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.551, rely=0.450,relwidth=.148)
b11 = Button(screen,text = "Vouchers",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.480,relwidth=.148)
b12 = Button(screen,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.520,relwidth=.148)

# Chart of accounts section



screen.mainloop()