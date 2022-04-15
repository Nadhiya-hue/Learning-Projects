from sqlite3 import connect
from tkinter import *
from tkinter import ttk
from webbrowser import BackgroundBrowser
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x790+0+0")
        self.root.title("CRIMINAL MANAGEMENT SYSTEM")

        # Variables.
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()
        self.var_criminal_name= StringVar()

        # Label the Title.
        lbl_title = Label(self.root,text = "CRIMINAL MANAGEMENT SOFTWARE",font = ('Times new roman',40,'bold'),bg='black',fg='violet')
        lbl_title.place(x=0,y=0,width=1400,height=70)

        # Image
        img_logo  = Image.open('images/logo.jpg')
        img_logo = img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        #Image_Label
        self.logo = Label(self.root,image = self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=60)

        # Image Frame.
        img_frame = Frame(self.root,border=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1500,height=150)

        # Image 1
        img_1  = Image.open('images/police_1.jpg')
        img_1 = img_1.resize((520,150),Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img_1)
        #Image1_Label
        self.img1 = Label(img_frame,image = self.photo_img1)
        self.img1.place(x=0,y=0,width=520,height=150)

        #Image 2
        img_2 = Image.open('images/police_2.jpg')
        img_2 = img_2.resize((520,150),Image.ANTIALIAS)
        self.photo_img2 = ImageTk.PhotoImage(img_2)
        #Image2_Label.
        self.img2 = Label(img_frame,image = self.photo_img2)
        self.img2.place(x=520,y=0,width=520,height=150)

        #Image 3
        img_3 = Image.open('images/police_3.jpg')
        img_3 = img_3.resize((500,150),Image.ANTIALIAS)
        self.photo_img3 = ImageTk.PhotoImage(img_3)
        #Image3_Label.
        self.img3 = Label(img_frame,image = self.photo_img3)
        self.img3.place(x=1040,y=0,width=500,height=150)

        #Main Frame.
        main_frame = Frame(self.root,border=2,relief=RIDGE,bg='grey')
        main_frame.place(x=10,y=210,width=1345,height=490)

        #Upper Frame.
        upper_frame = LabelFrame(main_frame,border=2,relief=RIDGE,text = "Criminal Information",font = ('Times new roman',11,'bold'),fg='Black',bg='Violet')
        upper_frame.place(x=5,y=10,width=1330,height=260)

        #Labels Entry.

        #1.CASE ID.
        case_id = Label(upper_frame,text = "CASE ID : ",font = ("Arial Black",10,'bold'),bg = 'violet')
        case_id.grid(row=0,column=0,padx=2,sticky=W) #w=west
        #Case Entry.
        case_entry = ttk.Entry(upper_frame,textvariable=self.var_case_id,width=20,font = ("Arial Black",10,'bold'))
        case_entry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal Number.
        criminal_no = Label(upper_frame,text = "CRIMINAL NO : ",font = ("Arial Black",10,'bold'),bg = 'violet')
        criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        #Criminal Number Entry.
        criminal_entry = ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=20,font = ("Arial Black",10,'bold'))
        criminal_entry.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #Crime Type.
        crime_type = Label(upper_frame,text = "CRIME TYPE : ",font = ("Arial Black",10,'bold'),bg = 'violet')
        crime_type.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        crime_entry = ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=20,font = ("Arial Black",10,'bold'))
        crime_entry.grid(row=0,column=5,padx=2,pady=7,sticky=W)

        #Criminal Name.
        criminal_name = Label(upper_frame,text = "CRIMINAL NAME : ",font = ("Arial Black",10,'bold'),bg = 'violet')
        criminal_name.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        criminal_name_entry = ttk.Entry(upper_frame,textvariable=self.var_criminal_name,width=20,font = ("Arial Black",10,'bold'))
        criminal_name_entry.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #Nick Name.
        Nickname = Label(upper_frame,text = "NICK NAME : ",font = ("Arial Black",10,'bold'),bg = 'violet')
        Nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        Nickname_entry = ttk.Entry(upper_frame,textvariable=self.var_nickname,width=20,font = ("Arial Black",10,'bold'))
        Nickname_entry.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        #Father Name.
        fathername = Label(upper_frame,text = "FATHER NAME :",font = ("Arial Black",10,'bold'),bg = 'violet')
        fathername.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        fathername_entry = ttk.Entry(upper_frame,textvariable=self.var_father_name,width=20,font = ("Arial Black",10,'bold'))
        fathername_entry.grid(row=1,column=5,padx=2,pady=7,sticky=W)

        #Arrest Date.
        Arrest_date = Label(upper_frame,text = "ARREST DATE :",font = ("Arial Black",10,'bold'),bg = 'violet')
        Arrest_date.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        Arrest_date_entry = ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=20,font = ("Arial Black",10,'bold'))
        Arrest_date_entry.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #Date of Crime.
        date_of_crime = Label(upper_frame,text = "DATE OF CRIME :",font = ("Arial Black",10,'bold'),bg = 'violet')
        date_of_crime.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        date_crime_entry = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=20,font = ("Arial Black",10,'bold'))
        date_crime_entry.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #Address.
        address = Label(upper_frame,text = "ADDRESS :",font = ("Arial Black",10,'bold'),bg = 'violet')
        address.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        address_entry = ttk.Entry(upper_frame,textvariable=self.var_address,width=20,font = ("Arial Black",10,'bold'))
        address_entry.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        #Age.
        age = Label(upper_frame,text = "AGE :",font = ("Arial Black",10,'bold'),bg = 'violet')
        age.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        age_entry = ttk.Entry(upper_frame,textvariable=self.var_age,width=20,font = ("Arial Black",10,'bold'))
        age_entry.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        #Occpation.
        occupation = Label(upper_frame,text = "OCCUPATION :",font = ("Arial Black",10,'bold'),bg = 'violet')
        occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        occupation_entry = ttk.Entry(upper_frame,textvariable=self.var_occupation,width=20,font = ("Arial Black",10,'bold'))
        occupation_entry.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        #Birth Mark.
        Birth_mark = Label(upper_frame,text = "BIRTH MARK :",font = ("Arial Black",10,'bold'),bg = 'violet')
        Birth_mark.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        Birth_mark_entry = ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=20,font = ("Arial Black",10,'bold'))
        Birth_mark_entry.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #Gender.
        gender = Label(upper_frame,text = "GENDER :",font = ("Arial Black",10,'bold'),bg = 'violet')
        gender.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        #Radio Button Gender.
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='yellow')
        radio_frame_gender.place(x=770,y=80,width=190,height=30)

        male = Radiobutton(radio_frame_gender,variable=self.var_gender,text="Male",value='Male',font=("Arial Black",8,'bold'),bg='yellow')
        male.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        self.var_gender.set('male')

        female = Radiobutton(radio_frame_gender,variable=self.var_gender,text="Female",value='Female',font=("Arial Black",8,'bold'),bg='yellow')
        female.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        self.var_gender.set('female')

        #Radio Button Wanted.
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='yellow')
        radio_frame_wanted.place(x=770,y=120,width=190,height=30)

        #Wanted.
        wanted = Label(upper_frame,text = "WANTED :",font = ("Arial Black",10,'bold'),bg = 'violet')
        wanted.grid(row=3,column=4,padx=2,pady=7,sticky=W)
        
        yes = Radiobutton(radio_frame_wanted,variable=self.var_wanted,text="Yes",value='Yes',font=("Arial Black",8,'bold'),bg='yellow')
        yes.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        self.var_wanted.set('yes')

        No = Radiobutton(radio_frame_wanted,variable=self.var_wanted,text="No",value='No',font=("Arial Black",8,'bold'),bg='yellow')
        No.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        self.var_wanted.set('No')

        #Buttons frame.
        buttons_frame=Frame(upper_frame,border=2,relief=RIDGE,bg='violet')
        buttons_frame.place(x=5,y=190,width=645,height=40)

        #Add Button.
        btn_add=Button(buttons_frame,command=self.add_data,text="Save Record",font=("Arial Black",9,'bold'),width=18,bg="blue",fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #Update Button.
        btn_update=Button(buttons_frame,text="Update",command=self.update_data,font=("Arial Black",9,'bold'),width=18,bg="blue",fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        #Delete Button.
        btn_delete=Button(buttons_frame,text="Delete",command=self.delete_data,font=("Arial Black",9,'bold'),width=18,bg="blue",fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
        #Clear Button.
        btn_clear=Button(buttons_frame,text="Clear",command=self.clear_data,font=("Arial Black",9,'bold'),width=18,bg="blue",fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #Image crime.
        img_crime = Image.open('images/criminal management.jpg')
        img_crime = img_crime.resize((480,290),Image.ANTIALIAS)
        self.photo_crime = ImageTk.PhotoImage(img_crime)
        #Image_Crime.
        self.img_crime = Label(upper_frame,image = self.photo_crime)
        self.img_crime.place(x=980,y=0,width=450,height=230)
        
        #Down Frame.
        down_frame = LabelFrame(main_frame,border=2,relief=RIDGE,text = "Criminal Information Table",font = ('Times new roman',11,'bold'),fg='Green',bg='orange')
        down_frame.place(x=5,y=270,width=1330,height=210)

        #Search Frame.
        search_frame = LabelFrame(down_frame,border=2,relief=RIDGE,text = "Search Criminal Record",font = ('Times new roman',11,'bold'),fg='Green',bg='yellow')
        search_frame.place(x=0,y=0,width=1325,height=50)

        #Search By label.
        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=2)

        #Combo Box.
        style=ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",fieldblackground="violet",background="grey")
        #Combo Box Variable and Search Box Variable.
        self.var_com_search=StringVar()
        self.var_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",10,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        style.configure("TEntry",fieldbackground="yellow",background="grey")
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=18,font = ("Arial",10,'bold'))
        search_entry.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        #Search Button.
        btn_search=Button(search_frame,text="Search",command=self.search_data,font=("Arial",8,'bold'),width=14,bg="blue",fg='white')
        btn_search.grid(row=0,column=3,padx=5,pady=5)

        #Show All Button.
        btn_clear=Button(search_frame,text="Show All",command=self.fetch_data,font=("Arial",8,'bold'),width=14,bg="blue",fg='white')
        btn_clear.grid(row=0,column=4,padx=5,pady=5)

        crime_agency = Label(search_frame,text = "CRIME AGENCY",font = ('arial',20,'bold'),fg='crimson',bg='yellow')
        crime_agency.grid(row=0,column=6,padx=20,pady=0)

        #Table_Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE,bg='orange')
        table_frame.place(x=0,y=50,width=1325,height=125)

        #Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseID')
        self.criminal_table.heading('2',text='CriminalNo')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Arrest Date')
        self.criminal_table.heading('5',text='CrimeOfDate')
        self.criminal_table.heading('6',text='Address')
        self.criminal_table.heading('7',text='Age')
        self.criminal_table.heading('8',text='Occupation')
        self.criminal_table.heading('9',text='Birth Mark')
        self.criminal_table.heading('10',text='Crime Type')
        self.criminal_table.heading('11',text='Father Name')
        self.criminal_table.heading('12',text='Gender')
        self.criminal_table.heading('13',text='Wanted')
        self.criminal_table.heading('14',text='NickName')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)
        #Packing the Table.
        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #Add  Funtion.
    def add_data(self):
            if self.var_case_id.get()=="":
                messagebox.showerror('Error','All Feilds are Required')
            else:
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='crime_management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_case_id.get(),
                                                                                                                self.var_criminal_no.get(),
                                                                                                                self.var_criminal_name.get(),
                                                                                                                self.var_arrest_date.get(),
                                                                                                                self.var_date_of_crime.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_occupation.get(),
                                                                                                                self.var_birthMark.get(),
                                                                                                                self.var_crime_type.get(),
                                                                                                                self.var_father_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_wanted.get(),
                                                                                                                self.var_nickname.get()

                                                                                                                ))      
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo('Success','Criminal Record has been Added Successfully')
                except Exception as es:
                    messagebox.showerror('Error',f'Due to {str(es)}')
    
    # Fetch Data Function for Fetching the all column data from mysql database.
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='crime_management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from criminal")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()
    
    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_criminal_name.set(data[2])
        self.var_arrest_date.set(data[3])
        self.var_date_of_crime.set(data[4])
        self.var_address.set(data[5])
        self.var_age.set(data[6])
        self.var_occupation.set(data[7])
        self.var_birthMark.set(data[8])
        self.var_crime_type.set(data[9])
        self.var_father_name.set(data[10])
        self.var_gender.set(data[11])
        self.var_wanted.set(data[12])
        self.var_nickname.set(data[13])

    # Update Function.
    def update_data(self):
        if self.var_case_id.get()=="":
                messagebox.showerror('Error','All Feilds are Required')
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this criminal record")
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='crime_management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s,Nick_name=%s where Case_id=%s',( 
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                            self.var_criminal_no.get(),
                                                                                                                                                                                                                                                            self.var_criminal_name.get(),
                                                                                                                                                                                                                                                            self.var_arrest_date.get(),
                                                                                                                                                                                                                                                            self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                                                            self.var_age.get(),
                                                                                                                                                                                                                                                            self.var_occupation.get(),
                                                                                                                                                                                                                                                            self.var_birthMark.get(),
                                                                                                                                                                                                                                                            self.var_crime_type.get(),
                                                                                                                                                                                                                                                            self.var_father_name.get(),
                                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                                            self.var_wanted.get(),
                                                                                                                                                                                                                                                            self.var_nickname.get(),
                                                                                                                                                                                                                                                            self.var_case_id.get()
                                                                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully Updated')

            except Exception as es:
                    messagebox.showerror('Error',f'Due to {str(es)}')

    #Delete Data.
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Feilds are Required')
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure delete this criminal record")
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='crime_management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully Deleted')
            except Exception as es:
                    messagebox.showerror('Error',f'Due to {str(es)}')
    
    # Clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_criminal_name.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        self.var_nickname.set("")

    #Search Function.
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Feilds are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='crime_management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                    messagebox.showerror('Error',f'Due to {str(es)}')
if __name__=="__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()