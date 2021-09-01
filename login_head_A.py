from tkinter import *
from tkinter import messagebox
import io
# from PIL import Image, ImageTk
from urllib.request import urlopen
import os
import requests
from bs4 import BeautifulSoup
import math, random
from pay_bill import Bill_window

global searching
global creation


# Billing System
class Bill_window:
        def __init__(self, bill):
            self.bill = bill
            self.bill.title('Get Your Ticket')
            self.bill.geometry('1350x700+0+0')
            self.bill.state('zoomed')
            bg_color = '#074463'
            title = Label(self.bill, text= "Movie Ticket Billing System", bd = 12, relief = GROOVE,bg = bg_color,fg='white',font = 'Times 25 bold',pady=2)
            title.pack(fill = X)

            # =========================================== VARIABLES =====================================================
            self.c_name = StringVar()
            # c_name = username1.get()
            self.phone_no = StringVar()
            self.silver = IntVar()
            self.gold = IntVar()
            self.plat = IntVar()
            self.t1 = StringVar()
            self.t2 = StringVar()
            self.t3 = StringVar()
            self.t4 = StringVar()
            self.ticket_no = StringVar()

            self.bill_no = StringVar()
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))


            # ========================================= LABEL FRAMES 1 ==================================================
            F1 = LabelFrame(self.bill, text = "Customer Details", font = "Times 20 bold", fg = 'Gold',bg = bg_color)
            F1.place(x = 0, y = 100, relwidth = 1)

            name_label = Label(F1, text = 'Enter Name:', bg = bg_color,fg = 'white',font = 'Times 15 bold').grid(row=0, column=0,padx=20,pady=5)
            name_entry =Entry(F1, width =22,textvariable = self.c_name,font = 'arial 15 bold',bd =7, relief = SUNKEN).grid(row =0, column=1, padx=10,pady=5)

            contact_label = Label(F1, text = 'Contact no.:', bg = bg_color,fg = 'white',font = 'Times 15 bold').grid(row=0, column=2,padx=20,pady=5)
            contact_entry =Entry(F1, width =22,textvariable = self.phone_no, font = 'arial 15 bold',bd =7, relief = SUNKEN).grid(row =0, column=3, padx=10,pady=5)

            bill_label = Label(F1, text = 'Enter ticket no.:', bg = bg_color,fg = 'white',font = 'Times 15 bold').grid(row=0, column=4,padx=20,pady=5)
            bill_entry =Entry(F1, width =22,textvariable = self.ticket_no, font = 'arial 15 bold',bd =7, relief = SUNKEN).grid(row =0, column=5, padx=10,pady=5)

            # ===================================== SILVER TICKETS PURCHASED ==============================================
            F2 = LabelFrame(self.bill, text= 'Silver Tickets',bd=10,relief=GROOVE, font='Times 20 bold',fg='Gold',bg=bg_color)
            F2.place(x=5,y=200,width=315,height=150)

            silver_tickets = Label(F2, text = 'Total Silver tickets',font ='times 15 bold',bg =bg_color,fg='lightgreen').grid(row=0,column =0,padx=10,pady=10,sticky="W")
            silver_txt = Entry(F2,width=8,textvariable = self.silver,font= 'times 12 bold',bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
            

            # ===================================== GOLD TICKETS PURCHASED ==============================================
            F3 = LabelFrame(self.bill, text= 'Gold Tickets',bd=10,relief=GROOVE, font='Times 20 bold',fg='Gold',bg=bg_color)
            F3.place(x=325,y=200,width=315,height=150)

            gold_tickets = Label(F3, text = 'Total Gold tickets',font ='times 15 bold',bg =bg_color,fg='lightgreen').grid(row=0,column =0,padx=10,pady=10,sticky="W")
            self.gold_txt = Entry(F3,width=8,textvariable =self.gold, font= 'times 12 bold',bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            # ===================================== PLATINUM TICKETS PURCHASED ==============================================
            F4 = LabelFrame(self.bill, text= 'Platinum Tickets',bd=10,relief=GROOVE, font='Times 20 bold',fg='Gold',bg=bg_color)
            F4.place(x=645,y=200,width=338,height=150)

            plat_tickets = Label(F4, text = 'Total Plantinum tickets',font ='times 15 bold',bg =bg_color,fg='lightgreen').grid(row=0,column =0,padx=10,pady=10,sticky="W")
            plat_txt = Entry(F4,width=8,textvariable = self.plat,font= 'times 12 bold',bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


            # ===================================== BILL AREA ==============================================
            F5 = LabelFrame(self.bill,bd=10,relief=GROOVE)
            F5.place(x=1000,y=200,width=350,height=380)

            bill_title = Label(F5, text="Bill Area",font='Arial 15 bold',bd =7, relief=GROOVE).pack(fill=X)
            scroll_y = Scrollbar(F5, orient = VERTICAL)
            self.txtarea = Text(F5, yscrollcommand = scroll_y.set)
            scroll_y.pack(side = RIGHT, fill = Y)
            scroll_y.config(command = self.txtarea.yview)
            self.txtarea.pack(fill = BOTH, expand = 1)


            # ===================================== TOTAL AREA ==============================================
            F6 = LabelFrame(self.bill,text = "Total Bill",bd=10,relief=GROOVE, font='Times 20 bold',fg='Gold',bg=bg_color)
            F6.place(x=5,y=435,width = 990,height = 180)

            T1 = Label(F6, text = 'Total silver Amount',font = 'Times 12 bold',bg = bg_color,fg = 'White').grid(row=0,column=0,padx=20,pady=1,sticky='W')
            T1_entry = Entry(F6,textvariable = self.t1, width = 18, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=0, column=1, padx=10,pady=1)

            T2 = Label(F6, text = 'Total Gold Amount',font = 'Times 12 bold',bg = bg_color,fg = 'White').grid(row=1,column=0,padx=20,pady=1,sticky='W')
            T2_entry = Entry(F6, width = 18,textvariable = self.t2, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=1, column=1, padx=10,pady=1)

            T3 = Label(F6, text = 'Total Platinum Amount',font = 'Times 12 bold',bg = bg_color,fg = 'White').grid(row=2,column=0,padx=20,pady=1,sticky='W')
            T3_entry = Entry(F6, width = 18,textvariable = self.t3, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=2, column=1, padx=10,pady=1)

            
            T4 = Label(F6, text = 'Total tax.',font = 'arial 12 bold',bg = bg_color,fg = 'White').grid(row=3,column=0,padx=20,pady=1,sticky='W')
            T4_entry = Entry(F6, width = 18,textvariable = self.t4, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=3, column=1, padx=10,pady=1)

            btn_f = LabelFrame(self.bill,bd = 7, relief = GROOVE,bg = bg_color)
            btn_f.place(x = 5, y= 350, width = 575,height = 85)
            Total_btn = Button(btn_f, text = 'Total', font = 'Times 20 bold',bg = 'cadet blue', fg ='White',bd = 5,padx=15,width=11,
                                          activebackground = 'gold',command = self.total).grid(row=0,column =0,padx=5,pady=5)
            bill_btn = Button(btn_f, text = 'Generate Bill >>>>', font = 'Times 20 bold',bg = 'cadet blue', fg ='White',bd = 5,padx=15,
                                          width=17,activebackground = 'gold',command = self.bill_area).grid(row=0,column =1,padx=5,pady=5)
                                         
            self.welcome_bill()

        def total(self):
            self.sp = self.silver.get()*110
            self.total_t1 = float(self.sp)
            self.t1.set('Rs.'+str(self.total_t1))

            self.gp = self.gold.get()*150
            self.total_t2 = float(self.gp)
            self.t2.set('Rs.'+str(self.total_t2))

            self.pp = self.plat.get()*200
            self.total_t3 = float(self.pp)
            self.t3.set('Rs.'+str(self.total_t3))

            self.tax_silver = float(self.total_t1*0.05)
            self.tax_gold = float(self.total_t2*0.05)
            self.tax_plat = float(self.total_t3*0.05)
            self.total_tax= float(self.tax_silver+self.tax_gold+self.tax_plat)
            self.t4.set('Rs.'+str(self.total_tax))

            self.ticket_price = float(self.total_t1 + self.total_t2 + self.total_t3)
            
            self.total_amount_paid = float(self.ticket_price +self.total_tax)
            

        def welcome_bill(self):
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, 'Welcome to Movie ticket booking centre')
            self.txtarea.insert(END,"\n")
            self.txtarea.insert(END, f'\nBill no.:{self.bill_no.get()}')
            self.txtarea.insert(END, f'\nCustomer Name :{self.c_name.get()}')
            self.txtarea.insert(END, f'\nContact no. :{self.phone_no.get()}')
            self.txtarea.insert(END,"\n======================================")
            self.txtarea.insert(END,"\nCriteria\t\tQTY\tTotal")
            self.txtarea.insert(END,"\n======================================")

        def bill_area(self):
            self.welcome_bill()
            if self.c_name.get() == "" :
                  messagebox.showerror('Customer Details','Kindly enter the Customer name')
                  return
            if self.phone_no.get() == "":
                  messagebox.showerror('Customer Details','Kindly enter the phone no')
                  return      
            if self.ticket_no.get() == "":
                  messagebox.showerror('Customer Details','Kindly enter the Ticket nos.')
                  return
            if self.silver.get() !=0:
                  self.txtarea.insert(END, f'\nSilver tickets\t\t {self.silver.get()}\tRs.{self.sp}')

            if self.gold.get() !=0:
                  self.txtarea.insert(END, f'\nGold tickets\t\t{self.gold.get()}\tRs.{self.gp}')      

            if self.plat.get() !=0:
                  self.txtarea.insert(END, f'\nPlatinum tickets\t\t{self.plat.get()}\tRs.{self.pp}')

            self.txtarea.insert(END, '\n--------------------------------------') 
            
            self.txtarea.insert(END, f'\nSeat nos :-\t{self.ticket_no.get()}')
            self.txtarea.insert(END, '\n--------------------------------------')
            self.txtarea.insert(END, f'\nTotal ticket price\t\t\t Rs.{self.ticket_price} ') 
            self.txtarea.insert(END, f'\nTotal tax\t\t\t + Rs.{self.total_tax} ')
            self.txtarea.insert(END, '\n\t\t\t---------')
            self.txtarea.insert(END, f'\nTotal Amount paid\t\t\t Rs.{self.total_amount_paid} ')
            self.txtarea.insert(END,"\n======================================")   
            self.bill.mainloop()

            
def Calling_Bill_window():
        bill = Tk()
        obj = Bill_window(bill)
        bill.mainloop()

# Storage of real time checkbox selections

def mention(x,time):
    if time == 9:
        storebox = open('morning_schedule.txt','a+')
        storebox.write(x)
        storebox.write('\n')
        storebox.close()    

    elif time == 12:
        storebox = open('afternoon1_schedule.txt','a+')
        storebox.write(x)
        storebox.write('\n')
        storebox.close()

    elif time == 15:
        storebox = open('afternoon2_schedule.txt','a+')
        storebox.write(x)
        storebox.write('\n')
        storebox.close()

    elif time == 18:
        storebox = open('evening_schedule.txt','a+')
        storebox.write(x)
        storebox.write('\n')
        storebox.close()
    
    elif time == 21:
        storebox = open('night_schedule.txt','a+')
        storebox.write(x)
        storebox.write('\n')
        storebox.close()
    else:
        print(error)
            
#Structure creation for checkboxes window

def structure(time):
    
    global check_window
    check_window = Tk()
    check_window.geometry("200x300")
    check_window.title("Seat options ")
    check_window.configure(bg = "khaki2")
    check_window.state('zoomed')
    disp2.destroy()

    silver_label = Label(check_window,text = "SILVER>", font = "Times 30 bold", relief = "ridge", width=10,height =2, bd=15, justify = "center", bg="silver", fg="black", padx=20, pady=20)
    silver_label.place(x=50,y=70)

    gold_label = Label(check_window,text = "GOLD>", font = "Times 30 bold", relief = "ridge", width=10,height =2, bd=15, justify = "center", bg="gold", fg="black", padx=20, pady=20)
    gold_label.place(x=50,y=335)

    platinum_label = Label(check_window,text = "PLATINUM>", font = "Times 30 bold", relief = "ridge", width=10, height =2, bd=15, justify = "center", bg="ghost white", fg="black", padx=20, pady=20)
    platinum_label.place(x=50,y=600)

    sponsor_message = Message(check_window, text = "M\nA\nD\nS", font = "Times 50 bold", relief = "ridge", width=120, bd=15, justify = "center", fg="ghost white", bg="black", padx=20, pady=20)
    sponsor_message.place(x = 1400, y = 70)

    next_button = Button(check_window, text = "NEXT",font = "Times 20 bold",relief = "groove", height = 2, width = 5,bd = 15, justify = "center", pady = 20,padx = 20, bg = 'black',fg = "lavender blush", activebackground = "light yellow", command = Calling_Bill_window)
    next_button.place(x =1400 , y = 610)

    if time == 9:
        creation = open("morning_schedule.txt","a+")
    elif time ==12:
        creation2 = open("afternoon1_schedule.txt","a+")
    elif time == 15:
        creation3 = open("afternoon2_schedule.txt","a+")
    elif time == 18:
        creation3 = open("evening_schedule.txt","a+")
    elif time == 21:
        creation3 = open("night_schedule.txt","a+")

#creating the checkbox displays 

    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)


    data_repeated = searching.read().find("a1")
    if data_repeated == -1:
        
        
        chk = Checkbutton(check_window,text = "a1", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a1",time))
        chk.place(x=400,y=70)

    else:
        chk = Checkbutton(check_window,text = "a1", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk.place(x=400,y=70)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)
        
    data_repeated = searching.read().find("a2")
    if data_repeated == -1:
        

        chk1 = Checkbutton(check_window,text = "a2",bg = "navy", fg = "lavender blush", height=3, width = 3,command = lambda: mention("a2",time))
        chk1.place(x=500,y=70)

    else:
        chk1 = Checkbutton(check_window,text = "a2", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk1.place(x=500,y=70)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a3")
    if data_repeated == -1:
        
        
        chk2 = Checkbutton(check_window,text = "a3", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a3",time))
        chk2.place(x=600,y=70)

    else:
        chk2 = Checkbutton(check_window,text = "a3", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk2.place(x=600,y=70)

       
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a4")
    if data_repeated == -1:
        
        
        chk3 = Checkbutton(check_window,text = "a4", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a4",time))
        chk3.place(x=700,y=70)

    else:
        chk3 = Checkbutton(check_window,text = "a4", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk3.place(x=700,y=70)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a5")
    if data_repeated == -1:
        
        
        chk4 = Checkbutton(check_window,text = "a5", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a5",time))
        chk4.place(x=800,y=70)

    else:
        chk4 = Checkbutton(check_window,text = "a5", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk4.place(x=800,y=70)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a6")
    if data_repeated == -1:
        
        
        chk5 = Checkbutton(check_window,text = "a6", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a6",time))
        chk5.place(x=900,y=70)

    else:
        chk5 = Checkbutton(check_window,text = "a6", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk5.place(x=900,y=70)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a7")
    if data_repeated == -1:
        
        
        chk6 = Checkbutton(check_window,text = "a7", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a7",time))
        chk6.place(x=1000,y=70)

    else:
        chk6 = Checkbutton(check_window,text = "a7", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk6.place(x=1000,y=70)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a8")
    if data_repeated == -1:
        
        
        chk7 = Checkbutton(check_window,text = "a8", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a8",time))
        chk7.place(x=1100,y=70)

    else:
        chk7 = Checkbutton(check_window,text = "a8", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk7.place(x=1100,y=70)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("a9")
    if data_repeated == -1:
        
        
        chk8 = Checkbutton(check_window,text = "a9", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("a9",time))
        chk8.place(x=1200,y=70)

    else:
        chk8 = Checkbutton(check_window,text = "a9", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk8.place(x=1200,y=70)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("ax")
    if data_repeated == -1:
        
        
        chk9 = Checkbutton(check_window,text = "ax", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("ax",time))
        chk9.place(x=1300,y=70)

    else:
        chk9 = Checkbutton(check_window,text = "ax", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk9.place(x=1300,y=70)


    #row2
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b1")
    if data_repeated == -1:
        
        
        chk11 = Checkbutton(check_window,text = "b1", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b1",time))
        chk11.place(x=400,y=170)

    else:
        chk11 = Checkbutton(check_window,text = "b1", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk11.place(x=400,y=170)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b2")
    if data_repeated == -1:
        

        chk12 = Checkbutton(check_window,text = "b2",bg = "navy", fg = "lavender blush", height=3, width = 3,command = lambda: mention("b2",time))
        chk12.place(x=500,y=170)

    else:
        chk12 = Checkbutton(check_window,text = "b2", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk12.place(x=500,y=170)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b3")
    if data_repeated == -1:
        
        
        chk12 = Checkbutton(check_window,text = "b3", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b3",time))
        chk12.place(x=600,y=170)

    else:
        chk12 = Checkbutton(check_window,text = "b3", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk12.place(x=600,y=170)

       
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b4")
    if data_repeated == -1:
        
        
        chk13 = Checkbutton(check_window,text = "b4", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b4",time))
        chk13.place(x=700,y=170)

    else:
        chk13 = Checkbutton(check_window,text = "b4", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk13.place(x=700,y=170)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b5")
    if data_repeated == -1:
        
        
        chk14 = Checkbutton(check_window,text = "b5", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b5",time))
        chk14.place(x=800,y=170)

    else:
        chk14 = Checkbutton(check_window,text = "b5", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk14.place(x=800,y=170)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b6")
    if data_repeated == -1:
        
        
        chk15 = Checkbutton(check_window,text = "b6", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b6",time))
        chk15.place(x=900,y=170)

    else:
        chk15 = Checkbutton(check_window,text = "b6", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk15.place(x=900,y=170)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b7")
    if data_repeated == -1:
        
        
        chk16 = Checkbutton(check_window,text = "b7", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b7",time))
        chk16.place(x=1000,y=170)

    else:
        chk16 = Checkbutton(check_window,text = "b7", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk16.place(x=1000,y=170)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b8")
    if data_repeated == -1:
        
        
        chk17 = Checkbutton(check_window,text = "b8", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b8",time))
        chk17.place(x=1100,y=170)

    else:
        chk17 = Checkbutton(check_window,text = "b8", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk17.place(x=1100,y=170)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("b9")
    if data_repeated == -1:
        
        
        chk18 = Checkbutton(check_window,text = "b9", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("b9",time))
        chk18.place(x=1200,y=170)

    else:
        chk18 = Checkbutton(check_window,text = "b9", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk18.place(x=1200,y=170)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("bx")
    if data_repeated == -1:
                
        chk19 = Checkbutton(check_window,text = "bx", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("bx",time))
        chk19.place(x=1300,y=170)

    else:
        chk19 = Checkbutton(check_window,text = "bx", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk19.place(x=1300,y=170)


    #row 3

    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c1")
    if data_repeated == -1:
        
        
        chk20 = Checkbutton(check_window,text = "c1", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c1",time))
        chk20.place(x=400,y=335)

    else:
        chk20 = Checkbutton(check_window,text = "c1", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk20.place(x=400,y=335)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c2")
    if data_repeated == -1:
        

        chk21 = Checkbutton(check_window,text = "c2",bg = "navy", fg = "lavender blush", height=3, width = 3,command = lambda: mention("c2",time))
        chk21.place(x=500,y=335)

    else:
        chk21 = Checkbutton(check_window,text = "c2", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk21.place(x=500,y=335)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c3")
    if data_repeated == -1:
        
        
        chk22 = Checkbutton(check_window,text = "c3", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c3",time))
        chk22.place(x=600,y=335)

    else:
        chk22 = Checkbutton(check_window,text = "c3", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk22.place(x=600,y=335)

       
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c4")
    if data_repeated == -1:
        
        
        chk23 = Checkbutton(check_window,text = "c4", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c4",time))
        chk23.place(x=700,y=335)

    else:
        chk23 = Checkbutton(check_window,text = "c4", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk23.place(x=700,y=335)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c5")
    if data_repeated == -1:
        
        
        chk24 = Checkbutton(check_window,text = "c5", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c5",time))
        chk24.place(x=800,y=335)

    else:
        chk24 = Checkbutton(check_window,text = "c5", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk24.place(x=800,y=335)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c6")
    if data_repeated == -1:
        
        
        chk25 = Checkbutton(check_window,text = "c6", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c6",time))
        chk25.place(x=900,y=335)

    else:
        chk25 = Checkbutton(check_window,text = "c6", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk25.place(x=900,y=335)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c7")
    if data_repeated == -1:
        
        chk26 = Checkbutton(check_window,text = "c7", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c7",time))
        chk26.place(x=1000,y=335)

    else:
        chk26 = Checkbutton(check_window,text = "c7", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk26.place(x=1000,y=335)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c8")
    if data_repeated == -1:
        
        
        chk27 = Checkbutton(check_window,text = "c8", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c8",time))
        chk27.place(x=1100,y=335)

    else:
        chk27 = Checkbutton(check_window,text = "c8", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk27.place(x=1100,y=335)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("c9")
    if data_repeated == -1:
        
        
        chk28 = Checkbutton(check_window,text = "c9", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("c9",time))
        chk28.place(x=1200,y=335)

    else:
        chk28 = Checkbutton(check_window,text = "c9", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk28.place(x=1200,y=335)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("cx")
    if data_repeated == -1:
        
        
        chk29 = Checkbutton(check_window,text = "cx", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("cx",time))
        chk29.place(x=1300,y=335)

    else:
        chk29 = Checkbutton(check_window,text = "cx", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk29.place(x=1300,y=335)


    #row 4
        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d1")
    if data_repeated == -1:
        
        
        chk30 = Checkbutton(check_window,text = "d1", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d1",time))
        chk30.place(x=400,y=435)

    else:
        chk30 = Checkbutton(check_window,text = "d1", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk30.place(x=400,y=435)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d2")
    if data_repeated == -1:
        

        chk31 = Checkbutton(check_window,text = "d2",bg = "navy", fg = "lavender blush", height=3, width = 3,command = lambda: mention("d2",time))
        chk31.place(x=500,y=435)

    else:
        chk31 = Checkbutton(check_window,text = "d2", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk31.place(x=500,y=435)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d3")
    if data_repeated == -1:
        
        
        chk32 = Checkbutton(check_window,text = "d3", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d3",time))
        chk32.place(x=600,y=435)

    else:
        chk32 = Checkbutton(check_window,text = "d3", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk32.place(x=600,y=435)

       
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d4")
    if data_repeated == -1:
        
        
        chk33 = Checkbutton(check_window,text = "d4", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d4",time))
        chk33.place(x=700,y=435)

    else:
        chk33 = Checkbutton(check_window,text = "d4", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk33.place(x=700,y=435)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d5")
    if data_repeated == -1:
        
        
        chk34 = Checkbutton(check_window,text = "d5", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d5",time))
        chk34.place(x=800,y=435)

    else:
        chk34 = Checkbutton(check_window,text = "d5", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk34.place(x=800,y=435)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d6")
    if data_repeated == -1:
        
        chk35 = Checkbutton(check_window,text = "d6", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d6",time))
        chk35.place(x=900,y=435)

    else:
        chk35 = Checkbutton(check_window,text = "d6", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk35.place(x=900,y=435)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d7")
    if data_repeated == -1:
        
        chk36 = Checkbutton(check_window,text = "d7", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d7",time))
        chk36.place(x=1000,y=435)

    else:
        chk36 = Checkbutton(check_window,text = "d7", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk36.place(x=1000,y=435)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("d8")
    if data_repeated == -1:
        
        chk37 = Checkbutton(check_window,text = "d8", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d8",time))
        chk37.place(x=1100,y=435)

    else:
        chk37 = Checkbutton(check_window,text = "d8", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk37.place(x=1100,y=435)


    searching = open("morning_schedule.txt","r")
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    if data_repeated == -1:
        
        
        chk38 = Checkbutton(check_window,text = "d9", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("d9",time))
        chk38.place(x=1200,y=435)

    else:
        chk38 = Checkbutton(check_window,text = "d9", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk38.place(x=1200,y=435)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("dx")
    if data_repeated == -1:
        
        
        chk39 = Checkbutton(check_window,text = "dx", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("dx",time))
        chk39.place(x=1300,y=435)

    else:
        chk39 = Checkbutton(check_window,text = "dx", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk39.place(x=1300,y=435)

    #row 5

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e1")
    if data_repeated == -1:
        
        
        chk40 = Checkbutton(check_window,text = "e1", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e1",time))
        chk40.place(x=400,y=600)

    else:
        chk40 = Checkbutton(check_window,text = "e1", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk40.place(x=400,y=600)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e2")
    if data_repeated == -1:
        

        chk41 = Checkbutton(check_window,text = "e2",bg = "navy", fg = "lavender blush", height=3, width = 3,command = lambda: mention("e2",time))
        chk41.place(x=500,y=600)

    else:
        chk41 = Checkbutton(check_window,text = "e2", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk41.place(x=500,y=600)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e3")
    if data_repeated == -1:
        
        
        chk42 = Checkbutton(check_window,text = "e3", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e3",time))
        chk42.place(x=600,y=600)

    else:
        chk42 = Checkbutton(check_window,text = "e3", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk42.place(x=600,y=600)

       
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e4")
    if data_repeated == -1:
        
        
        chk43 = Checkbutton(check_window,text = "e4", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e4",time))
        chk43.place(x=700,y=600)

    else:
        chk43 = Checkbutton(check_window,text = "e4", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk43.place(x=700,y=600)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e5")
    if data_repeated == -1:
        
        
        chk44 = Checkbutton(check_window,text = "e5", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e5",time))
        chk44.place(x=800,y=600)

    else:
        chk44 = Checkbutton(check_window,text = "e5", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk44.place(x=800,y=600)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e6")
    if data_repeated == -1:
        
        
        chk45 = Checkbutton(check_window,text = "e6", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e6",time))
        chk45.place(x=900,y=600)

    else:
        chk45 = Checkbutton(check_window,text = "e6", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk45.place(x=900,y=600)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e7")
    if data_repeated == -1:
        
        
        chk46 = Checkbutton(check_window,text = "e7", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e7",time))
        chk46.place(x=1000,y=600)

    else:
        chk46 = Checkbutton(check_window,text = "e7", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk46.place(x=1000,y=600)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e8")
    if data_repeated == -1:
        
        
        chk47 = Checkbutton(check_window,text = "e8", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e8",time))
        chk47.place(x=1100,y=600)

    else:
        chk47 = Checkbutton(check_window,text = "e8", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk47.place(x=1100,y=600)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("e9")
    if data_repeated == -1:
        
        
        chk48 = Checkbutton(check_window,text = "e9", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("e9",time))
        chk48.place(x=1200,y=600)

    else:
        chk48 = Checkbutton(check_window,text = "e9", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk48.place(x=1200,y=600)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("ex")
    if data_repeated == -1:
        
        
        chk49 = Checkbutton(check_window,text = "ex", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("ex",time))
        chk49.place(x=1300,y=600)

    else:
        chk49 = Checkbutton(check_window,text = "ex", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk49.place(x=1300,y=600)

    #row 6    
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time == 12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f1")
    if data_repeated == -1:
        
        
        chk50 = Checkbutton(check_window,text = "f1", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f1",time))
        chk50.place(x=400,y=700)

    else:
        chk50 = Checkbutton(check_window,text = "f1", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk50.place(x=400,y=700)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f2")
    if data_repeated == -1:
        

        chk51 = Checkbutton(check_window,text = "f2",bg = "navy", fg = "lavender blush", height=3, width = 3,command = lambda: mention("f2",time))
        chk51.place(x=500,y=700)

    else:
        chk51 = Checkbutton(check_window,text = "f2", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk51.place(x=500,y=700)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f3")
    if data_repeated == -1:
        
        
        chk52 = Checkbutton(check_window,text = "f3", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f3",time))
        chk52.place(x=600,y=700)

    else:
        chk52 = Checkbutton(check_window,text = "f3", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk52.place(x=600,y=700)

       
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f4")
    if data_repeated == -1:
        
        
        chk53 = Checkbutton(check_window,text = "f4", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f4",time))
        chk53.place(x=700,y=700)

    else:
        chk53 = Checkbutton(check_window,text = "f4", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk53.place(x=700,y=700)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f5")
    if data_repeated == -1:
        
        
        chk54 = Checkbutton(check_window,text = "f5", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f5",time))
        chk54.place(x=800,y=700)

    else:
        chk54 = Checkbutton(check_window,text = "f5", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk54.place(x=800,y=700)

        
    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f6")
    if data_repeated == -1:
        
        
        chk55 = Checkbutton(check_window,text = "f6", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f6",time))
        chk55.place(x=900,y=700)

    else:
        chk55 = Checkbutton(check_window,text = "f6", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk55.place(x=900,y=700)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f7")
    if data_repeated == -1:
        
        
        chk56 = Checkbutton(check_window,text = "f7", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f7",time))
        chk56.place(x=1000,y=700)

    else:
        chk56 = Checkbutton(check_window,text = "f7", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk56.place(x=1000,y=700)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f8")
    if data_repeated == -1:
        
        
        chk57 = Checkbutton(check_window,text = "f8", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f8",time))
        chk57.place(x=1100,y=700)

    else:
        chk57 = Checkbutton(check_window,text = "f8", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk57.place(x=1100,y=700)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("f9")
    if data_repeated == -1:
        
        
        chk58 = Checkbutton(check_window,text = "f9", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("f9",time))
        chk58.place(x=1200,y=700)

    else:
        chk58 = Checkbutton(check_window,text = "f9", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk58.place(x=1200,y=700)


    if time == 9:
        searching = open("morning_schedule.txt","r")
    elif time ==12:
        searching = open("afternoon1_schedule.txt","r")
    elif time == 15:
        searching = open("afternoon2_schedule.txt","r")
    elif time == 18:
        searching = open("evening_schedule.txt","r")
    elif time == 21:
        searching = open("night_schedule.txt","r")
    else:
        print(Error)

    data_repeated = searching.read().find("fx")
    if data_repeated == -1:
        
        
        chk59 = Checkbutton(check_window,text = "fx", height=3,bg = "navy", fg = "lavender blush", width = 3,command = lambda: mention("fx",time))
        chk59.place(x=1300,y=700)

    else:
        chk59 = Checkbutton(check_window,text = "fx", height=3,bg = "black", fg = "ghost white", width = 3,state = "disabled")
        chk59.place(x=1300,y=700)

    check_window.mainloop()

# to display the time options for a user

def booking():
    
    global disp2
    disp2 = Tk()
    disp2.geometry("200x300")
    disp2.title("Time options ")
    disp2.configure(bg = "Orange")
    disp2.state('zoomed')

    
#Labels for show Times
    Morning_label = Label(disp2,text = "Click Here for Morning Show>", font = "Times 50 bold", relief = "ridge", width=25, bd=10, justify = "center", bg="Black", fg="White", padx=20, pady=20)
    Morning_label.place(x=50,y=50)
    Afternoon_label = Label(disp2,text = "Click Here for Afternoon Shows>", font = "Times 50 bold", relief = "ridge", width=25, bd=10, justify = "center", bg="Black", fg="White", padx=20, pady=20)
    Afternoon_label.place(x=50,y=250)
    Evening_label = Label(disp2,text = "Click Here for Evening Show>", font = "Times 50 bold", relief = "ridge", width=25, bd=10, justify = "center", bg="Black", fg="White", padx=20, pady=20)
    Evening_label.place(x=50,y=450)
    Night_label = Label(disp2,text = "Click Here for Night Show>", font = "Times 50 bold", relief = "ridge", width=25, bd=10, justify = "center", bg="Black", fg="White", padx=20, pady=20)
    Night_label.place(x=50,y=650)
    
#Buttons for show times
    Morning_button = Button(disp2, text = "Morning",font = "Times 20 bold",relief = "groove", height = 3, width = 15,justify = "center", pady = 5,padx = 5, bg = 'Black',fg = "Orange", activebackground = "light yellow", bd = 10, command = lambda: structure(9))
    Morning_button.place(x = 1230, y = 50)
    Afternoon_button1 = Button(disp2, text = "Afternoon(12:00)",font = "Times 20 bold",relief = "groove", height = 1, width = 15,justify = "center", pady = 5,padx = 5, bg = 'Black',fg = "Orange", activebackground = "light yellow", bd = 10, command = lambda: structure(12))
    Afternoon_button1.place(x = 1230, y = 225)
    Afternoon_button2 = Button(disp2, text = "Afternoon(15:00)",font = "Times 20 bold",relief = "groove", height = 1, width = 15,justify = "center", pady = 5,padx = 5, bg = 'Black',fg = "Orange", activebackground = "light yellow", bd = 10, command = lambda: structure(15))
    Afternoon_button2.place(x = 1230,y = 320)
    Evening_button = Button(disp2, text = "Evening",font = "Times 20 bold",relief = "groove", height = 3, width = 15,justify = "center", pady = 5,padx = 5, bg = 'Black',fg = "Orange", activebackground = "light yellow", bd = 10, command = lambda: structure(18))
    Evening_button.place(x = 1230, y = 450)
    Night_button = Button(disp2, text = "Night",font = "Times 20 bold",relief = "groove", height = 3, width = 15,justify = "center", pady = 5,padx = 5, bg = 'Black',fg = "Orange", activebackground = "light yellow",bd = 10, command = lambda: structure(21))
    Night_button.place(x = 1230, y = 650)
    disp2.mainloop()


# Displaying Movies from web through web scraping

def view_movies():
    disp = Tk()
    disp.geometry("200x300")
    disp.title("Movie options ")
    disp.configure(bg = "Orange")
    disp.state('zoomed')
        

    
    url1 = "http://media1.santabanta.com/full1/"
    # url2 = "Bollywood%20Movies/Kedarnath/kedarnath-0a.jpg"
    # pic_url = url1+url2
    # open the web page picture and read it into a memory stream
    # and convert to an image Tkinter can handle
    # my_page = urlopen(pic_url)
    # create an image file object
    # my_picture = io.BytesIO(my_page.read())
    # use PIL to open image formats like .jpg  .png  .gif  etc.
    # pil_img = Image.open(my_picture)
    # convert to an image Tkinter can use
    # tk_img = ImageTk.PhotoImage(pil_img)
    # put the image on a typical widget
    # movie_label1 = Label(disp,image=tk_img,width=750,height=750,font = "Times 20 bold",bd = 25, relief = "ridge",bg="Black",fg="White",padx=5,pady=5)
    # movie_label1.place(x = 50,y = 20)

    url = 'https://www.imdb.com/title/tt7027278/'
    access_url = requests.get(url)
    html_page = access_url.content
    soup = BeautifulSoup(html_page, 'html.parser')
    display = soup.find(text = "Storyline").findNext('span').string
    Labelx = Label(disp,text = "Movie Plot", font = "Times 40 bold", relief = "ridge", width=10, bd=10, justify = "center", bg="Black", fg="White", padx=20, pady=20)
    Labelx.place(x = 1020,y= 25)
    story_message = Message(disp, text = display, font = "Times 20 bold", relief = "ridge", width=500, bd=10, justify = "center", bg="Black", fg="White", padx=20, pady=20)
    story_message.place(x = 930, y = 170)
    intrested_button = Button(disp, text = "Interested? Book Ticket?",font = "Times 20 bold",relief = "groove", bd = 10, height = 2, width = 20,justify = "center", pady = 5,padx = 5, bg = 'Black',fg = "Orange", activebackground = "light yellow",command = booking)
    intrested_button.place(x = 10, y = 10)

    
    disp.mainloop()

    
def register():

    #get username and password to register
    username_info = username1.get()
    password_info = password1.get()
    contact_info = contact1.get()

    check = open("messi.txt","a+")     #for first time creation

    searching_contacts = open("messi.txt","r")
    data_repeated = searching_contacts.read().find(contact_info)

    if contact_info.isdigit():

        if len(contact_info) == 10:

            if data_repeated == -1:

                store = open('messi.txt','a+')
                store.write(f'{username_info}\n')
                store.write(f'{contact_info}\n')
                store.close()
                
                #for password storage
                file = open(username_info,"w")
                file.write(username_info + "\n")
                file.write(password_info)
                file.close()
                sign_up_window.destroy()
                view_movies()
                

            else:
                messagebox.showerror("ERROR","Please enter a new contact no.\nThis contact no. is already registered")
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                contact_entry.delete(0, END)
                
        else:
            messagebox.showerror("ERROR","Please enter valid 10 digits!!")
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            contact_entry.delete(0, END)
            
    
    else:
        messagebox.showerror("ERROR","Please enter digits!!")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        contact_entry.delete(0, END)

            
#sign_up_code
def sign_up():

    global sign_up_window
    global username1
    global password1
    global contact1
    global username_entry
    global password_entry
    global contact_entry

    root.destroy()
    sign_up_window = Tk()
    sign_up_window.geometry("500x700")
    sign_up_window.title("Sign_Up_Window")
    sign_up_window.configure(bg = "khaki2")
    sign_up_window.state('zoomed')
    

    #setting variables to store data
    username1 = StringVar()
    password1 = StringVar()
    contact1 = StringVar()
    
    Lab1 = Label(sign_up_window,text ="Please Enter Credentials here",font = "Times 20 bold",relief = "ridge",bd = 20, width=97,padx=5,pady=5,height=5,bg="dark slate gray",fg="White")
    Lab1.place(x=0,y=0)

    username_label = Label(sign_up_window,text="Enter Username",font = "Times 20 bold",relief = "ridge",width=20,height=2,bd = 10, bg="Black",fg="White",padx=5,pady=5)
    username_label.place(x=400,y=300)

    password_label = Label(sign_up_window,text="Enter password",width=20,height=2,bd = 10,font = "Times 20 bold",relief = "ridge",bg="Black",fg="White",padx=5,pady=5)
    password_label.place(x=400,y=400)

    contact_label = Label(sign_up_window,text="Enter contact number",width=20,height=2,bd = 10,font = "Times 20 bold",relief = "ridge",bg="Black",fg="White",padx=5,pady=5)
    contact_label.place(x=400,y=500)

    contact_entry = Entry(sign_up_window,fg="white",bg="Black",bd = 10,font = "Times 20 bold",relief = "ridge",textvariable = contact1)
    contact_entry.place(x=800,y=500,width=400,height=90)

    username_entry = Entry(sign_up_window,fg="white",bg="Black",bd = 10,font = "Times 20 bold",relief = "ridge",textvariable = username1)
    username_entry.place(x=800,y=300,width=400,height=90)

    password_entry = Entry(sign_up_window,fg="white",bg="Black",font = "Times 20 bold",bd = 10,relief = "ridge",textvariable = password1,show = "*")
    password_entry.place(x=800,y=400,width=400,height=90)

    sign_up_Button = Button(sign_up_window,text = "SIGN UP", bg = "Black", fg = "White",bd = 10,font = "Times 20 bold",relief = "ridge",height=2,width=20,pady=5,padx=5,activebackground = "yellow",command = register)
    sign_up_Button.place(x=600,y=690)


#defining login function
def login_verify():
    user_verify = verify_username.get()
    pass_verify = verify_password.get()

    entry1.delete(0, END)
    entry2.delete(0, END)

    list_of_files = os.listdir()    #returns list of all the files created to store the credentials

    if user_verify in list_of_files:
        file1 = open(user_verify,"r")
        verify = file1.read().splitlines()   #to verify the password we use splitlines method
        
        if pass_verify in verify:
            root.destroy()
            view_movies()
            
        else:
            messagebox.showerror("Error","Wrong Password")
    
    else:
        messagebox.showerror("Error","Invalid Username\n User does not exist")
    


def bill_window():
    class bills:
        def __init__(self, bill,name):
            self.bill_1 = bill
            self.bill_1.title('Get Your Ticket')
            self.bill_1.geometry('1350x700+0+0')
            self.bill_1.state('zoomed')
            self.name = name
            print(self.name)

            Employees("Shashi","Prajapati", 10)
            # buut = Button(self.bill, text = 'tiket', command = self.Bill_window(bill))
            # buut.pack(padx = 10, pady = 10)

    
    bill = Tk()
    obj = bills(bill, "Shashi")
    bill.mainloop() 


#first window Code    
def main_screen():

    global root
    global entry1
    global entry2
    
    root = Tk()
    root.geometry("500x700")
    root.title("Login or Sign Up here!")
    root.state('zoomed')
    
    global verify_username
    global verify_password
    global img1
    verify_username = StringVar()
    verify_password = StringVar()
    
    img1 = PhotoImage(file = "D:/Users/User/Python/login.png")
    Label_photo  = Label(root,image = img1)
    Label_photo.image = img1 #to keep a referance 
    Label_photo.place(x = 0, y = 0,relwidth=1,relheight=1)
    Label1  = Label(root,text = "Username", bg = "Black", fg = "White",bd = 10, font = "Times 15 bold",relief = "ridge",height=2,width=20,pady=5,padx=5)
    Label1.place(x=500,y=200)
    
    Label2  = Label(root,text = "Password", bg = "Black", fg = "White",bd = 10, font = "Times 15 bold",relief = "ridge",height=2,width=20,pady=5,padx=5)
    Label2.place(x=500,y=300)

    entry1 = Entry(root,bg = "Black",fg="white",font = "Times 15 bold",bd = 10, textvariable = verify_username)
    entry1.place(x=800,y=200,width=250,height=75)

    entry2 = Entry(root,bg = "Black",fg= "white",font = "Times 15 bold",bd = 10, textvariable = verify_password,show = "*")
    entry2.place(x=800,y=300,width=250,height=75)

    button1 = Button(root,text = "Log in",bg = "Black",width = 20,height = 2,bd = 10, padx = 5,pady = 5,fg = "White",font = "Times 15 bold",relief = "ridge",activebackground = "yellow",command = login_verify)
    button1.place(x=650,y=400)

    button2  = Button(root,text = "New user? sign up?", bg = "Black", fg = "White",height = 2,bd = 10, width = 20,pady=5,padx=5,font = "Times 15 bold",relief = "ridge",activebackground = "yellow",command = sign_up)
    button2.place(x=650,y=500)

    button_3 = Button(root, text = "Bill window", command = bill_window)
    button_3.place(x = 10, y = 10)

    root.mainloop()

main_screen()
