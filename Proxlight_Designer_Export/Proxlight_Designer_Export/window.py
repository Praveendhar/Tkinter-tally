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

def chartofaccountsgroups():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of masters', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07,relwidth=.100)
    b1 = Button(Canvas2,text = "Branch/Divisions",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10'),command=LOGbranchordivision).place(relx=0, rely=0.12)
    b2 = Button(Canvas2,text = "Capital Account",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10'),command=LOGcapitalaccount).place(relx=0, rely=0.15)
    b3 = Button(Canvas2,text = "Reserves & Surplus",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10'),command=LOGreverseandsurplus).place(relx=0.02, rely=0.18)
    b4 = Button(Canvas2,text = "Current Assets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10'),command=LOGcurrentassets).place(relx=0, rely=0.21)
    b5 = Button(Canvas2,text = "Bank Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.24)
    b6 = Button(Canvas2,text = "Cash in Hand",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.27)
    b7 = Button(Canvas2,text = "Deposits (Asset)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.30)
    b8 = Button(Canvas2,text = "Loans & Advances (Asset)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.33)
    b9 = Button(Canvas2,text = "Stock-in-Hand",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.36)
    b10 = Button(Canvas2,text = "Sundry Debtors",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.39)
    b11 = Button(Canvas2,text = "Current Liabilities",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.42)
    b12 = Button(Canvas2,text = "Duties & Taxes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.45)
    b13 = Button(Canvas2,text = "Provisions",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.48)
    b14 = Button(Canvas2,text = "Sundry Creditors",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.51)
    b15 = Button(Canvas2,text = "Direct Expenses",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.54)
    b16 = Button(Canvas2,text = "Direct Incomes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.57)
    b17 = Button(Canvas2,text = "Fixed Assets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.60)
    b18 = Button(Canvas2,text = "Inderect Expenses",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.63)
    b19 = Button(Canvas2,text = "Inderect Incomes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.66)
    b20 = Button(Canvas2,text = "Investments",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.69)
    b21 = Button(Canvas2,text = "Loans (Liability)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.72)
    b22 = Button(Canvas2,text = "Bank OD A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.75)
    b23 = Button(Canvas2,text = "Secured Loans",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.78)
    b24 = Button(Canvas2,text = "Unsecured Loans",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.02, rely=0.81)
    b25 = Button(Canvas2,text = "Misc Expenses (ASSET)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.84)
    b26 = Button(Canvas2,text = "Purchase Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.87)
    b27 = Button(Canvas2,text = "Sales Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.90)
    b28 = Button(Canvas2,text = "Suspense A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0, rely=0.93)
    b29 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsledgers():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Ledgers', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    Label2 = Label(Canvas2,text='Assets', background="white",foreground="black",font="-family {Segoe Arial} -size 13 -weight bold ").place(relx=0.003, rely=0.1)
    b1 = Button(Canvas2,text = "Current Assets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 11')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "Bank Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.16)
    b3 = Button(Canvas2,text = "Cash in Hand",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.19)
    b4 = Button(Canvas2,text = "Cash",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Papyrus 10')).place(relx=0.02, rely=0.22)
    b5 = Button(Canvas2,text = "Deposits (Asset)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.25)
    b6 = Button(Canvas2,text = "Loans and Advances (Asset)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.28)
    b7 = Button(Canvas2,text = "Stock-In-Hand",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.31)
    b8 = Button(Canvas2,text = "Sundry Debtors",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.34)
    b9 = Button(Canvas2,text = "Fixed Assets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.37)
    b10 = Button(Canvas2,text = "Investments",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.40)
    b11 = Button(Canvas2,text = "Misc. Expenses (ASSET)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.43)
    Label3 = Label(Canvas2,text='Liabilities', background="white",foreground="black",font="-family {Segoe Arial} -size 13 -weight bold ").place(relx=0.003, rely=0.46)
    b12 = Button(Canvas2,text = "Branch/Divisions",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.49)
    b13 = Button(Canvas2,text = "Capital Account",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.52)
    b14 = Button(Canvas2,text = "Reserves & Surplus",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.55)
    b15 = Button(Canvas2,text = "Current Liabilities",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.58)
    b16 = Button(Canvas2,text = "Duties and Taxes",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.61)
    b17 = Button(Canvas2,text = "Provisions",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.64)
    b18 = Button(Canvas2,text = "Sundry Creditors",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.67)
    b19 = Button(Canvas2,text = "Loans (Liability)",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.70)
    b20 = Button(Canvas2,text = "Bank OD A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.73)
    b21 = Button(Canvas2,text = "Secured Loans",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.76)
    b22 = Button(Canvas2,text = "Unsecured Loans",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.01, rely=0.79)
    b23 = Button(Canvas2,text = "Suspense A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.82)
    b24 = Button(Canvas2,text = "Profit & Loss A/c",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Papyrus 10')).place(relx=0.02, rely=0.85)
    Label4 = Label(Canvas2,text="Expenses", background="white",foreground="black",font="-family {Segoe Arial} -size 13 -weight bold ").place(relx=0.3, rely=0.1)
    b25 = Button(Canvas2,text = "Direct Expenses",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.303, rely=0.13)
    b26 = Button(Canvas2,text = "Indirect Expenses",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.303, rely=0.16)
    b27 = Button(Canvas2,text = "Purchase Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.303, rely=0.19)
    Label5 = Label(Canvas2,text="Income", background="white",foreground="black",font="-family {Segoe Arial} -size 13 -weight bold ").place(relx=0.3, rely=0.22)
    b28 = Button(Canvas2,text = "Direct Income",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.303, rely=0.25)
    b29 = Button(Canvas2,text = "Indirect Income",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.303, rely=0.28)
    b30 = Button(Canvas2,text = "Sales Accounts",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.303, rely=0.31)
    b31 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsvouchertypes():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Voucher Types', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    b1 = Button(Canvas2,text = "Attendance",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 11')).place(relx=0.003, rely=0.12)
    b2 = Button(Canvas2,text = "Contra",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 11')).place(relx=0.003, rely=0.15)
    b3 = Button(Canvas2,text = "Credit Note",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.18)
    b4 = Button(Canvas2,text = "Debit Note",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.21)
    b5 = Button(Canvas2,text = "Delivery Note",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.24)
    b6 = Button(Canvas2,text = "Job Work In Order",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.27)
    b7 = Button(Canvas2,text = "Job Work out Order",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.30)
    b8 = Button(Canvas2,text = "Journal",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.33)
    b9 = Button(Canvas2,text = "Material in",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.36)
    b10 = Button(Canvas2,text = "Material out",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.39)
    b11 = Button(Canvas2,text = "Memorandum",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.42)
    b12 = Button(Canvas2,text = "Payment",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.45)
    b13 = Button(Canvas2,text = "Payroll",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.48)
    b14 = Button(Canvas2,text = "Physical Stock",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.51)
    b15 = Button(Canvas2,text = "Purchase",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.54)
    b16 = Button(Canvas2,text = "Purchase Order",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.57)
    b17 = Button(Canvas2,text = "Receipt",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.60)
    b18 = Button(Canvas2,text = "Receipt Note",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.63)
    b19 = Button(Canvas2,text = "Rejections In",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.66)
    b20 = Button(Canvas2,text = "Rejections Out",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.69)
    b21 = Button(Canvas2,text = "Reversing Journal",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.72)
    b22 = Button(Canvas2,text = "Sales",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.75)
    b23 = Button(Canvas2,text = "Sales Order",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.78)
    b24 = Button(Canvas2,text = "Sales Journal",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.81)
    b25 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def LOGbranchordivision():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#8a8a8a", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = tk.Canvas( background="white", relief="ridge").place(relx=0, rely=0.07, relheight=0.500, relwidth=.450)

    Label1 = Label(Canvas3,text='Branch or Division', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0.02, rely=0.07)
    Label2 = Label(Canvas3,text='Name :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.11)
    e1=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.11,relwidth=.180)
    Label3 = Label(Canvas3,text='(alias) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.14)
    e2=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.14,relwidth=.180)
    Label4 = Label(Canvas3,text='Under :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.18)
    Label5 = Label(Canvas3,text='◆Primary', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.10, rely=0.18)
    separator = ttk.Separator(Canvas3, orient='horizontal').place(relx=0, rely=0.23, relheight=0, relwidth=0.450)
    Label6 = Label(Canvas3,text='Nature of Group :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.26)
    combo1 = ttk.Combobox(Canvas3,values=["Assets", "Liabilities"]).place(relx=0.25, rely=0.26)
    Label7 = Label(Canvas3,text='Group behaves like a sub-ledger :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.31)
    combo2 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.31)
    Label8 = Label(Canvas3,text='Nett Debit/Credit Balances for Reporting :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.36)
    combo3 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.36)
    Label9 = Label(Canvas3,text='Used for calculation (for example: taxes,discounts) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.41)
    combo4 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.41)
    Label10 = Label(Canvas3,text='(for sales invoice entries)', background="white",foreground="black",font="-family {Papyrus} -size 10 -weight bold ").place(relx=0.02, rely=0.46)
    Label11 = Label(Canvas3,text='Method to allocate when used in purchase invoice :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.51)
    combo5 = ttk.Combobox(Canvas3,values=["◆Not Applicable", "Appropriate by Qty", "Appropriate by Value"]).place(relx=0.25, rely=0.51)
    # b1 = Button(Canvas2,text = "Main Location",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccountsgroups).place(relx=0.8, rely=0.1)

def LOGcapitalaccount():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#8a8a8a", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = tk.Canvas( background="white", relief="ridge").place(relx=0, rely=0.07, relheight=0.500, relwidth=.450)

    Label1 = Label(Canvas3,text='Capital Account', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0.02, rely=0.07)
    Label2 = Label(Canvas3,text='Name :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.11)
    e1=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.11,relwidth=.180)
    Label3 = Label(Canvas3,text='(alias) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.14)
    e2=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.14,relwidth=.180)
    Label4 = Label(Canvas3,text='Under :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.18)
    Label5 = Label(Canvas3,text='◆Primary', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.10, rely=0.18)
    separator = ttk.Separator(Canvas3, orient='horizontal').place(relx=0, rely=0.23, relheight=0, relwidth=0.450)
    Label6 = Label(Canvas3,text='Nature of Group :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.26)
    Labels14 = Label(Canvas3,text='Liabilities', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.25, rely=0.26)
    Label7 = Label(Canvas3,text='Group behaves like a sub-ledger :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.31)
    combo2 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.31)
    Label8 = Label(Canvas3,text='Nett Debit/Credit Balances for Reporting :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.36)
    combo3 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.36)
    Label9 = Label(Canvas3,text='Used for calculation (for example: taxes,discounts) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.41)
    combo4 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.41)
    Label10 = Label(Canvas3,text='(for sales invoice entries)', background="white",foreground="black",font="-family {Papyrus} -size 10 -weight bold ").place(relx=0.02, rely=0.46)
    Label11 = Label(Canvas3,text='Method to allocate when used in purchase invoice :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.51)
    combo5 = ttk.Combobox(Canvas3,values=["◆Not Applicable", "Appropriate by Qty", "Appropriate by Value"]).place(relx=0.25, rely=0.51)
    # b1 = Button(Canvas2,text = "Main Location",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccountsgroups).place(relx=0.8, rely=0.1)

def LOGreverseandsurplus():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#8a8a8a", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = tk.Canvas( background="white", relief="ridge").place(relx=0, rely=0.07, relheight=0.500, relwidth=.450)

    Label1 = Label(Canvas3,text='Reserves & Surplus', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0.02, rely=0.07)
    Label2 = Label(Canvas3,text='Name :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.11)
    e1=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.11,relwidth=.180)
    Label3 = Label(Canvas3,text='(alias) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.14)
    e2=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.14,relwidth=.180)
    Label4 = Label(Canvas3,text='Under :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.18)
    Label5 = Label(Canvas3,text='Capital Account', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.10, rely=0.18)
    separator = ttk.Separator(Canvas3, orient='horizontal').place(relx=0, rely=0.23, relheight=0, relwidth=0.450)
    Label7 = Label(Canvas3,text='Group behaves like a sub-ledger :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.31)
    combo2 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.31)
    Label8 = Label(Canvas3,text='Nett Debit/Credit Balances for Reporting :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.36)
    combo3 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.36)
    Label9 = Label(Canvas3,text='Used for calculation (for example: taxes,discounts) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.41)
    combo4 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.41)
    Label10 = Label(Canvas3,text='(for sales invoice entries)', background="white",foreground="black",font="-family {Papyrus} -size 10 -weight bold ").place(relx=0.02, rely=0.46)
    Label11 = Label(Canvas3,text='Method to allocate when used in purchase invoice :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.51)
    combo5 = ttk.Combobox(Canvas3,values=["◆Not Applicable", "Appropriate by Qty", "Appropriate by Value"]).place(relx=0.25, rely=0.51)
    # b1 = Button(Canvas2,text = "Main Location",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccountsgroups).place(relx=0.8, rely=0.1)

def LOGcurrentassets():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#8a8a8a", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = tk.Canvas( background="white", relief="ridge").place(relx=0, rely=0.07, relheight=0.500, relwidth=.450)

    Label1 = Label(Canvas3,text='Current Assets', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0.02, rely=0.07)
    Label2 = Label(Canvas3,text='Name :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.11)
    e1=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.11,relwidth=.180)
    Label3 = Label(Canvas3,text='(alias) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.14)
    e2=Entry(Canvas3,bg='#ffdd90').place(relx=0.10,rely=0.14,relwidth=.180)
    Label4 = Label(Canvas3,text='Under :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.18)
    Label5 = Label(Canvas3,text='◆Primary', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.10, rely=0.18)
    separator = ttk.Separator(Canvas3, orient='horizontal').place(relx=0, rely=0.23, relheight=0, relwidth=0.450)
    Label6 = Label(Canvas3,text='Nature of Group :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.26)
    Label12 = Label(Canvas3,text='Assets', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.25, rely=0.26)
    Label7 = Label(Canvas3,text='Group behaves like a sub-ledger :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.31)
    combo2 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.31)
    Label8 = Label(Canvas3,text='Nett Debit/Credit Balances for Reporting :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.36)
    combo3 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.36)
    Label9 = Label(Canvas3,text='Used for calculation (for example: taxes,discounts) :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.41)
    combo4 = ttk.Combobox(Canvas3,values=["Yes", "No"]).place(relx=0.25, rely=0.41)
    Label10 = Label(Canvas3,text='(for sales invoice entries)', background="white",foreground="black",font="-family {Papyrus} -size 10 -weight bold ").place(relx=0.02, rely=0.46)
    Label11 = Label(Canvas3,text='Method to allocate when used in purchase invoice :', background="white",foreground="black",font="-family {Arial} -size 10 -weight bold ").place(relx=0.02, rely=0.51)
    combo5 = ttk.Combobox(Canvas3,values=["◆Not Applicable", "Appropriate by Qty", "Appropriate by Value"]).place(relx=0.25, rely=0.51)
    # b1 = Button(Canvas2,text = "Main Location",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccountsgroups).place(relx=0.8, rely=0.1)


def chartofaccountscurrencies():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Currencies', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsbudgets():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Budgets', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    # b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsscenarios():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Scenarios', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    # b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsstockgroups():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Stock Groups', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    # b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsstockitems():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Stock Items', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    # b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsstockcategories():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Stock Categories', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    # b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsunits():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Unit', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    # b1 = Button(Canvas2,text = "₹",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 13')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccountsgodowns():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    Label1 = Label(Canvas2,text='List of Godowns', background="white",foreground="black",font="-family {Segoe Arial} -size 15 -weight bold ").place(relx=0, rely=0.07)
    b1 = Button(Canvas2,text = "Main Location",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='white',borderwidth=0,font=('Arial 10')).place(relx=0.003, rely=0.13)
    b2 = Button(Canvas2,text = "X",activeforeground = "white", activebackground = "red",fg='white',bg='black',borderwidth=0,font=('Arial 10'),command=chartofaccounts).place(relx=0.8, rely=0.1)

def chartofaccounts():
    global Canvas1
    Canvas1 = tk.Canvas( background="#ffffff", relief="ridge").place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white").place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)

    global canvas4
    Canvas4 = tk.Canvas( background="lightblue", relief="sunken").place(relx=0.35, rely=0.3, relheight=0.500, relwidth=.200)

    Label1 = Label(Canvas3,text='List of masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.35, rely=0.29,relwidth=.200)
    # Label2 = Label(Canvas3,text='Accounting masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.450,relwidth=.150)
    # Label3 = Label(Canvas3,text='Inventory masters', background="#3385ff",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.402,relwidth=.150)
    Label2 = Label(Canvas3,text='Accounting masters', background="Lightblue",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.35, rely=0.33,relwidth=.200)
    b1 = Button(Canvas3,text = "Groups",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsgroups).place(relx=0.35, rely=0.36,relwidth=.200)
    b2 = Button(Canvas3,text = "Ledgers",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsledgers).place(relx=0.35, rely=0.39,relwidth=.200)
    b3 = Button(Canvas3,text = "Voucher Types",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsvouchertypes).place(relx=0.35, rely=0.42,relwidth=.200)
    b4 = Button(Canvas3,text = "Currencies",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountscurrencies).place(relx=0.35, rely=0.45,relwidth=.200)
    b5 = Button(Canvas3,text = "Budgets",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsbudgets).place(relx=0.35, rely=0.48,relwidth=.200)
    b6 = Button(Canvas3,text = "Scenarios",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsscenarios).place(relx=0.35, rely=0.51,relwidth=.200)
    Label3 = Label(Canvas3,text='Inventory masters', background="Lightblue",foreground="#00254a",font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.35, rely=0.54,relwidth=.200)
    b7 = Button(Canvas3,text = "Stock Groups",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsstockgroups).place(relx=0.35, rely=0.57,relwidth=.200)
    b8 = Button(Canvas3,text = "Stock Items",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsstockitems).place(relx=0.35, rely=0.60,relwidth=.200)
    b9 = Button(Canvas3,text = "Stock Catogories",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsstockcategories).place(relx=0.35, rely=0.63,relwidth=.200)
    b10 = Button(Canvas3,text = "Units",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsunits).place(relx=0.35, rely=0.66,relwidth=.200)
    b11 = Button(Canvas3,text = "Godowns",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10'),command=chartofaccountsgodowns).place(relx=0.35, rely=0.69,relwidth=.200)
    b12 = Button(Canvas3,text = "Back",activeforeground = "black", activebackground = "#ffbe23",fg='black',bg='lightblue',borderwidth=0,font=('Arial 10')).place(relx=0.35, rely=0.72,relwidth=.200)

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


a=chartofaccountsgroups()
screen.mainloop()