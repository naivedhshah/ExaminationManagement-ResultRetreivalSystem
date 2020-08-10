import random
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

def timetable():
    w101=tkinter.Toplevel(root)
    w101.title("SE-EXAM TIME TAABLE")
    w101.geometry("1000x525")

    pic3 = PhotoImage(file = "C:\\Users\\Nilesh\\Desktop\\sem4\\EXAMINATION MANAGEMENT f\\pics\\kjk.png")
    w = Label(w101, image=pic3,anchor=CENTER)
    w.photo = pic3   
    w.place(x=300,y=100)
    w.pack()

def failedstud():
    w100=tkinter.Toplevel(root)
    w100.title("SE-5")
    w100.geometry("600x400")  
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
    stmt=db.cursor()
    stmt.execute(" select subject.subjectno,subject.subjectname,marks.seatno, marks.subjectno, marks.subjectmarks,tstudent.studentname from subject,marks,tstudent where marks.subjectno=subject.subjectno and tstudent.seatno=marks.seatno having(subjectmarks)<32 order by marks.seatno;");
    rs=stmt.fetchall()
    ll=tkinter.Listbox(w100)
    i=0
    str2=tkinter.StringVar()
    str2=""
    for fp in rs:
        i=i+1
        str2+= str(fp[2])+" | "+ fp[5]+" | "+str(fp[1])
        ll.insert(tkinter.END,str2+ " | MARKS= "+str(fp[4]))
        str2=""
        
    
    ll.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    def closebfs1():
        w100.withdraw()
    
    bfs1=tkinter.Button(w100,text ="Go Back",command=closebfs11)          
    bfs1.pack()
def sresult():
    global s0
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global username
    
    
    def showresult():
            
            global s0
            global s1
            global s2
            global s3
            global s4
            global s5
            global s6
            global username
            
    
            db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
            stmt=db.cursor()
            stmt.execute("select * from marks where seatno='"+esr1.get()+"' and seatno in (select seatno from tstudent where rollno='"+username+"');")
            rs=stmt.fetchall()
            i=0
            s0=esr1.get()
            s1=""
            s2=""
            s3=""
            s4=""
            s5=""
            s6=""
            if len(rs)!=0 :
                for x in rs:
                    i=i+1
                    s0=x[0]
                    if i==1: s1=str(x[2])
                    elif i==2: s2=str(x[2])
                    elif i==3: s3=str(x[2])
                    elif i==4: s4=str(x[2])
                    elif i==5: s5=str(x[2])
                    elif i==6: s6=str(x[2])
                
                w9.withdraw()
                sresult()
                
            else:
                w9.withdraw()
                messagebox.showinfo(title="ALLOWANCE DENIED",message="Please enter a valid seat no.")
                
        
            
    v1=tkinter.StringVar()
    v2=tkinter.StringVar()
    v3=tkinter.StringVar()
    v4=tkinter.StringVar()
    v5=tkinter.StringVar()
    v6=tkinter.StringVar()
    v7=tkinter.StringVar()
    v8=tkinter.StringVar()
    v1.set(s0)
    v2.set(s1)
    v3.set(s2)
    v4.set(s3)
    v5.set(s4)
    v6.set(s5)
    v7.set(s6)
    if len(s0)==0 or len(s1)==0 or len(s2)==0 or len(s2)==0 or len(s3)==0 or len(s4)==0 or len(s5)==0 or len(s6)==0 :
        v8.set("")
        
    else:
        total=(int(s1)+int(s2)+int(s3)+int(s4)+int(s5)+int(s6))/6.0
        v8.set(str(total))
        
    w9=tkinter.Toplevel(root)
    w9.title("SEM-IV")
    w9.geometry("425x500")
    """ C = Canvas(w9, bg="thistle3", height=1000, width=800)            
    C.pack()"""
    pic3 = PhotoImage(file="C:\\Users\\Nilesh\\Downloads\\225.png")
    w = Label(w9, image=pic3,anchor=NW)
    w.photo = pic3   
    w.place(x=100,y=300)
    w.pack()
    lsr1=tkinter.Label(w9,text="ENTER SEAT NO.",bg='white')
    lsr1.place(x=50,y=25)
    
    esr1=tkinter.Entry(w9, textvariable=v1)   
    esr1.place(x=160,y=25)
    bsr2=tkinter.Button(w9,text ="SHOW",command=showresult,bg='white') 
    bsr2.place(x=130,y=72)
    lsr2=tkinter.Label(w9,text="AM-IV",bg='white')
    lsr2.place(x=50,y=125)
    esr2=tkinter.Entry(w9 ,textvariable=v2,state='disabled')
    esr2.place(x=150,y=125)
    lsr3=tkinter.Label(w9,text="COA",bg='white')
    lsr3.place(x=50,y=175)
    esr3=tkinter.Entry(w9 , textvariable=v3,state='disabled')
    esr3.place(x=150,y=175)
    lsr4=tkinter.Label(w9,text="PYTHON LAB",bg='white')
    esr4=tkinter.Entry(w9,textvariable=v4,state='disabled')
    lsr4.place(x=50,y=225)    
    esr4.place(x=150,y=225)
    lsr5=tkinter.Label(w9,text="OS",bg='white')
    lsr5.place(x=50,y=275)
    esr5=tkinter.Entry(w9,textvariable=v5,state='disabled')
    esr5.place(x=150,y=275)
    lsr6=tkinter.Label(w9,text="AT",bg='white')
    lsr6.place(x=50,y=325)
    esr6=tkinter.Entry(w9,textvariable=v6,state='disabled')
    esr6.place(x=150,y=325)
    lsr7=tkinter.Label(w9,text="CN",bg='white')
    lsr7.place(x=50,y=375)
    esr7=tkinter.Entry(w9,textvariable=v7,state='disabled')
    esr7.place(x=150,y=375)
    lsr8=tkinter.Label(w9,text="PERCENTAGE",bg='white')
    lsr8.place(x=175,y=425)
    esr8=tkinter.Entry(w9,textvariable=v8,state='disabled')
    esr8.place(x=150,y=450)
    
    def gobackshowresult():
        w9.withdraw()
    bsr1=tkinter.Button(w9,text ="Go Back",command=gobackshowresult) 
    bsr1.place(x=360,y=460)
    
    
    



def classresult():
    w8=tkinter.Toplevel(root)
    w8.title("SE-5 : SEM IV")
    w8.geometry("600x300")
    
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
    stmt=db.cursor()
    stmt.execute("Select * from marks order by seatno,subjectno");    
    rs=stmt.fetchall()
    l=tkinter.Listbox(w8)
    i=0
    str1=tkinter.StringVar()
    str1=""
    for x in rs:
        i=i+1
        if i%6==1:
            str1+=x[0]+ " | Maths=" +str(x[2])      #string getting update and concatenated 
        if i%6==2:
            str1+= " | COA=" +str(x[2])
        if i%6==3:
            str1+=" | Python Lab=" +str(x[2])
        if i%6==4:
            str1+= " | OS=" +str(x[2])
        if i%6==5:
            str1+= " | AT=" +str(x[2])
        if i%6==0:
            l.insert(tkinter.END,str1+ " | CN=" +str(x[2]))
            str1=""                                             #to make string null for next row 
    
    l.pack(fill=tkinter.BOTH, expand=tkinter.YES)            #both is to expand horizontally&vertically and YES is to hold every item
    def closebcr1():
        w8.withdraw()
    
    bcr1=tkinter.Button(w8,text ="Go Back",command=closebcr1)          
    bcr1.pack()
    
        
    
    

def deletemarks():
    def msgboxdm():
        global username
        w7.withdraw()
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
        stmt=db.cursor()
        stmt.execute("select * from tstaff where staffid='"+username+"' and staffpassword='"+e9.get()+"'")       #for re-verification 
        rs=stmt.fetchall()
        if len(rs)==0:
            messagebox.showinfo(title="INVALID",message="Password does not match")
            
        else :
            stmt.execute("delete from marks where seatno='"+e8.get()+"'")     
            db.commit()
            messagebox.showinfo(title="DELETED",message="Marks are deleted!")
           
    w7=tkinter.Toplevel(root)
    w7.title("SE-5")
    w7.geometry("600x200")
    pic3 = PhotoImage(file="C:\\Users\\Nilesh\\Downloads\\black-metal-grill-texture-x-textured-473647.png")
    w = Label(w7, image=pic3,anchor=CENTER)
    w.photo = pic3   
    w.place(x=300,y=100)
    w.pack()
    l8=tkinter.Label(w7,text="Enter Seat No.")
    l8.place(x=235,y=50)
    e8=tkinter.Entry(w7)
    e8.place(x=365,y=50)
    l9=tkinter.Label(w7,text="Password for verification")
    l9.place(x=225,y=100)
    e9=tkinter.Entry(w7,show='*')
    e9.place(x=365,y=100)
    bdm1=tkinter.Button(w7,text ="Delete Marks",command=msgboxdm) 
    bdm1.place(x=255,y=150)
    
def editmarks():
    def msgboxum1():
        
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
        stmt=db.cursor()
        stmt.execute("delete from marks where seatno='"+e1e.get()+"'")       #so the previous marks are deleted and new marks are only entered 
        stmt.execute("insert into marks values('"+e1e.get()+"',1,"+e2e.get()+")")
        stmt.execute("insert into marks values('"+e1e.get()+"',2,"+e3e.get()+")")
        stmt.execute("insert into marks values('"+e1e.get()+"',3,"+e4e.get()+")")
        stmt.execute("insert into marks values('"+e1e.get()+"',4,"+e5e.get()+")")
        stmt.execute("insert into marks values('"+e1e.get()+"',5,"+e6e.get()+")")
        stmt.execute("insert into marks values('"+e1e.get()+"',6,"+e7e.get()+")")
        db.commit()
        messagebox.showinfo(title="ENTERED",message="Marks are successfully entered!")
        w6.withdraw()
    
    w61=tkinter.Toplevel(root)
    w61.title("SE-5-EDIT MARKS")
    w61.geometry("500x350")
    
    
    l1e=tkinter.Label(w61,text="ENTER SEAT NO.")
    l1e.pack()
    e1e=tkinter.Entry(w61)
    e1e.pack()
    l2e=tkinter.Label(w61,text="AM-IV")
    l2e.pack()
    e2e=tkinter.Entry(w61)
    e2e.pack()
    l3e=tkinter.Label(w61,text="COA")
    l3e.pack()
    e3e=tkinter.Entry(w61)
    e3e.pack()
    l4e=tkinter.Label(w61,text="PYTHON LAB")
    e4e=tkinter.Entry(w61)
    l4e.pack()    
    e4e.pack()
    l5e=tkinter.Label(w61,text="OS")
    l5e.pack()
    e5e=tkinter.Entry(w61)
    e5e.pack()
    l6e=tkinter.Label(w61,text="AT")
    l6e.pack()
    e6e=tkinter.Entry(w61)
    e6e.pack()
    l7e=tkinter.Label(w61,text="CN")
    l7e.pack()
    e7e=tkinter.Entry(w61)
    e7e.pack()
    bum1e=tkinter.Button(w61,text ="Enter Marks",command=msgboxum1) 
    bum1e.pack()
    def closebum2e():
        w61.withdraw()
    bum2=tkinter.Button(w61,text ="Go Back",command=closebum2e)          
    bum2.pack()
    
def uploadmarks():
    def msgboxum():
        
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
        stmt=db.cursor()
        #stmt.execute("delete from marks where seatno='"+e1.get()+"'")
        stmt.execute("insert into marks values('"+e1.get()+"',1,"+e2.get()+")")
        stmt.execute("insert into marks values('"+e1.get()+"',2,"+e3.get()+")")
        stmt.execute("insert into marks values('"+e1.get()+"',3,"+e4.get()+")")
        stmt.execute("insert into marks values('"+e1.get()+"',4,"+e5.get()+")")
        stmt.execute("insert into marks values('"+e1.get()+"',5,"+e6.get()+")")
        stmt.execute("insert into marks values('"+e1.get()+"',6,"+e7.get()+")")
        db.commit()
        messagebox.showinfo(title="ENTERED",message="Marks are successfully entered!")
        w6.withdraw()
    
    w6=tkinter.Toplevel(root)
    w6.title("SE-5")
    w6.geometry("500x350")
    
    l1=tkinter.Label(w6,text="ENTER SEAT NO.")
    l1.pack()
    e1=tkinter.Entry(w6)
    e1.pack()
    l2=tkinter.Label(w6,text="AM-IV")
    l2.pack()
    e2=tkinter.Entry(w6)
    e2.pack()
    l3=tkinter.Label(w6,text="COA")
    l3.pack()
    e3=tkinter.Entry(w6)
    e3.pack()
    l4=tkinter.Label(w6,text="PYTHON LAB")
    e4=tkinter.Entry(w6)
    l4.pack()    
    e4.pack()
    l5=tkinter.Label(w6,text="OS")
    l5.pack()
    e5=tkinter.Entry(w6)
    e5.pack()
    l6=tkinter.Label(w6,text="AT")
    l6.pack()
    e6=tkinter.Entry(w6)
    e6.pack()
    l7=tkinter.Label(w6,text="CN")
    l7.pack()
    e7=tkinter.Entry(w6)
    e7.pack()
    bum1=tkinter.Button(w6,text ="Enter Marks",command=msgboxum) 
    bum1.pack()
    def closebum2():
        w6.withdraw()
    bum2=tkinter.Button(w6,text ="Go Back",command=closebum2)          
    bum2.pack()
def top10():
             global p0
             global p1
             global p2
             global p3
             global p4
             global p5
             global p6
             global p7
             global p8
             global p9
         
             def top102():
                 global p0
                 global p1
                 global p2
                 global p3
                 global p4
                 global p5
                 global p6
                 global p7
                 global p8
                 global p9
                 db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
                 stmt=db.cursor()
                 stmt.execute("select studentname,marks.seatno from tstudent,marks where tstudent.seatno=marks.seatno group by seatno having max(subjectmarks) order by sum(subjectmarks) desc;") 
                 rs=stmt.fetchall()
                 p0=""
                 p1=""
                 p2=""
                 p3=""
                 p4=""
                 p5=""
                 p6=""
                 p7=""
                 p8=""
                 p9=""
                 ii=0
                 for xxx in rs:
                        ii=ii+1
                        if ii==1: p0=("1.",xxx[0])
                        elif ii==2: p1=("2.",xxx[0])
                        elif ii==3: p2=("3",xxx[0])
                        elif ii==4: p3=("4.",xxx[0])
                        elif ii==5: p4=("5.",xxx[0])
                        elif ii==6: p5=("6.",xxx[0])
                        elif ii==7: p6=("7.",xxx[0])
                        elif ii==8: p7=("8.",xxx[0])
                        elif ii==9: p8=("9.",xxx[0])
                        elif ii==10:p9=("10.",xxx[0])
                 w10.withdraw()   
                 top10()
                
            
                
             w10=tkinter.Toplevel()
             w10.title("SEM 4: TOP 10")
             w10.geometry("600x400")
             vv1=tkinter.StringVar()
             vv2=tkinter.StringVar()
             vv3=tkinter.StringVar()
             vv4=tkinter.StringVar()
             vv5=tkinter.StringVar()
             vv6=tkinter.StringVar()
             vv7=tkinter.StringVar()
             vv8=tkinter.StringVar()
             vv9=tkinter.StringVar()
             vv10=tkinter.StringVar()
             vv1.set(p0)
             vv2.set(p1)
             vv3.set(p2)
             vv4.set(p3)
             vv5.set(p4)
             vv6.set(p5)
             vv7.set(p6)
             vv8.set(p7)
             vv9.set(p8)
             vv10.set(p9)
             ett1=tkinter.Entry(w10, textvariable=vv1)   
             ett1.pack()
             ett2=tkinter.Entry(w10, textvariable=vv2)   
             ett2.pack()
             ett3=tkinter.Entry(w10, textvariable=vv3)   
             ett3.pack()
             ett4=tkinter.Entry(w10, textvariable=vv4)   
             ett4.pack()
             ett5=tkinter.Entry(w10, textvariable=vv5)   
             ett5.pack()
             ett6=tkinter.Entry(w10, textvariable=vv6)   
             ett6.pack()
             ett7=tkinter.Entry(w10, textvariable=vv7)   
             ett7.pack()
             ett8=tkinter.Entry(w10, textvariable=vv8)   
             ett8.pack()
             ett9=tkinter.Entry(w10, textvariable=vv9)   
             ett9.pack()
             ett10=tkinter.Entry(w10, textvariable=vv10)   
             ett10.pack()   
             btp1=tkinter.Button(w10,text ="Show",command=top102) 
             btp1.pack()
             def closetop():
                 w10.withdraw()
             btp2=tkinter.Button(w10,text ="GO Back",command=closetop) 
             btp2.pack()
def statistics(): 
    w11=tkinter.Toplevel()
    w11.title("SEM 4: ANALYSIS")
    w11.geometry("670x200")
    pic100 = PhotoImage(file="C:\\Users\\Nilesh\\Downloads\\new-statistics.png")
    w = Label(w11, image=pic100,anchor=NW)
    w.photo = pic100
    
    w.place(x=100,y=300)
    w.pack()
    bn3=tkinter.Button(w11,text ="Top 10 students",command=top10) 
    bn3.place(x=313,y=75)
    bn4=tkinter.Button(w11,text ="Failed Students",command=failedstud) 
    bn4.place(x=313,y=125)
    
    def closestat():
        w11.withdraw()
        
    bn2=tkinter.Button(w11,text ="Go Back",command=closestat) 
    bn2.place(x=323,y=168)

def stafflogin():
    #root.withdraw()
    
    def staff2():
        global username
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
        stmt=db.cursor()
        stmt.execute("select * from tstaff where staffid='"+et1.get()+"' and staffpassword='"+et2.get()+"'")
        rs=stmt.fetchall()
        if len(rs)==0:
            print("Invalid login")
            messagebox.showinfo(title="INVALID",message="INVALID CREDENTIALS!")
        else:
            username=et1.get()
            w2.withdraw()
            w4=tkinter.Toplevel(root)
            w4.title("SEM 4")
            w4.geometry("400x400")
            c=Canvas(w4, bg="light cyan", height=1000, width=800)            
            c.pack()
            c.create_text(125,22,fill="darkblue",font="Times 28 italic bold",text="Welcome,user!",justify=CENTER)
            c.update
            
            bt21=tkinter.Button(w4,text ="Upload Marks",command=uploadmarks) #left
            bt21.place(x=160,y=100)
            bt211=tkinter.Button(w4,text ="Edit Marks",command=editmarks) #left
            bt211.place(x=160,y=150)
            bt31=tkinter.Button(w4,text ="Delete Marks",command=deletemarks) #left
            bt31.place(x=166,y=200)
            bt24=tkinter.Button(w4,text ="Class Result",command=classresult) 
            bt24.place(x=167,y=250)
            bn1=tkinter.Button(w4,text ="Statistics",command=statistics) 
            bn1.place(x=172,y=300)
            def close25():
                global username
                username=""
                w4.withdraw()
        
            bt25=tkinter.Button(w4,text ="Sign out",command=close25) 
            bt25.place(x=171,y=350)
            w4.mainloop()

    w2=tkinter.Toplevel(root)
    w2.title("Staff LOGIN")
    w2.geometry("600x200")
    C = Canvas(w2, bg="powderblue", height=1000, width=800)            
    C.pack()
    lt2=tkinter.Label(w2,text="Teacher ID")
    lt2.place(x=190,y=10)
    et1=tkinter.Entry(w2)
    et1.place(x=270,y=10)
    lt3=tkinter.Label(w2,text="Password",)
    lt3.place(x=197,y=50)
    et2=tkinter.Entry(w2,show="*")
    et2.place(x=270,y=50)

    bt2=tkinter.Button(w2,text ="LOGIN",command=staff2 )
    bt2.place(x=310,y=70)
    def closebt3():
        w2.withdraw()
    bt3=tkinter.Button(w2,text ="GO BACK",command=closebt3) 
    bt3.place(x=305,y=100)
    w2.mainloop()



def studentlogin():
    #root.withdraw()
    def student2():
        global username
        global randseatno1
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
        stmt=db.cursor()
        stmt.execute("select * from tstudent where rollno='"+es1.get()+"' and studentpassword='"+es2.get()+"'")
        rs=stmt.fetchall()
        if len(rs)==0:
                print("Invalid login")
                messagebox.showinfo(title="INVALID",message="INVALID CREDENTIALS!")
        else:
                username=es1.get()    
                w3.withdraw()    
                w5=tkinter.Toplevel(root)
                w5.title("SEM IV")
                w5.geometry("500x300")
                C = Canvas(w5, bg="indianred", height=1000, width=800)
                
                C.pack()
               
                
                def gen_seatno():
                    global username
                    global randseatno1
                    p=999+int(username)
                    while(True):
                        while(True):
                            p=p+1
                            break
                        
                        randseatno=random.randint(p,p)
                        randseatno1=randseatno
                        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
                        stmt=db.cursor()
                        stmt.execute("select * from tstudent where seatno='"+str(randseatno)+"'")
                        
                
                        rs=stmt.fetchall()
                        if len(rs)==0:
                            # update
                            stmt.execute("update tstudent set seatno='"+str(randseatno)+"' where rollno='"+username+"'")
                            db.commit()
                            messagebox.showinfo(title="GENERATED",message="Seat no. generated, please login again!")
                            w5.withdraw()
                            break
                #2
                db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
                stmt=db.cursor()
                stmt.execute("select * from tstudent where rollno='"+username+"' and seatno<>''")
                print("select * from tstudent where rollno='"+username+"' and seatno<>''")
                rs=stmt.fetchall()
                print(len(rs))
                if len(rs)==0:    
                    C.create_text(105,19,fill="darkblue",font="Times 25 italic bold",text="Welcome,user!")
                    C.update
                    bs21=tkinter.Button(w5,text =" Generate Exam Seat No.",command=gen_seatno) 
                    bs21.place(x=100,y=50)
                    es21=tkinter.Entry(w5)          #To-Display-SeatNO
                    es21.place(x=300,y=55)
                else:
                    
                    C.create_text(105,19,fill="darkblue",font="Times 25 italic bold",text="Welcome,user!")
                    C.update
                    v=tkinter.StringVar()
                    for xx in rs:
                        v.set(xx[1])
                        break
                    es21=tkinter.Entry(w5,textvariable=v,state='disabled')          #To-Display-SeatNO
                    es21.place(x=375,y=50)
                
                bs24=tkinter.Button(w5,text ="Exam Timetable",command=timetable)      
                bs24.place(x=200,y=100)
                bs25=tkinter.Button(w5,text ="Result",command=sresult)          
                bs25.place(x=215,y=150)
                def closebs26():
                    w5.withdraw()
                    
                bs26=tkinter.Button(w5,text ="Sign out",command=closebs26)          
                bs26.place(x=400,y=255)    
    
    #1         
    w3=tkinter.Toplevel(root)
    w3.title("Sign in")
    w3.geometry("600x200")
    C = Canvas(w3, bg="powderblue", height=1000, width=800)
    pic2 = PhotoImage(file = "C:\\Users\\Nilesh\\Downloads\\aaa.png")
    C.create_image(0,0, image=pic2,anchor=NW)
    C.pack()
    
    ls2=tkinter.Label(w3,text=" Student ID:")
    ls2.place(x=190,y=10)
    es1=tkinter.Entry(w3)
    es1.place(x=270,y=10)
    ls3=tkinter.Label(w3,text="Password:")
    ls3.place(x=197,y=50)
    es2=tkinter.Entry(w3,show="*")
    es2.place(x=270,y=50)
    bs2=tkinter.Button(w3,text ="sign in",command=student2) 
    bs2.place(x=310,y=70)
    def closebs2():
        w3.withdraw()
    bs3=tkinter.Button(w3,text ="GO BACK",command=closebs2) 
    bs3.place(x=305,y=100)
    

global s0
global s1
global s2
global s3
global s4
global s5
global s6
global username
global randseatno1

username=""
s0=""
s1=""
s2=""
s3=""
s4=""
s5=""
s6=""
    
global p0
global p1
global p2
global p3
global p4
global p5
global p6
global p7
global p8
global p9
p0=""
p1=""
p2=""
p3=""
p4=""
p5=""
p6=""
p7=""
p8=""
p9=""
root=tkinter.Tk()
root.geometry("600x400")
root.title("SHAH & ANCHOR KUTCHHI ENGINEERING COLLEGE")


C = Canvas(root, bg="blue", height=1000, width=800)
pic1 = PhotoImage(file = "C:\\Users\\Nilesh\\Downloads\\aaa.png")
C.create_image(0,0, image=pic1,anchor=NW)
C.pack()



mb=Menu(root)
about_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="About us",menu=about_menu)

academic_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="Academic",menu=academic_menu)

admission_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="Admission",menu=admission_menu)

placement_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="Placement",menu=placement_menu)

gallery_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="Gallery",menu=gallery_menu)

researchcell_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="Research Cell",menu=researchcell_menu)

mb.add_cascade(label="Events",menu=about_menu)
events_menu = Menu(mb, tearoff=0)

mb.add_cascade(label="Contact us",menu=about_menu)
contact_menu = Menu(mb, tearoff=0)

login_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="    login",menu=login_menu)
login_menu.add_command(label="Teachers login",command=stafflogin)
login_menu.add_separator()
login_menu.add_command(label="Student Login",command=studentlogin)

root.config(menu=mb)

root.mainloop()


