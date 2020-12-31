def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        print(id, name, email)
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob))
            con.commit()
            res = messagebox.askyesnocancel('Successfully Added','USN {} Name {} added Successfully...! Do you want to Clear the Form to add New one'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')


        except:
                messagebox.showerror('Duplicacy Error!!','Enterd USN is already present Please check and try Again..!!',parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentmttable.delete(*studentmttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
            studentmttable.insert('',END,values=vv)
            print(vv)
        print(datas)

        print('Submitted')


    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('DCB - Add a Student')
    addroot.config(bg='blue')
    addroot.iconbitmap('student.ico')
    addroot.resizable(False,False)
    #           Add Student Labels
    idlabel = Label(addroot,text='Enter USN ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    Addresslabel = Label(addroot,text='Enter Address ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter DOB ',bg='gold2',font=('Consolas',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)



    #---------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=220,y=10)

    nameentry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=220,y=70)

    mobileentry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=220,y=130)

    emailsentry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=emailval)
    emailsentry.place(x=220,y=190)

    addressentry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=220,y=250)

    genderentry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=220,y=310)

    dobentry = Entry(addroot,font=('Consolas',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=220,y=370)

    submitbtn = Button(addroot,text='Submit',font=('Consolas',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)


    addroot.mainloop()
    print("Student Added")








#--------Searrch Student
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        if(id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)
        elif(name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)

        elif(mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)
        elif(email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)
        elif(address != ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)
        elif(gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)
        elif(dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studentmttable.delete(*studentmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                studentmttable.insert('', END, values=vv)
                print(vv)
            print(datas)


        print('Searched Student Result')

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('DCB - Add a Student')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap('student.ico')
    searchroot.resizable(False, False)
    #           Add Student Labels
    idlabel = Label(searchroot, text='Enter USN ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    Addresslabel = Label(searchroot, text='Enter Address ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter DOB ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    # datelabel = Label(searchroot, text='Enter DOB ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
    #                  borderwidth=3, width=12, anchor='w')
    # datelabel.place(x=10, y=430)

    # ---------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=220, y=10)

    nameentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=220, y=70)

    mobileentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=220, y=130)

    emailsentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=emailval)
    emailsentry.place(x=220, y=190)

    addressentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=220, y=250)

    genderentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=220, y=310)

    dobentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=220, y=370)

    dateentry = Entry(searchroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=220, y=430)

    submitbtn = Button(searchroot, text='Submit', font=('Consolas', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=search)
    submitbtn.place(x=150, y=480)

    searchroot.mainloop()


def deletestudent():
    cc = studentmttable.focus()
    content = studentmttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Deleted Sucessfuly','USN {} Deleted Successfully deleted'.format(pp))

    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentmttable.delete(*studentmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
        studentmttable.insert('', END, values=vv)
        print(vv)
    print(content)


    print("Student Delete")





def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob))
        con.commit()
        messagebox.showinfo('Updated Sucessfully...','USN {} Modified successfully...',format(id))

        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentmttable.delete(*studentmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
            studentmttable.insert('', END, values=vv)
            print(vv)



        print('Student Updated!!')

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x540+220+200')
    updateroot.title('DCB - Add a Student')
    updateroot.config(bg='skyblue')
    updateroot.iconbitmap('student.ico')
    updateroot.resizable(False, False)
    #           Add Student Labels
    idlabel = Label(updateroot, text='Enter USN ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    Addresslabel = Label(updateroot, text='Enter Address ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter DOB ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter DOB ', bg='gold2', font=('Consolas', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    # ---------Add Student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=220, y=10)

    nameentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=220, y=70)

    mobileentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=220, y=130)

    emailsentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=emailval)
    emailsentry.place(x=220, y=190)

    addressentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=220, y=250)

    genderentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=220, y=310)

    dobentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=220, y=370)

    dateentry = Entry(updateroot, font=('Consolas', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=220, y=430)

    submitbtn = Button(updateroot, text='Submit', font=('Consolas', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=update)
    submitbtn.place(x=150, y=480)


    cc = studentmttable.focus()
    content = studentmttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])





    updateroot.mainloop()
    print("Student Update")

def showastudent():
    print("Student Show")

def exportstudent():
    print("Student Exported")

def exitstudent():
    res = messagebox.askyesnocancel("Are you sure","Do you want to exit ?")
    if(res==True):
        root.destroy()
    print("Student Data Exited")






#           Establishing Connection to DataBase
def connectDB():
    def submidb():
        global con,mycursor
        # host = hostvalue.get()
        # user = uservalue.get()
        # password = passwordvalue.get()
        host = 'localhost'
        user = 'root'
        password = 'harsha'
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror("Invalid Credentials","Your entered values do not match!!")
            return
        try:
            strr = 'create Database StudentManagement2'
            mycursor.execute(strr)
            strr = 'use StudentManagement2'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int, name varchar(20),mobile varchar(12),email varchar(40),address varchar(100),gender varchar(10),dob varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.INFO('Connecting... Establishing connection to DataBase, Please wait...',parent=dbroot)
            messagebox.showinfo('Success','Database is Created Successfuly Now You are connected to database..',parent=dbroot)

        except:
            strr = 'use StudentManagement2'
            mycursor.execute(strr)
            messagebox.showinfo('Success','You are successfully connected to database..',parent=dbroot)
        dbroot.destroy()

        print(host,user,password)
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('530x250+800+230')
    dbroot.iconbitmap('student.ico')
    dbroot.title('Authentication 🔒')
    dbroot.resizable(False,False)
    dbroot.config(bg='#ffe8d9')



#          Labels

    hostlabel = Label(dbroot, text = "Enter Host", font=('Consolas', 17), bg='#ffe8d9', borderwidth=3, width=20, anchor='w')
    hostlabel.place(x=10, y=13)

    userlabel = Label(dbroot, text = "Enter UserName ", font=('Consolas', 17), bg='#ffe8d9', borderwidth=3, width=20, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text = "Enter Password  🔑", font=('Consolas', 17), bg='#ffe8d9', borderwidth=3, width=20, anchor='w')
    passwordlabel.place(x=10, y= 130)






    #Databse Authenticatication Input


    hostvalue = StringVar()
    uservalue = StringVar()
    passwordvalue = StringVar()


    hostinput = Entry(dbroot,font=('Consolas', 15),bd=2,textvariable=hostvalue)
    hostinput.place(x=280, y=13)

    userinput = Entry(dbroot,font=('Consolas', 15),bd=2,textvariable=uservalue)
    userinput.place(x=280, y=70)

    passwordinput = Entry(dbroot,font=('Consolas', 15),bd=2,textvariable=passwordvalue)
    passwordinput.place(x=280, y=130)


    #       Connect DB Button
    submitbutton = Button(dbroot,text='Connect', font=('Consolas', 15), width=20, bg='#a5d6fe',
                          activebackground = '#55b2fd', activeforeground = 'white',command=submidb)
    submitbutton.place(x=150,y=190)



    dbroot.mainloop()



def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date : '+date_string+"\nTime : "+time_string)
    clock.after(100,tick)



def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text = text)
    count += 1
    SliderLabel.after(200,IntroLabelTick)

from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root = Tk()
root.title('Navkis College of Engineering : Demand Collection Balance')
root.config(bg='#1e4ba0')
root.geometry('1174x700+200+50')
root.iconbitmap('student.ico')
root.resizable(False, False)



#        Frames


DataEntryFrame = Frame(root, bg='#f9e4db', relief = RIDGE, borderwidth = 5)
DataEntryFrame.place(x = 0, y = 60, width = 300, height = 642)




#       -------DataEntry Section-------

frontLabel = Label(DataEntryFrame,text='<-- Select any Operations -->',width=35,font=('Consolas',12,'bold'),bg='gold2')
frontLabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='Add Student',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)



searchbtn = Button(DataEntryFrame,text='Search Student',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)


deletebtn = Button(DataEntryFrame,text='Delete Student',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)


updatebtn = Button(DataEntryFrame,text='Update Student',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)


showallbtn = Button(DataEntryFrame,text='Show All',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=showastudent)
showallbtn.pack(side=TOP,expand=True)


exportbtn = Button(DataEntryFrame,text='Export Data',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)


exitbtn = Button(DataEntryFrame,text='Exit',width=25,font=('Consolas',20,'bold'),bd=4,bg='skyblue',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)







ShowDataFrame = Frame(root, bg='#c9e9f6', relief = RIDGE, borderwidth = 5)
ShowDataFrame.place(x = 300, y = 60, width = 875, height = 642)






#----------Displaying Data Frame
style = ttk.Style()
style.configure('Treeview.Heading',font=('Consolas',20,'bold'),foreground='blue')
style.configure('Treeview',font=('Consolas',20,'bold'),background='cyan',foreground='black')

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studentmttable = Treeview(ShowDataFrame,columns=('USN','Name','Mobile No','Email','Address','Gender','D O B'),
                          yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=studentmttable.xview)
scroll_y.config(command=studentmttable.yview)

studentmttable.heading('USN',text='USN')
studentmttable.heading('Name',text='Name')
studentmttable.heading('Email',text='Email')
studentmttable.heading('Mobile No',text='Mobile No')
studentmttable.heading('Address',text='Address')
studentmttable.heading('Gender',text='Gender')
studentmttable.heading('D O B',text='D O B')
studentmttable['show'] = 'headings'

studentmttable.column('USN',width=200)
studentmttable.column('Name',width=300)
studentmttable.column('Email',width=400)
studentmttable.column('Mobile No',width=200)
studentmttable.column('Address',width=400)
studentmttable.column('Gender',width=100)
studentmttable.column('D O B',width=200)




studentmttable.pack(fill=BOTH,expand=1)





#          Slider
#ss = 'Navkis College of Engineering'
ss = 'NAVKIS COLLEGE OF ENGINEERING'
count = 0;
text = ' '


SliderLabel = Label(root, text = ss, font=('Candara',30, 'bold'),relief=RIDGE, borderwidth = 0, width = 35, bg = '#1e4ba0', foreground = 'white')
SliderLabel.place(x = 200, y = 0)

IntroLabelTick()



#           Clock

clock = Label(root, font=('Microsoft JhengHei',10),relief=RIDGE, borderwidth = 0, bg = '#1e4ba0',foreground = 'white')
clock.place(x = 0, y = 0)
tick()


#           Connect to DataBase

connectButton = Button(root,font=('Calibri',13),relief=RIDGE, bg='#ffbf00', borderwidth = 0, text = "Connect to DataBase📡", width = 20, activebackground = '#ff8c00', activeforeground = 'white',command=connectDB)
connectButton.place(x = 980, y = 15)



root.mainloop()