import random
import tkinter
import mysql.connector
from tkinter import *
from tkinter import messagebox


def sresult():
    global s0
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    
    
    def showresult():
            global s0
            global s1
            global s2
            global s3
            global s4
            global s5
            global s6
    
            db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
            stmt=db.cursor()
            stmt.execute("select * from marks where seatno='"+esr1.get()+"'")
            rs=stmt.fetchall()
            i=0
            s0=esr1.get()
            s1=""
            s2=""
            s3=""
            s4=""
            s5=""
            s6=""
            #if len(rs)==0
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
    w9.geometry("600x400")
    lsr1=tkinter.Label(w9,text="ENTER SEAT NO.")
    lsr1.pack()
    
    esr1=tkinter.Entry(w9, textvariable=v1)   
    esr1.pack()
    bsr2=tkinter.Button(w9,text ="SHOW",command=showresult) 
    bsr2.pack()
    lsr2=tkinter.Label(w9,text="AM-IV")
    lsr2.pack()
    esr2=tkinter.Entry(w9 ,textvariable=v2)
    esr2.pack()
    lsr3=tkinter.Label(w9,text="COA")
    lsr3.pack()
    esr3=tkinter.Entry(w9 , textvariable=v3)
    esr3.pack()
    lsr4=tkinter.Label(w9,text="PYTHON LAB")
    esr4=tkinter.Entry(w9,textvariable=v4)
    lsr4.pack()    
    esr4.pack()
    lsr5=tkinter.Label(w9,text="OS")
    lsr5.pack()
    esr5=tkinter.Entry(w9,textvariable=v5)
    esr5.pack()
    lsr6=tkinter.Label(w9,text="AT")
    lsr6.pack()
    esr6=tkinter.Entry(w9,textvariable=v6)
    esr6.pack()
    lsr7=tkinter.Label(w9,text="CN")
    lsr7.pack()
    esr7=tkinter.Entry(w9,textvariable=v7)
    esr7.pack()
    lsr8=tkinter.Label(w9,text="PERCENTAGE")
    lsr8.pack()
    esr8=tkinter.Entry(w9,textvariable=v8)
    esr8.pack()
    
    def gobackshowresult():
        w9.withdraw()
    bsr1=tkinter.Button(w9,text ="Go Back",command=gobackshowresult) 
    bsr1.pack()
    
    
    



def classresult():
    w8=tkinter.Toplevel(root)
    w8.title("SE-5 : SEM IV")
    w8.geometry("600x400")
    
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
    stmt=db.cursor()
    stmt.execute("Select * from marks order by seatno");
    rs=stmt.fetchall()
    l=tkinter.Listbox(w8)
    i=0
    str1=tkinter.StringVar()
    str1=""
    for x in rs:
        i=i+1
        if i%6==1:
            str1+=x[0]+ " | Maths=" +str(x[2])
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
            str1=""
    
    l.pack(fill=tkinter.BOTH, expand=tkinter.YES)
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
        stmt.execute("select * from tstaff where staffid='"+username+"' and staffpassword='"+e9.get()+"'")
        rs=stmt.fetchall()
        if len(rs)==0:
            messagebox.showinfo(title="INVALID",message="Password does not match")
            
        else :
            stmt.execute("delete from marks where seatno='"+e8.get()+"'")
            db.commit()
            messagebox.showinfo(title="DELETED",message="Marks are deleted!")
           
    w7=tkinter.Toplevel(root)
    w7.title("SE-5")
    w7.geometry("600x400")
    l8=tkinter.Label(w7,text="Enter Seat No.")
    l8.pack()
    e8=tkinter.Entry(w7)
    e8.pack()
    l9=tkinter.Label(w7,text="Password for verification")
    l9.pack()
    e9=tkinter.Entry(w7)
    e9.pack()
    bdm1=tkinter.Button(w7,text ="Delete Marks",command=msgboxdm) 
    bdm1.pack()
    
    
def uploadmarks():
    def msgboxum():
        
        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
        stmt=db.cursor()
        stmt.execute("delete from marks where seatno='"+e1.get()+"'")
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
    w6.geometry("600x400")  
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
    w11.geometry("600x400")         
    bn3=tkinter.Button(w11,text ="Top 10 students",command=top10) 
    bn3.pack()
    def closestat():
        w11.withdraw()
    bn2=tkinter.Button(w11,text ="GO Back",command=closestat) 
    bn2.pack()   

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
            w4=tkinter.Toplevel(w2)
            w4.title("SEM 4")
            w4.geometry("600x400")
            bt21=tkinter.Button(w4,text ="Upload Marks",command=uploadmarks) #left
            bt21.pack()
            bt31=tkinter.Button(w4,text ="Delete Marks",command=deletemarks) #left
            bt31.pack()
            bt24=tkinter.Button(w4,text ="Class Result",command=classresult) 
            bt24.pack()
            bn1=tkinter.Button(w4,text ="Statistics",command=statistics) 
            bn1.pack()
            def close25():
                global username
                username=""
                w4.withdraw();
        
            bt25=tkinter.Button(w4,text ="Sign out",command=close25) 
            bt25.pack()
            w4.mainloop()

    w2=tkinter.Toplevel(root)
    w2.title("Staff LOGIN")
    w2.geometry("600x200")
    lt2=tkinter.Label(w2,text="Teacher ID")
    lt2.pack()
    et1=tkinter.Entry(w2)
    et1.pack()
    lt3=tkinter.Label(w2,text="Password")
    lt3.pack()
    et2=tkinter.Entry(w2)
    et2.pack()

    bt2=tkinter.Button(w2,text ="LOGIN",command=staff2 )
    bt2.pack()
    def closebt3():
        w2.withdraw()
    bt3=tkinter.Button(w2,text ="GO BACK",command=closebt3) 
    bt3.pack()
    w2.mainloop()



def studentlogin():
    #root.withdraw()
    def student2():
        global username
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
                w5.geometry("600x400")
               
                
                def gen_seatno():
                    global username
                    while(True):
                        randseatno=random.randint(999,1051)
                        db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
                        stmt=db.cursor()
                        stmt.execute("select * from tstudent where seatno='"+str(randseatno)+"'")
                        
                     #print("select * from tstudent where rollno='"+username+"' and seatno<>''")
                        rs=stmt.fetchall()
                        if len(rs)==0:
                            # update
                            stmt.execute("update tstudent set seatno='"+str(randseatno)+"' where rollno='"+username+"'")
                            db.commit()
                            messagebox.showinfo(title="GENERATED",message="Seat no. generated, please login again!")
                            w5.withdraw()
                            break
        
                db=mysql.connector.connect(host="localhost",user="root",passwd="",database="em1")
                stmt=db.cursor()
                stmt.execute("select * from tstudent where rollno='"+username+"' and seatno<>''")
                print("select * from tstudent where rollno='"+username+"' and seatno<>''")
                rs=stmt.fetchall()
                print(len(rs))
                if len(rs)==0:    
                    bs21=tkinter.Button(w5,text =" Generate Exam Seat No.",command=gen_seatno) 
                    bs21.pack()
                    es21=tkinter.Entry(w5)          #To-Display-SeatNO
                    es21.pack()
                else:
                    #bs21=tkinter.Button(w5,text ="Exam Seat No.",command="") 
                    #bs21.pack()
                    v=tkinter.StringVar()
                    for xx in rs:
                        v.set(xx[1])
                        break
                    es21=tkinter.Entry(w5,textvariable=v,state='disabled')          #To-Display-SeatNO
                    es21.pack()
                bs23=tkinter.Button(w5,text ="CR Allotment",command="")    #left
                bs23.pack()
                bs24=tkinter.Button(w5,text ="Exam Timetable",command="")      #left
                bs24.pack()
                bs25=tkinter.Button(w5,text ="Result",command=sresult)          
                bs25.pack()
                def closebs26():
                    w5.withdraw()
                    
                bs26=tkinter.Button(w5,text ="Sign out",command=closebs26)          
                bs26.pack()    
    
              
    w3=tkinter.Toplevel(root)
    w3.title("Student LOGIN")
    w3.geometry("600x200")
    """C = Canvas(w3, bg="blue", height=400, width=600)
    C.pack() """
    ls2=tkinter.Label(w3,text=" Student ID:")
    ls2.place(x=190,y=10)
   
    es1=tkinter.Entry(w3)
    es1.place(x=270,y=10)
    ls3=tkinter.Label(w3,text="Password:")
    ls3.place(x=197,y=50)
    es2=tkinter.Entry(w3)
    es2.place(x=270,y=50)
    bs2=tkinter.Button(w3,text ="LOGIN",command=student2) 
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
root.geometry('%dx%d+%d+%d'%(470,1,100,50))
root.title("SHAH & ANCHOR KUTCHHI ENGINEERING COLLEGE")
"""C = Canvas(root, bg="blue", height=250, width=300)
pic1 = PhotoImage(file = "C:\\Users\\Nilesh\\Downloads\\aaa.png")
C.create_image(0,0, image=pic1,anchor=NW)
C.pack()"""
"""photo = PhotoImage(file='aaa.png')
label = Label(root, image=photo)
label.pack()"""
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
login_menu = Menu(mb, tearoff=0)
mb.add_cascade(label="login",menu=login_menu)
login_menu.add_command(label="Teachers login",command=stafflogin)
login_menu.add_separator()
login_menu.add_command(label="Student Login",command=studentlogin)

root.config(menu=mb)

root.mainloop()


