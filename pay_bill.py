from tkinter import *
from tkinter import messagebox
import math, random
import os


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
            self.phone_no = StringVar()
            self.silver = StringVar()
            self.gold = StringVar()
            self.plat = StringVar()
            self.t1 = StringVar()
            self.t2 = StringVar()
            self.t3 = StringVar()
            self.t4 = StringVar()
            self.ticket_no = StringVar()
            self.search_bill = StringVar()

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
            F6.place(x=5,y=435,width = 990,height = 200)

            T1 = Label(F6, text = 'Total silver Amount',font = 'Times 12 bold',bg = bg_color,fg = 'White').grid(row=0,column=0,padx=20,pady=1,sticky='W')
            T1_entry = Entry(F6,textvariable = self.t1, width = 18, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=0, column=1, padx=10,pady=1)

            T2 = Label(F6, text = 'Total Gold Amount',font = 'Times 12 bold',bg = bg_color,fg = 'White').grid(row=1,column=0,padx=20,pady=1,sticky='W')
            T2_entry = Entry(F6, width = 18,textvariable = self.t2, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=1, column=1, padx=10,pady=1)

            T3 = Label(F6, text = 'Total Platinum Amount',font = 'Times 12 bold',bg = bg_color,fg = 'White').grid(row=2,column=0,padx=20,pady=1,sticky='W')
            T3_entry = Entry(F6, width = 18,textvariable = self.t3, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=2, column=1, padx=10,pady=1)

            
            T4 = Label(F6, text = 'Total tax.',font = 'arial 12 bold',bg = bg_color,fg = 'White').grid(row=3,column=0,padx=20,pady=1,sticky='W')
            T4_entry = Entry(F6, width = 18,textvariable = self.t4, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=3, column=1, padx=10,pady=1)

      
            T5_entry = Entry(F6, width = 18,textvariable = self.search_bill, font = 'arial 10 bold',bd =5, relief = SUNKEN).grid(row=4, column=1, padx=10,pady=1)


            btn_f = LabelFrame(self.bill,bd = 7, relief = GROOVE,bg = bg_color)
            btn_f.place(x = 5, y= 350, width = 990,height = 85)
            Total_btn = Button(btn_f, text = 'Total', font = 'Times 20 bold',bg = 'cadet blue', fg ='White',bd = 5,padx=15,width=11,
                                          activebackground = 'gold',command = self.total).grid(row=0,column =0,padx=5,pady=5)
            bill_btn = Button(btn_f, text = 'Generate Bill >>>', font = 'Times 20 bold',bg = 'cadet blue', fg ='White',bd = 5,padx=15,
                                          width=15,activebackground = 'gold',command = self.bill_area).grid(row=0,column =3,padx=5,pady=5)

            search_bill = Button(btn_f, text = 'Search Bill', font = 'Times 20 bold',bg = 'cadet blue', fg ='White',bd = 5,padx=15,
                                          width=10,activebackground = 'gold',command = self.find_bill).grid(row=0,column =2,padx=5,pady=5)                              
                                         
            clear_bill = Button(btn_f, text = 'Clear All', font = 'Times 20 bold',bg = 'cadet blue', fg ='White',bd = 5,padx=15,
                                          width=10,activebackground = 'gold',command = self.clear_all).grid(row=0,column =1,padx=5,pady=5)                             
            self.welcome_bill()

        def total(self):
            # self.num_silver = int(self.silver.get())
            if self.silver.get() == "":
                  self.t1.set('Rs.0.0')
                  self.silver_c = 0
                  self.sp = 0
                  self.total_t1 = 0
            else:
                  self.num_silver = int(self.silver.get())      
                  self.sp = self.num_silver*110
                  self.total_t1 = float(self.sp)
                  self.t1.set('Rs.'+str(self.total_t1))
                  self.silver_c = self.silver.get()

            if self.gold.get() == "":
                  self.t2.set('Rs.0.0')
                  self.gold_c = 0
                  self.gp = 0
                  self.total_t2 = 0
            else:
                  self.num_gold = int(self.gold.get())      
                  self.gp = self.num_gold*110
                  self.total_t2 = float(self.gp)
                  self.t2.set('Rs.'+str(self.total_t2))
                  self.gold_c = self.gold.get()
                  
            if self.plat.get() == "":
                  self.t3.set('Rs.0.0')
                  self.plat_c = 0
                  self.pp = 0
                  self.total_t3 = 0
            else:
                  self.num_plat = int(self.plat.get())      
                  self.pp = self.num_plat*110
                  self.total_t3 = float(self.pp)
                  self.t3.set('Rs.'+str(self.total_t3))            
                  self.plat_c = self.plat.get()
            # print(self.total_t1)      
            # self.gp = self.gold.get()*150
            # self.total_t2 = float(self.gp)
            # self.t2.set('Rs.'+str(self.total_t2))

            # self.pp = self.plat.get()*200
            # self.total_t3 = float(self.pp)
            # self.t3.set('Rs.'+str(self.total_t3))

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
            if self.silver.get()=="" and self.gold.get()=="" and self.plat.get() =="":
                  messagebox.showerror("Tickets","kindly enter your ticket counts")
                  return
            else:      
                  if self.silver.get() !='':
                        self.txtarea.insert(END, f'\nSilver tickets\t\t {self.silver_c}\tRs.{self.sp}')

                  if self.gold.get() !='':
                        self.txtarea.insert(END, f'\nGold tickets\t\t{self.gold_c}\tRs.{self.gp}')      

                  if self.plat.get() !='':
                        self.txtarea.insert(END, f'\nPlatinum tickets\t\t{self.plat_c}\tRs.{self.pp}')

            self.txtarea.insert(END, '\n--------------------------------------') 
            
            self.txtarea.insert(END, f'\nSeat nos :-\t{self.ticket_no.get()}')
            self.txtarea.insert(END, '\n--------------------------------------')
            self.txtarea.insert(END, f'\nTotal ticket price\t\t\t Rs.{self.ticket_price} ') 
            self.txtarea.insert(END, f'\nTotal tax\t\t\t + Rs.{self.total_tax} ')
            self.txtarea.insert(END, '\n\t\t\t---------')
            self.txtarea.insert(END, f'\nTotal Amount paid\t\t\t Rs.{self.total_amount_paid} ')
            self.txtarea.insert(END,"\n======================================")   
            self.txtarea.config(state = DISABLED)
            self.save_bill()

        def save_bill(self):
            op = messagebox.askyesno("Save bill","do you want to save the bill")
            if op>0:
                  self.bill_data = self.txtarea.get('1.0',END)
                  f1 = open("Bills/"+str(self.bill_no.get())+".txt","w")
                  f1.write(self.bill_data)
                  f1.close()
                  messagebox.showinfo("Saved","Bill no. {self.bill_no.get()} saved successfully")
            else:
                  return
                 

        def find_bill(self):
            present = "No"
            for i in os.listdir("Bills/"):
               if i.split('.')[0]==self.search_bill.get():              # [0] this stores the bill no and [1] is .txt
                  f1 = open(f"Bills/{i}","r")
                  self.txtarea.delete('1.0', END)
                  for d in f1:
                        self.txtarea.insert(END, d)
                  f1.close()
                  present = "Yes" 
            if present == "No":
                  messagebox.showerror("Error","Invalid Bill no.")           
               
 
        def clear_all(self):
            self.c_name.set("")
            self.phone_no.set("")
            self.silver.set("")
            self.gold.set("")
            self.plat.set("")
            self.t1.set("")
            self.t2.set("")
            self.t3.set("")
            self.t4.set("")
            self.ticket_no.set("")
            self.search_bill.set("")

            self.bill_no = StringVar()              
                  
if __name__ == '__main__':
      bill = Tk()
      obj = Bill_window(bill)
      bill.mainloop()






