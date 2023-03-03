from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyComplianceSystem:
    def __init__(self,root):
        #initializes the object and sets up the initial values for various variables
        self.root=root
        self.root.title("Pharmacy Compliance System")
        self.root.geometry("1550x800+0+0")
        self.addmed_var.get()
        self.refmed_var.get()
        self.ref_var.get()
        self.comy_Nme.get()
        self.typ_Nme.get()
        self.med_Nme.get()
        self.lot_Var.get()
        self.issue_dt.get()
        self.exd_dt.get()
        self.uses.get()
        self.side_eff.get()
        self.warning.get()
        self.dosage.get()
        self.price.get()
        self.product.get()

        #Code for the title frame
        laltitle=Label(self.root, text="Pharmacy Compliance System",bd=15,relief=RIDGE,bg="green",fg="#FFCC00",font=('tekton pro',50,'bold'),padx=2,pady=4)
        laltitle.pack(side="top",fill=X)         
        img1=Image.open( 'pharmacy_store.png'  )
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=150,y=18)

        #code creates a GUI interface with two label frames (DataFrameLeft and DataFrameRight) placed inside a main frame (DataFrame)
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20,bg="#FFF5EE")
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="#FFCC00",bg="#FFF5EE", font=('Tekton Pro',20,'bold'))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Departent",fg="#FFCC00",bg="#FFF5EE",font=('Tekton Pro',20,'bold'))
        DataFrameRight.place(x=910,y=5,width=550,height=350)

        #button frame
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20,bg="#FFF5EE")
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        #creates five buttons (Addbuttoon, UpdButton, DelButton, ResetButton, and ExitButton) inside a button frame (ButtonFrame) in a GUI interface.
        Addbuttoon=Button(ButtonFrame,command=self.add_data,text=" Add ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=15)
        Addbuttoon.grid(row=0,column=0)

        UpdButton=Button(ButtonFrame,text=" Update ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=15)
        UpdButton.grid(row=0,column=1)

        DelButton=Button(ButtonFrame,text=" Delete ",command=self.cmd_delete,fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=15)
        DelButton.grid(row=0,column=2)

        ResetButton=Button(ButtonFrame,text=" Reset ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=15)
        ResetButton.grid(row=0,column=3)

        ExitButton=Button(ButtonFrame,text=" Exit ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=15)
        ExitButton.grid(row=0,column=4)

        SrchButton=Label(ButtonFrame,text=" Search by.. ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'))
        SrchButton.grid(row=0,column=5,sticky=W)    
        
        #search bar with a drop-down men
        combo_serarch=ttk.Combobox(ButtonFrame,width=20,font=('Tekton Pro',12,'bold'),state="readonly")# state prevents it for overwriting
        combo_serarch["values"]=("Reference","Medicine Name","Lot")
        combo_serarch.grid(row=0,column=6)    
        combo_serarch.current(0) 

        #entry field where users can enter search keywords to find data in the medicine information 
        self.Srchtxt_var=StringVar()
        Srchtxt=Entry(ButtonFrame,bd=3,relief=RIDGE ,textvariable=self.Srchtxt_var, width=12,font=('Tekton Pro',12,'bold'))
        Srchtxt.grid(row=0,column=7)    

        #two buttons, one for searching and the other for displaying all the data.
        Searchbtn=Button(ButtonFrame,text=" Search ",command=self.Srchtxt_var, fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=10)
        Searchbtn.grid(row=0,column=8)

        ShowAll=Button(ButtonFrame,command=self.fetch_data, text=" Show all ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=12)
        ShowAll.grid(row=0,column=9)

        #label named Ref_num in the left label frame (DataFrameLeft)
        Ref_num=Label(DataFrameLeft,text="Reference number",textvariable=self.refmed_var,bg="#FFF5EE", font=('Tekton Pro',12,'bold'))
        Ref_num.grid(row=0,column=0,sticky=W) 

        #Connect to a MySQL database and retrieve medicine names
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT medicine_name FROM nano")
        med=my_cursor.fetchall()
        row=my_cursor.fetchall()
        combo_ref=ttk.Combobox(DataFrameLeft,width=18,font=('Tekton Pro',12,'bold'),state="readonly")# state prevents it for overwriting
        combo_ref["values"]=row
        combo_ref.grid(row=0,column=1)    
        combo_ref.current(0)    

        #entry fields for company name, medicine type, lot number, issued date, expiration date, uses, side effects, precautions,price and dosage
        cmpy_name=Label(DataFrameLeft,text="Company name:",textvariable=self.comy_Nme,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=6)
        cmpy_name.grid(row=1,column=0,sticky=W) 
        cmpy_name=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        cmpy_name.grid(row=1,column=1)  

        med_type=Label(DataFrameLeft,text="Type of medicine:",textvariable=self.typ_Nme,bg="#FFF5EE", font=('Tekton Pro',12,'bold'))
        med_type.grid(row=2,column=0,sticky=W) 

        med_type=ttk.Combobox(DataFrameLeft,width=18,font=('Tekton Pro',12,'bold'),state="readonly")# state prevents it for overwriting
        med_type["values"]=("Tablet","Liquid","Capsules","Drops","Inhales","Injection")
        med_type.grid(row=2,column=1)    
        med_type.current(0) 

        Ref_num=Label(DataFrameLeft,text="Medicine Type:",textvariable=self.ref_var,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=6)
        Ref_num.grid(row=3,column=0,sticky=W) 

        combo_ref=ttk.Combobox(DataFrameLeft,width=18,font=('Tekton Pro',12,'bold'),state="readonly")# state prevents it for overwriting
        combo_ref["values"]=("Nice","Novel")
        combo_ref.grid(row=3,column=1)    
        combo_ref.current(0) 

        ltnum=Label(DataFrameLeft,text="Lot number:",textvariable=self.lot_Var,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=4)
        ltnum.grid(row=4,column=0,sticky=W) 
        ltnum=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        ltnum.grid(row=4,column=1)  

        issue_dt=Label(DataFrameLeft,text="Issued date",textvariable=self.issue_dt,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=4)
        issue_dt.grid(row=5,column=0,sticky=W) 
        issue_dt=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        issue_dt.grid(row=5,column=1)

        exp_dt=Label(DataFrameLeft,text="Exp date:",textvariable=self.exd_dt,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=4)
        exp_dt.grid(row=6,column=0,sticky=W) 
        exp_dt=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        exp_dt.grid(row=6,column=1)

        uses=Label(DataFrameLeft,text="Uses:",textvariable=self.uses,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=4)
        uses.grid(row=7,column=0,sticky=W) 
        uses=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        uses.grid(row=7,column=1)
        
        side_eff=Label(DataFrameLeft,text="Side Effect:",textvariable=self.side_eff,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=2,pady=4)
        side_eff.grid(row=8,column=0,sticky=W) 
        side_eff=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        side_eff.grid(row=8,column=1)

        preca=Label(DataFrameLeft,text="Precautions:",textvariable=self.warning,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=20,pady=6)
        preca.grid(row=0,column=2,sticky=W) 
        preca=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        preca.grid(row=0,column=3)

        dos=Label(DataFrameLeft,text="Dosage:",textvariable=self.dosage,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=20,pady=4)
        dos.grid(row=1,column=2,sticky=W) 
        dos=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        dos.grid(row=1,column=3)

        price=Label(DataFrameLeft,text="Price:",textvariable=self.price,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=20,pady=4)
        price.grid(row=2,column=2,sticky=W) 
        price=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        price.grid(row=2,column=3)

        prod_qt=Label(DataFrameLeft,text="Products QT:",textvariable=self.product,bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=20,pady=4)
        prod_qt.grid(row=3,column=2,sticky=W) 
        prod_qt=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        prod_qt.grid(row=3,column=3)

        #adding images to the interface
        stay_home=Label(DataFrameLeft,text="Stay Home Stay Safe:",bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=20,pady=6,fg="black")
        stay_home.place(x=475,y=135)

        img2=Image.open( 'img1.jpg'  )
        img2=img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=410,y=340)

        img3=Image.open( 'img2.jpg'  )
        img3=img3.resize((150,135),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=585,y=340)

        img4=Image.open( 'img3.jpg'  )
        img4=img4.resize((150,135),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=760,y=340)

        #A label frame on the right side of the main frame for adding medicine details
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Departent",fg="#FFCC00",bg="#FFF5EE",font=('Tekton Pro',20,'bold'))
        DataFrameRight.place(x=910,y=5,width=550,height=350)

        img5=Image.open( 'img5.jpg'  )
        img5=img5.resize((150,135),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1305,y=180)

        #A label and entry widget for "Reference No." ,"Medicine Name" and assign a variable to the entry
        ref_num_lb=Label(DataFrameRight,text="Reference No.:",bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=5,pady=4)
        ref_num_lb.place(x=0,y=80)
        ref_num_lb=Entry(DataFrameRight,textvariable=self.refmed_var, bd=3,relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        ref_num_lb.place(x=135,y=80)

        med_name=Label(DataFrameRight,text="Medicine Name:",bg="#FFF5EE", font=('Tekton Pro',12,'bold'),padx=5,pady=4)
        med_name.place(x=0,y=110)
        med_name=Entry(DataFrameRight,textvariable=self.addmed_var, bd=3, relief=RIDGE,width=20,font=('Tekton Pro',12,'bold'))
        med_name.place(x=135,y=110)

        #A side frame with a scrollbar for displaying medicine details using a Treeview widget.
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=150)

        scroll_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","medname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.medicine_table.xview)
        scroll_y.config(command=self.medicine_table.yview)

        #Configure the Treeview widget to show only the column headings
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<buttonRelesase-1>",self.med_cursor)

        #a frame with buttons for adding, updating, deleting, and clearing medicine data
        frame_down=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="#FFCC00")
        frame_down.place(x=330,y=150,width=135,height=147)

        Add_med_buttoon=Button(frame_down,text=" Add ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=11,padx=5,pady=2)
        Add_med_buttoon.grid(row=0,column=0)

        Add_updt_buttoon=Button(frame_down,command=self.upd_Med,text=" Update ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=11,padx=5,pady=2)
        Add_updt_buttoon.grid(row=1,column=0)

        Add_del_buttoon=Button(frame_down,command=self.dellMed,text=" Delete ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=11,padx=5,pady=2)
        Add_del_buttoon.grid(row=2,column=0)

        Add_clr_buttoon=Button(frame_down,command=self.clr_Med,text=" Clear ",fg="#FFCC00",bg="green", font=('Tekton Pro',12,'bold'),width=11,padx=5,pady=2)
        Add_clr_buttoon.grid(row=3,column=0)

        #a bottom frame with a horizontal and vertical scrollbar and a Treeview widget for displaying pharmacy data, with scrolling functionality.
        frame_table=Frame(self.root,bd=15,relief=RIDGE,bg="#FFF5EE",padx=20)
        frame_table.place(x=0,y=585,width=1530,height=200)

        scroll_frame_x=ttk.Scrollbar(frame_table,orient=HORIZONTAL)
        scroll_frame_x.pack(side=BOTTOM,fill=X)
        scroll_frame_y=ttk.Scrollbar(frame_table,orient=VERTICAL)
        scroll_frame_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_tb=ttk.Treeview(frame_table,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt"),xscrollcommand=scroll_frame_x.set,yscrollcommand=scroll_frame_y.set)

        scroll_frame_x.pack(side=BOTTOM,fill=X)
        scroll_frame_y.pack(side=RIGHT,fill=Y)
        scroll_frame_x.config(command=self.pharmacy_tb.xview)
        scroll_frame_y.config(command=self.pharmacy_tb.yview)

        #treeview widget with columns and headings, sets column widths, fetches data from the database
        self.pharmacy_tb["show"]="headings"
        self.pharmacy_tb.heading("reg",text="Reference num")
        self.pharmacy_tb.heading("companyname",text="Company Name")
        self.pharmacy_tb.heading("type",text="Type of medicine")
        self.pharmacy_tb.heading("tabletname",text="Tablet name")
        self.pharmacy_tb.heading("lotno",text="Lot num")
        self.pharmacy_tb.heading("issuedate",text="Issue Date")
        self.pharmacy_tb.heading("expdate",text="Expiry Date")
        self.pharmacy_tb.heading("uses",text="Uses")
        self.pharmacy_tb.heading("sideeffect",text="Side Effect ")
        self.pharmacy_tb.heading("warning",text="Precautions")
        self.pharmacy_tb.heading("dosage",text="Dosage")
        self.pharmacy_tb.heading("price",text="Price")
        self.pharmacy_tb.heading("productqt",text="Product QT")
        self.pharmacy_tb.pack(fill=BOTH,expand=1)

        self.pharmacy_tb.column("reg",width=100)
        self.pharmacy_tb.column("companyname",width=100)
        self.pharmacy_tb.column("type",width=100)
        self.pharmacy_tb.column("tabletname",width=100)
        self.pharmacy_tb.column("lotno",width=100)
        self.pharmacy_tb.column("issuedate",width=100)
        self.pharmacy_tb.column("expdate",width=100)
        self.pharmacy_tb.column("uses",width=100)
        self.pharmacy_tb.column("sideeffect",width=100)
        self.pharmacy_tb.column("warning",width=100)
        self.pharmacy_tb.column("dosage",width=100)
        self.pharmacy_tb.column("price",width=100)
        self.pharmacy_tb.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_tb.bind("<ButtonRelease-1>",self.get_cursor)
 
    #first function "AddMed" inserts medicine data into the database and updates the medicine table. It also displays a success message box.
    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO nano(Ref,MedName) VALUES(%s, %s)",(
            self.refmed_var.get(),
            self.addmed_var.get(), ))
        conn.commit()
        self.fetch_dataMed()
        self.med_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine added")
    
    #The second function "fetch_dataMed" fetches medicine data from the database and populates the medicine table with the data.
    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from nano")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #med_cursor: retrieves data from selected row in medicine_table and displays it in entry fields.
    def med_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.added_var.set(row[1])
    
    #upd_Med: updates the medicine name in the database with the new value entered in the entry field. Displays a success message upon completion.
    def upd_Med(self):
        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("error","all data is required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE nano SET MedName=%s WHERE Ref=%s",(
                self.addmed_var.get(),
                self.refmed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Medicine data is updated")
            
    #dellMed(): deletes a medicine record from the database based on the reference number.
    def dellMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        sql="DELETE FROM nano WHERE Ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()

    #clr_Med(): clears the input fields for adding/editing medicine.
    def clr_Med(self):
        self.refmed_var.set("blank")
        self.addmed_var.set("")

    #add_data: Adds data to the Pharmacy table in the database.
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_Var.get()=="":
            messagebox.showerror("ERROR")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO nano VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)",(
            self.ref_var.get(),
            self.comy_Nme.get(),
            self.typ_Nme.get(),
            self.med_Nme.get(),
            self.lot_Var.get(),
            self.issue_dt.get(),
            self.exd_dt.get(),
            self.uses.get(),
            self.side_eff.get(),
            self.warning.get(),
            self.dosage.get(),
            self.price.get(),
            self.product.get(),  ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("SUCCESS","Data is inserted")
    
    #get_data: Retrieves data from the Pharmacy table and populates the pharmacy_tb tkinter treeview widget.
    def get_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT + FROM nano")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_tb.delete(*self.pharmacy_tb.get_children())
            for i in row:

                self.pharmacy_tb.insert("END" ,values=i)
            conn.commit()
        conn.close()

    #get_cursor: Retrieve the values of a selected row in the medicine_table and set them to respective entry widgets.
    def get_cursor(self,ev=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0])
        self.comy_Nme.set(row[1])
        self.typ_Nme.set(row[2])
        self.med_Nme.set(row[3])
        self.lot_Var.set(row[4])
        self.issue_dt.set(row[5])
        self.exd_dt.set(row[6])
        self.uses.set(row[7])
        self.side_eff.set(row[8])
        self.warning.set(row[9])
        self.dosage.set(row[10])
        self.price.set(row[11])
        self.product.set(row[12])

    #upd: Update the database with the new values from the entry widgets.
    def upd(self):
        if self.ref_var.get()=="" or self.lot_Var.get()=="":
            messagebox.showerror("error","all data is required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE pharmay SET cmpName=%s,lot=%s,issuedate=%s,uses=%s,Type=%s,sideEffect=%s,expdate=%s,warning=%s,price=%s,product=%s where Ref=%s",(
            self.ref_var.get(),
            self.comy_Nme.get(),
            self.typ_Nme.get(),
            self.med_Nme.get(),
            self.lot_Var.get(),
            self.issue_dt.get(),
            self.exd_dt.get(),
            self.uses.get(),
            self.side_eff.get(),
            self.warning.get(),
            self.dosage.get(),
            self.price.get(),
            self.product.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Medicine data is updated")

    #cmd_delete: Delete the row with the selected reference value from the database and update the treeview widget.
    def cmd_delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        sql="DELETE FROM nano WHERE Ref=%s"
        val=(self.ref_Var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Deleted","Data is deleted")

    #cmd_reset: resets all input fields to empty string
    def cmd_reset(self):
         
        self.comy_Nme.set(""),
        self.lot_Var.set(""),
        self.issue_dt.set(""),
        self.exd_dt.set(""),
        self.uses.set(""),
        self.side_eff.set(""),
        self.warning.set(""),
        self.dosage.set(""),
        self.price.set(""),
        self.product.set(""),

    #cmd_search: searches for data in the database based on the search term entered by the user and displays it in the table view
    def cmd_search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql#python@22",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM nano WHERE "+ str(self.search_var.get())+"LIKE"+str(self.Srchtxt_var.get())+"%")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_tb.delete(*self.pharmacy_tb.get_children())
            for i in rows:
                self.pharmacy_tb.insert("",END,values=i)
            conn.commit()
        conn.close

#main block of code that creates the root window and initializes the PharmacyComplianceSystem object
if __name__ == "__main__":
    root=Tk()
    obj=PharmacyComplianceSystem(root)
    root.mainloop()