from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt
import mysql.connector 
import webbrowser
from PIL import Image,ImageTk
import speech_recognition as sr
import os
import time
import datetime
import csv
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
mydb=mysql.connector.connect(host="localhost",user="root",passwd=" ")
mycursor=mydb.cursor()
mycursor.execute("use sgp")
mydb.commit()
#************************VOICE RECORDER FUNCTIONS**********************************************************
def voice_recorder():#sign-in u
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.record(source,duration=5)
        try:
            u.set(r.recognize_google(audio))
        except Exception as e:
            messagebox.showinfo("Invalid","Please Speak Clearly")
def voice_recorder1():#sign-in p
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.record(source,duration=5)
        try:
            p.set(r.recognize_google(audio))
        except Exception as e:
            messagebox.showinfo("Invalid","Please Speak Clearly")
def voice_recorder2():#profile
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.record(source,duration=5)
        try:
            a.set(r.recognize_google(audio))
        except Exception as e:
            messagebox.showinfo("Invalid","Please Speak Clearly")
def search():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.record(source,duration=5)
        try:
            searching.set(r.recognize_google(audio))
        except Exception as e:
            messagebox.showinfo("Invalid","Please Speak Clearly")
        if searching.get()=="Yeh Jawaani Hai Deewani":
             webbrowser.open("https://www.primevideo.com/detail/0NU7MBRU958PX2QUTM0F3GG5TP/ref=atv_hm_hom_c_DaEPNJ_brws_11_6")
        elif searching.get()=="The Family Man" or "the family man":
            webbrowser.open("https://www.primevideo.com/detail/0S3QYI59BAEI5KVLHCKSR91YGD/ref=atv_hm_hom_c_dfByPd_3_6")
        else:
            messagebox.showinfo("POPUP","Sorry Unavailable!!!")
#*************************SIGN IN WINDOW************************************************************************
def sign_in():
    if email.get()=="" or passw.get()=="":
        messagebox.showinfo("Try Again","This Field Is Compulsory")
    else :
        top=Toplevel()
        top.title("PRIME VIDEO SIGN-IN")
        top.geometry("500x600")
        top.configure(background="#333333")
        frame=Frame(top,width=350,height=400,bg="white",highlightbackground="red",highlightthickness="3")
        frame.place(x=75,y=125)
        #LABELS
        amazon=Label(top,text="amazon",font=("arial",30,"bold"),borderwidth=0,bg="#333333",fg="white").place(x=155,y=32)
        primevideo=Label(top,text="prime video",font=("arial",25,"bold"),borderwidth=0,bg="#333333",fg="white").place(x=190,y=69)
        signin=Label(frame,text="Sign-In",font=("arial",20,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=20)
        username=Label(frame,text="Username",font=("arial",16,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=70)
        password=Label(frame,text="Password",font=("arial",16,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=140)
        new=Label(frame,text="New To Amazon?",font=("arial",10,"bold"),borderwidth=0,bg="white",fg="black").place(x=110,y=270)
        #ENTRIES
        user=Entry(frame,textvariable=u,width=45,highlightthickness="3").place(x=20,y=100)
        pas=Entry(frame,textvariable=p,width=45,highlightthickness="3").place(x=20,y=170)
        username=email.get()
        password=passw.get()
        #BUTTONS
        signin=Button(frame,text="Sign In",width=34,command=profile,font=("arial",10,"bold"),highlightbackground="black",highlightthickness="3",borderwidth=0,bg="#e6e600",fg="black",relief="sunken").place(x=20,y=220)
        signup=Button(frame,text="Create Your Amazon Account",width=34,command=sign_up,font=("arial",10,"bold"),highlightbackground="black",highlightthickness="3",borderwidth=0,bg="grey",fg="black",relief="sunken").place(x=20,y=310)
        mycursor.execute("insert into signup values('"+username+"','"+password+"')")
        mydb.commit()
#**********************************SIGN UP WINDOW*********************************************************************
def sign_up():
    top=Toplevel()
    top.title("PRIME VIDEO SIGN-UP")
    top.geometry("500x600")
    top.configure(background="#333333")
    frame=Frame(top,width=350,height=400,bg="white",highlightbackground="red",highlightthickness="3")
    frame.place(x=75,y=125)
    #LABELS
    amazon=Label(top,text="amazon",font=("arial",30,"bold"),borderwidth=0,bg="#333333",fg="white").place(x=155,y=32)
    primevideo=Label(top,text="prime video",font=("arial",25,"bold"),borderwidth=0,bg="#333333",fg="white").place(x=190,y=69)
    signin=Label(frame,text="Sign-Up",font=("arial",20,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=20)
    username=Label(frame,text="Username",font=("arial",16,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=70)
    password=Label(frame,text="Password",font=("arial",16,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=140)
    new=Label(frame,text="Already a Member?",font=("arial",10,"bold"),borderwidth=0,bg="white",fg="black").place(x=110,y=270)
    #ENTRIES
    global email
    email=StringVar()
    global passw
    passw=StringVar()
    user=Entry(frame,textvariable=email,width=45,highlightthickness="3")
    user.place(x=20,y=100)
    pas=Entry(frame,textvariable=passw,width=45,highlightthickness="3")
    pas.place(x=20,y=170)
    #BUTTONS
    signup=Button(frame,text="Sign Up",width=34,command=sign_in,font=("arial",10,"bold"),highlightbackground="black",highlightthickness="3",borderwidth=0,bg="#e6e600",fg="black",relief="sunken").place(x=20,y=220)
    signin=Button(frame,text="Sign In To Amazon",width=34,command=sign_in,font=("arial",10,"bold"),highlightbackground="black",highlightthickness="3",borderwidth=0,bg="grey",fg="black",relief="sunken").place(x=20,y=310)
#**********************************PROFILES***************************************************************************
def profile():
    messagebox.showinfo("","Welcome"+" "+u.get())
    top=Toplevel()
    top.title("AMAZON PRIME VIDEO-PROFLES")
    top.geometry("1920x1080")
    top.configure(background="#333333")
    prime=Label(top,text="prime video",fg="white",bg="#333333",borderwidth=0,font=("arial",16,"bold")).place(x=15,y=10)
    prof=Label(top,text="Hello "+" "+u.get(),bg="#333333",fg="white",font=("arial",15,"bold"))
    prof.place(x=1300,y=10)
    l=Label(top,text="Who's Watching ?",fg="white",bg="#333333",borderwidth=0,font=("arial",24,"bold")).place(x=630,y=75)
    global name
    global e
    global profile_name
    global voice2
    name=Label(top,text="Enter Your Name",fg="white",bg="#333333",borderwidth=0,font=("arial",16,"bold"))
    name.place(x=540,y=320)
    voice2=Button(top,image=google,command=voice_recorder2,borderwidth=0)
    voice2.place(x=870,y=320)
    profile_name=StringVar()
    e=Entry(top,textvariable=profile_name)
    e.place(x=730,y=320)
    professor=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\professor.png")
    harvey=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\harvey.png")
    rachel=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\rachelzane.png")
    mike=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\mikeross.png")
    #tokyo=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\tokyo.png")
    smiley=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\smiley.png")
    global smileyb
    global professorb
    global harveyb
    global rachelb
    global mikeb
    global smileydb
    def hi():
        #professorb.config(state=ACTIVE)
        harveyb.config(state=ACTIVE)
        rachelb.config(state=ACTIVE)
        mikeb.config(state=ACTIVE)
        smileydb.config(state=ACTIVE)
        save.config(state=ACTIVE)
        edit.destroy()
        #tokyob.config(state=ACTIVE)
    def save():
        name.destroy()
        e.destroy()
        harveyb.destroy()
        rachelb.destroy()
        mikeb.destroy()
        smileydb.destroy()
        save.destroy()
        voice2.destroy()
        b=profile_name.get()
        d=Label(top,text=b,bg="#333333",fg="white",font=("arial",20,"bold"))
        d.place(x=710,y=320)
    def smileyc():
        smileyb.config(image=smiley)
    #def professorc():
     #   smileyb.config(image=professor)
    def harveyc():
        smileyb.config(image=harvey)
    def rachelc():
        smileyb.config(image=rachel)
    def mikec():
        smileyb.config(image=mike)
    #def tokyoc():
        #smileyb.config(image=tokyo)
    global smileyb
    global professorb
    global harveyb
    global rachelb
    global mikeb
    #global tokyob
    smileyb=Button(top,image=smiley,command=click,borderwidth=0)#main profile
    smileyb.place(x=630,y=150)
    smileydb=Button(top,image=smiley,command=smileyc,state=DISABLED,borderwidth=0)
    smileydb.place(x=10,y=380)
    #professor=Button(top,image=professor,command=professorc,borderwidth=0,state=DISABLED)
    #professor.place(x=10,y=380)
    harveyb=Button(top,image=harvey,command=harveyc,borderwidth=0,state=DISABLED)
    harveyb.place(x=310,y=380)
    rachelb=Button(top,image=rachel,command=rachelc,borderwidth=0,state=DISABLED)
    rachelb.place(x=610,y=380)
    mikeb=Button(top,image=mike,command=mikec,borderwidth=0,state=DISABLED)
    mikeb.place(x=910,y=380)
    #tokyob=Button(top,image=tokyo,borderwidth=0,state=DISABLED)
    #tokyob.place(x=1210,y=625)
    edit=Button(top,text="Edit",command=hi,font=("arial",20,"bold"),borderwidth=0,bg="#333333",fg="white")
    edit.place(x=700,y=620)
    save=Button(top,text="Save",command=save,font=("arial",20,"bold"),borderwidth=0,state=DISABLED,bg="#333333",fg="white")
    save.place(x=850,y=620)
    '''username=u.get()
    prof_name=profile_name.get()
    '''
    top.mainloop()
#**********************************HOME PAGE**************************************************************************
def click():
    top=Toplevel()
    top.title("AMAZON PRIME VIDEO")
    top.geometry("1920x1080")
    top.configure(background="#333333")
    f=profile_name.get()
    g=Label(top,text="Hello "+f,bg="#333333",fg="white",font=("arial",15,"bold"))
    g.place(x=1300,y=10)
    global searching
    def hotshots():
        mycursor.execute("use sgp")
        mycursor.execute(" select movie_name from recommendation order by movie_count desc limit 5")
        ld=mycursor.fetchall()
        output=""
        for x in ld:
            output +=x[0]+"\n"+"\n"
        hotshot=Label(top,bg="#333333",text=output,fg="yellow",font=("arial",10,"bold"),bd=0)
        hotshot.place(x=15,y=105)
        mydb.commit()
    hotshots()
#*********************************TIME********************************************************************************
    localtime=time.asctime(time.localtime(time.time()))
    timel=Label(top,font=('arial',15,'bold'),text=localtime,bg="#333333",fg="white",bd=10,anchor='w').place(x=1000,y=10)
#*********************************IMAGE SLIDER************************************************************************
    class Sliding_Image:
        def __init__(self,top):
            self.top=top
            self.image1=ImageTk.PhotoImage(file="bigbang.png")
            self.image2=ImageTk.PhotoImage(file="goodnewz.png")
            self.image3=ImageTk.PhotoImage(file="jackryan.png")
            self.image4=ImageTk.PhotoImage(file="ie.png")
            frame=Frame(self.top)
            frame.place(x=225,y=80,width=1041,height=210)
            self.l1=Button(frame,image=self.image1,bd=0)
            self.l1.place(x=0,y=0)
            self.l2=Button(frame,image=self.image2,bd=0)
            self.l2.place(x=1041,y=0)
            self.x=1041
            self.slider_func()
        def slider_func(self):
            self.x-=1
            if self.x==0:
                self.x=1041
                time.sleep(2)
                self.new_im=self.image1
                self.image1=self.image2
                self.image2=self.image3
                self.image3=self.image4
                self.image4=self.new_im
                self.l1.config(image=self.image1)
                self.l2.config(image=self.image2)
            self.l2.place(x=self.x,y=0)
            self.l2.after(1,self.slider_func)
    obj=Sliding_Image(top)
    # LABELS
    amazonorignals=Label(top,text="AMAZON ORIGNALS",fg="white",bg="#333333",font=("arial",10,"bold")).place(x=15,y=300)
    moviesinhindi=Label(top,text="MOVIES IN HINDI",fg="white",bg="#333333",font=("arial",10,"bold")).place(x=15,y=550)
    # ICONS
    back=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\back.png")
    amazonprime=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\amazonprime.png")
    familyman=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\familyman.png")
    breathe=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\breathe.png")
    insideedge=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\insideedge.png")
    mirzapur=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\mirzapur.png")
    patallok=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\patallok.png")
    yjhd=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\yjhd.png")
    znmd=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\znmd.png")
    sktks=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\sktks.png")
    dch=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\dilchatahai.png")
    kkhh=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\kkhh.png")
    familymaninfo=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\fminfo.png")
    breathinfo=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\binfo.png")
    insideedgeinfo=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\ieinfo.png")
    mirzapurinfo=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\minfo.png")
    patallokinfo=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\plinfo.png")
    fmr=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\fmr.png")
    plr=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\plr.png")
    mr=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\mr.png")
    ier=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\ier.png")
    # IMAGE FUNC
    def amazon():
        webbrowser.open("https://www.primevideo.com/storefront/home/ref=atv_nb_logo")
    def family():
        webbrowser.open("https://www.primevideo.com/detail/0S3QYI59BAEI5KVLHCKSR91YGD/ref=atv_hm_hom_c_dfByPd_3_6")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5115")
        mydb.commit()
    def breath():
        webbrowser.open("https://www.primevideo.com/detail/0TRG6QSFTYWRDB885FMYJOJO9X/ref=atv_hm_hom_c_dfByPd_3_5")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5116")
        mydb.commit()
    def edge():
        webbrowser.open("https://www.primevideo.com/detail/0PDN3DS1B1DWPHDVZ6MTAW1XE9/ref=atv_dp_season_select_s1")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5117")
        mydb.commit()
    def mirza():
        webbrowser.open("https://www.primevideo.com/detail/0PDOKMV9CRLOMO5EUKNCUJLG4Q/ref=atv_hm_hom_c_dfByPd_3_4")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5118")
        mydb.commit()
    def patal():
        webbrowser.open("https://www.primevideo.com/detail/0G9IEOHCN8KMY6COD9ILGH7IY5/ref=atv_hm_hom_c_dfByPd_3_9")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5119")
        mydb.commit()
    def yeh():
        webbrowser.open("https://www.primevideo.com/detail/0NU7MBRU958PX2QUTM0F3GG5TP/ref=atv_hm_hom_c_DaEPNJ_brws_11_6")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5120")
        mydb.commit()
    def zindagi():
        webbrowser.open("https://www.primevideo.com/detail/0TZV1UJ71TP46I86TZZ50HUJMW/ref=atv_hm_hom_c_DaEPNJ_brws_11_4")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5121")
        mydb.commit()
    def ke():
        webbrowser.open("https://www.primevideo.com/detail/0N0EXSVCF16I1DIFSE16VHEXM0/ref=atv_hm_hom_c_DaEPNJ_brws_11_8")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5122")
        mydb.commit()
    def dil():
        webbrowser.open("https://www.primevideo.com/detail/0GUPSYRY1MTBUBAJMLTKNYIC7E/ref=atv_hm_hom_c_DaEPNJ_brws_11_3")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5123")
        mydb.commit()
    def kuch():
        webbrowser.open("https://www.primevideo.com/detail/0S7X9EIS7SOF8MX3258XNFTXAA/ref=atv_hm_hom_c_DaEPNJ_brws_11_21")
        mycursor.execute("update recommendation set movie_count=movie_count+1 where movie_id=5124")
        mydb.commit()
#********************************Meta Data**************************************************************************
#d1=director,c1=cast,g1=genre are used as label variables
#dd1=directordata,cd1=castdata,gd1=genredata used for there respectieve details from csv file
#dl1,cl1,gl1 are used as list variables to print the data from csv file
#infob1 is button used in this frame
#rb is used for movie recommended button
    def fminfo():
        global infob1,d1,c1,g1,dd1,cd1,gd1,backb,fminfol,ierb,mrb,plrb
        fmframe=Frame(top,height=730,width=566,bg="#333333",highlightbackground="yellow",highlightthickness="3")
        fmframe.place(x=500,y=50)
        infob1=Button(top,command=family,image=familymaninfo,borderwidth=0)
        infob1.place(x=502,y=53)
        def back_func():
            fmframe.destroy()
            d1.destroy()
            c1.destroy()
            g1.destroy()
            dd1.destroy()
            cd1.destroy()
            gd1.destroy()
            infob1.destroy()
            backb.destroy()
            fminfol.destroy()
            ierb.destroy()
            mrb.destroy()
            plrb.destroy()
        backb=Button(top,command=back_func,image=back,borderwidth=0)
        backb.place(x=1033,y=53)
        d1=Label(top,text="Directors",bg="#333333",fg="white",font=("arial",15,"bold"))
        d1.place(x=510,y=447)
        c1=Label(top,text="Cast",bg="#333333",fg="white",font=("arial",15,"bold"))
        c1.place(x=510,y=487)
        g1=Label(top,text="Genres",bg="#333333",fg="white",font=("arial",15,"bold"))
        g1.place(x=510,y=527)
        dd1=Label(top,text="")
        dd1.place(x=610,y=447)
        cd1=Label(top,text="")
        cd1.place(x=610,y=487)
        gd1=Label(top,text="")
        gd1.place(x=610,y=527)
        filepath="C:\\Users\\Devarsh\\Desktop\\demo.csv"
        file=open(filepath)
        r=csv.reader(file)
        data=list(r)
        dl3=data[1][3]
        cl3=data[1][1]
        gl3=data[1][2]
        dd1.config(text=dl3,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        cd1.config(text=cl3,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        gd1.config(text=gl3,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        fminfol=Label(top,text="Because You Selected Family Man",borderwidth=0,bg="#333333",font=("arial",15,"bold"),fg="white")
        fminfol.place(x=510,y=637)
        ierb=Button(top,image=ier,borderwidth=0)
        ierb.place(x=503,y=673)
        mrb=Button(top,image=mr,borderwidth=0)
        mrb.place(x=690,y=673)
        plrb=Button(top,image=plr,borderwidth=0)
        plrb.place(x=880,y=673)
    def binfo():
        global infob2,d2,c2,g2,dd2,cd2,gd2,backb,binfol,ierb,mrb,plrb
        bframe=Frame(top,height=730,width=566,bg="#333333",highlightbackground="yellow",highlightthickness="3")
        bframe.place(x=500,y=50)
        infob2=Button(top,command=breath,image=breathinfo,borderwidth=0)
        infob2.place(x=502,y=53)
        def back_func():
            bframe.destroy()
            d2.destroy()
            c2.destroy()
            g2.destroy()
            dd2.destroy()
            cd2.destroy()
            gd2.destroy()
            infob2.destroy()
            backb.destroy()
            binfol.destroy()
            ierb.destroy()
            mrb.destroy()
            plrb.destroy()
        backb=Button(top,command=back_func,image=back,borderwidth=0)
        backb.place(x=1033,y=53)
        d2=Label(top,text="Directors",bg="#333333",fg="white",font=("arial",15,"bold"))
        d2.place(x=510,y=467)
        c2=Label(top,text="Cast",bg="#333333",fg="white",font=("arial",15,"bold"))
        c2.place(x=510,y=507)
        g2=Label(top,text="Genres",bg="#333333",fg="white",font=("arial",15,"bold"))
        g2.place(x=510,y=547)
        dd2=Label(top,text="")
        dd2.place(x=610,y=467)
        cd2=Label(top,text="")
        cd2.place(x=610,y=507)
        gd2=Label(top,text="")
        gd2.place(x=610,y=547)
        filepath="C:\\Users\\Devarsh\\Desktop\\demo.csv"
        file=open(filepath)
        r=csv.reader(file)
        data=list(r)
        dl2=data[2][3]
        cl2=data[2][1]
        gl2=data[2][2]
        dd2.config(text=dl2,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        cd2.config(text=cl2,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        gd2.config(text=gl2,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        binfol=Label(top,text="Because You Selected Breath",borderwidth=0,bg="#333333",font=("arial",15,"bold"),fg="white")
        binfol.place(x=510,y=637)
        ierb=Button(top,image=ier,borderwidth=0)
        ierb.place(x=503,y=673)
        mrb=Button(top,image=mr,borderwidth=0)
        mrb.place(x=690,y=673)
        plrb=Button(top,image=plr,borderwidth=0)
        plrb.place(x=880,y=673)
    def ieinfo():
        global infob3,d3,c3,g3,dd3,cd3,gd3,backb,ieinfol,fmrb,mrb,plrb
        ieframe=Frame(top,height=730,width=566,bg="#333333",highlightbackground="yellow",highlightthickness="3")
        ieframe.place(x=500,y=50)
        infob3=Button(top,command=edge,image=insideedgeinfo,borderwidth=0)
        infob3.place(x=502,y=53)
        def back_func():
            ieframe.destroy()
            d3.destroy()
            c3.destroy()
            g3.destroy()
            dd3.destroy()
            cd3.destroy()
            gd3.destroy()
            infob3.destroy()
            backb.destroy()
            ieinfol.destroy()
            fmrb.destroy()
            mrb.destroy()
            plrb.destroy()
        backb=Button(top,command=back_func,image=back,borderwidth=0)
        backb.place(x=1033,y=53)
        d3=Label(top,text="Directors",bg="#333333",fg="white",font=("arial",15,"bold"))
        d3.place(x=510,y=507)
        c3=Label(top,text="Cast",bg="#333333",fg="white",font=("arial",15,"bold"))
        c3.place(x=510,y=547)
        g3=Label(top,text="Genres",bg="#333333",fg="white",font=("arial",15,"bold"))
        g3.place(x=510,y=587)
        dd3=Label(top,text="")
        dd3.place(x=610,y=507)
        cd3=Label(top,text="")
        cd3.place(x=610,y=547)
        gd3=Label(top,text="")
        gd3.place(x=610,y=587)
        filepath="C:\\Users\\Devarsh\\Desktop\\demo.csv"
        file=open(filepath)
        r=csv.reader(file)
        data=list(r)
        dl3=data[3][3]
        cl3=data[3][1]
        gl3=data[3][2]
        dd3.config(text=dl3,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        cd3.config(text=cl3,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        gd3.config(text=gl3,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        ieinfol=Label(top,text="Because You Selected Inside Edge",borderwidth=0,bg="#333333",font=("arial",15,"bold"),fg="white")
        ieinfol.place(x=510,y=637)
        fmrb=Button(top,image=fmr,borderwidth=0)
        fmrb.place(x=503,y=673)
        mrb=Button(top,image=mr,borderwidth=0)
        mrb.place(x=690,y=673)
        plrb=Button(top,image=plr,borderwidth=0)
        plrb.place(x=880,y=673)
    def minfo():
        global infob4,d4,c4,g4,dd4,cd4,gd4,backb,minfol,ierb,fmrb,plrb
        mframe=Frame(top,height=730,width=566,bg="#333333",highlightbackground="yellow",highlightthickness="3")
        mframe.place(x=500,y=50)
        infob1=Button(top,command=mirza,image=mirzapurinfo,borderwidth=0)
        infob1.place(x=502,y=53)
        def back_func():
            mframe.destroy()
            d4.destroy()
            c4.destroy()
            g4.destroy()
            dd4.destroy()
            cd4.destroy()
            gd4.destroy()
            infob1.destroy()
            backb.destroy()
            minfol.destroy()
            ierb.destroy()
            fmrb.destroy()
            plrb.destroy()
        backb=Button(top,command=back_func,image=back,borderwidth=0)
        backb.place(x=1033,y=53)
        d4=Label(top,text="Directors",bg="#333333",fg="white",font=("arial",15,"bold"))
        d4.place(x=510,y=467)
        c4=Label(top,text="Cast",bg="#333333",fg="white",font=("arial",15,"bold"))
        c4.place(x=510,y=507)
        g4=Label(top,text="Genres",bg="#333333",fg="white",font=("arial",15,"bold"))
        g4.place(x=510,y=547)
        dd4=Label(top,text="")
        dd4.place(x=610,y=467)
        cd4=Label(top,text="")
        cd4.place(x=610,y=507)
        gd4=Label(top,text="")
        gd4.place(x=610,y=547)
        filepath="C:\\Users\\Devarsh\\Desktop\\demo.csv"
        file=open(filepath)
        r=csv.reader(file)
        data=list(r)
        dl4=data[4][3]
        cl4=data[4][1]
        gl4=data[4][2]
        dd4.config(text=dl4,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        cd4.config(text=cl4,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        gd4.config(text=gl4,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        minfol=Label(top,text="Because You Selected Mirzapur",borderwidth=0,bg="#333333",font=("arial",15,"bold"),fg="white")
        minfol.place(x=510,y=637)
        ierb=Button(top,image=ier,borderwidth=0)
        ierb.place(x=503,y=673)
        fmrb=Button(top,image=fmr,borderwidth=0)
        fmrb.place(x=690,y=673)
        plrb=Button(top,image=plr,borderwidth=0)
        plrb.place(x=880,y=673)
    def plinfo():
        global infob5,d5,c5,g5,dd5,cd5,gd5,backb,plinfol,ierb,mrb,plrb
        plframe=Frame(top,height=730,width=566,bg="#333333",highlightbackground="yellow",highlightthickness="3")
        plframe.place(x=500,y=50)
        infob1=Button(top,command=patal,image=patallokinfo,borderwidth=0)
        infob1.place(x=502,y=53)
        def back_func():
            plframe.destroy()
            d5.destroy()
            c5.destroy()
            g5.destroy()
            dd5.destroy()
            cd5.destroy()
            gd5.destroy()
            infob1.destroy()
            backb.destroy()
            plinfol.destroy()
            ierb.destroy()
            mrb.destroy()
            fmrb.destroy()
        backb=Button(top,command=back_func,image=back,borderwidth=0)
        backb.place(x=1033,y=53)
        d5=Label(top,text="Directors",bg="#333333",fg="white",font=("arial",15,"bold"))
        d5.place(x=510,y=467)
        c5=Label(top,text="Cast",bg="#333333",fg="white",font=("arial",15,"bold"))
        c5.place(x=510,y=507)
        g5=Label(top,text="Genres",bg="#333333",fg="white",font=("arial",15,"bold"))
        g5.place(x=510,y=547)
        dd5=Label(top,text="")
        dd5.place(x=610,y=467)
        cd5=Label(top,text="")
        cd5.place(x=610,y=507)
        gd5=Label(top,text="")
        gd5.place(x=610,y=547)
        filepath="C:\\Users\\Devarsh\\Desktop\\demo.csv"
        file=open(filepath)
        r=csv.reader(file)
        data=list(r)
        dl5=data[5][3]
        cl5=data[5][1]
        gl5=data[5][2]
        dd5.config(text=dl5,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        cd5.config(text=cl5,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        gd5.config(text=gl5,bg="#333333",fg="#b3ffff",font=("arial",15,"bold"))
        plinfol=Label(top,text="Because You Selected Patal Lok",borderwidth=0,bg="#333333",font=("arial",15,"bold"),fg="white")
        plinfol.place(x=510,y=637)
        ierb=Button(top,image=ier,borderwidth=0)
        ierb.place(x=503,y=673)
        mrb=Button(top,image=mr,borderwidth=0)
        mrb.place(x=690,y=673)
        fmrb=Button(top,image=fmr,borderwidth=0)
        fmrb.place(x=880,y=673)
#*********************************Graph Functions*********************************************************************
    def indianseries():
        mycursor.execute("use sgp")
        mycursor.execute(" select movie_count from recommendation")
        graph=mycursor.fetchall()
        output=""
        for x in graph:
            fmv=str(graph[0])
            bv=str(graph[1])
            iev=str(graph[2])
            mv=str(graph[3])
            plv=str(graph[4])
            yjhdv=str(graph[5])
            znmdv=str(graph[6])
            sktksv=str(graph[7])
            dchv=str(graph[8])
            kkhhv=str(graph[9])
        series=["Family Man","Breathe","Indside Edge","Mirzapur","Patallok","Yeh Jawaani Hai Deewani","Zindagi Na Milegi Doobara","Sonu Ke Titu Ki Sweetu","Dil Chahta Hai","Kuch Kuch Hota Hai"]
        views=[fmv,bv,iev,mv,plv,yjhdv,znmdv,sktksv,dchv,kkhhv]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
        mydb.commit()
    def romance():
        series=["Hum Tum","Raabta","Love Yatri","Mohabbatein","Notebook","Kalank","Padmaavat","Marjaavaan","Ok Jaanu","Salaam Namaste"]
        views=[9000,12000,7530,6400,3120,5067,4056,1200,2455,14500]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
    def thriller():
        series=["Jack Ryan","Raazi","Supernatural","Dont Breathe","Vodka Diaries","IT","Wazir","Anacondas","New York","Tumbbad"]
        views=[1789,997,2000,953,780,500,457,2090,1310,700]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
    def indianmovies():
        series=["Gold","Batla House","Befikre","Newton","Raaz","Race","2 States","Golmaal","Gully Boy","Bewakoofiyaan"]
        views=[11895,5567,4000,6783,5500,2000,10457,3209,7102,8500]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
    def americanseries():
        series=["The Office","Shameless","Suits","Supernatural","Boyfriend Experience","Blindspot","Two And A Half Men","2 Broke Girls","Dexter","Chuck"]
        views=[17895,3467,27707,16453,15500,24355,12457,7209,2102,7500]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
    def americanmovies():
        series=["Stuart Little","Spider Man","The Godfather","Fantastic Beasts","The Conjuring","Jumanji","Kung Fu Panda","Bad Boys","Parasite","Batman Begins"]
        views=[5005,12467,14000,26743,1550,12000,4047,7289,17102,5890]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
    def comedy():
        series=["Double Dhamaal","Hera Pheri","Comicstaan","Rasbhari","Phir Hera Pheri","Welcome","PagalPanti","Thank You","Fukrey","Munna Bhai MBBS"]
        views=[4733,11367,6769,3243,30376,24815,3757,7081,6504,15140]
        explode=(0.1,0,0,0,0,0,0,0,0,0)
        fig1,ax1=plt.subplots()
        ax1.pie(views, explode=explode, labels=series, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
        ax1.axis('equal')
        plt.show()
#*********************************Icon Functions********************************************************************** 
    def ten():
        top=Toplevel()
        top.title("AMAZON-TOP 10")
        top.geometry("500x600")
        top.configure(background="#333333")
        frame=Frame(top,width=350,height=400,bg="white",highlightbackground="red",highlightthickness="3")
        frame.place(x=75,y=125)
        indianseriesb=Button(frame,text="Indian Series",borderwidth=0,bg="white",font=("arial",15,"bold"),fg="black",command=indianseries).place(x=100,y=50)
        romanceb=Button(frame,text="Romance",borderwidth=0,fg="black",bg="white",font=("arial",15,"bold"),command=romance).place(x=100,y=90)
        thrillerb=Button(frame,text="Thriller",borderwidth=0,fg="black",bg="white",font=("arial",15,"bold"),command=thriller).place(x=100,y=130)
        indianmoviesb=Button(frame,text="Indian Movies",borderwidth=0,fg="black",bg="white",font=("arial",15,"bold"),command=indianmovies).place(x=100,y=170)
        americanseriesb=Button(frame,text="American Series",borderwidth=0,fg="black",bg="white",font=("arial",15,"bold"),command=americanseries).place(x=100,y=210)
        americanmoviesb=Button(frame,text="American Movies",borderwidth=0,fg="black",bg="white",font=("arial",15,"bold"),command=americanmovies).place(x=100,y=250)
        comedyb=Button(frame,text="Comedy",borderwidth=0,fg="black",bg="white",font=("arial",15,"bold"),command=comedy).place(x=100,y=290)
        top.mainloop()
#*******************************Buttons for prime page****************************************************************
    primelogob=Button(top,text="prime video",borderwidth=0,bg="#333333",font=("arial",15,"bold"),fg="white",command=amazon).place(x=15,y=10)
    homeb=Button(top,text="Home",borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold"),command=amazon).place(x=200,y=10)
    tvshowsb=Button(top,text="TV Shows",borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold"),command=amazon).place(x=270,y=10)
    moviesb=Button(top,text="Movies",borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold"),command=amazon).place(x=380,y=10)
    kidsb=Button(top,text="Kids",borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold"),command=amazon).place(x=465,y=10)
    topb=Button(top,text="Top 10",borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold"),command=ten).place(x=525,y=10)
    likedb=Button(top,text="Most Liked",borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold"),command=amazon).place(x=610,y=10)
    searchb=Button(top,text="Search",command=search,borderwidth=0,bg="#333333",fg="white",font=("arial",15,"bold")).place(x=735,y=10)
    global searching
    searching=StringVar()
    searched=Entry(top,textvariable=searching)
    searched.place(x=830,y=20)
    hotshotsb=Button(top,fg="white",bg="#333333",command=hotshots,borderwidth=0,text="Most Viewed",font=("arial",15,"bold"))
    hotshotsb.place(x=40,y=60)
    familyb=Button(top,image=familyman,borderwidth=0,command=fminfo).place(x=15,y=325)
    breatheb=Button(top,image=breathe,borderwidth=0,command=binfo).place(x=400,y=325)
    edgeb=Button(top,image=insideedge,borderwidth=0,command=ieinfo).place(x=745,y=325)
    mirzapurb=Button(top,image=mirzapur,borderwidth=0,command=minfo).place(x=1050,y=325)
    patalb=Button(top,image=patallok,borderwidth=0,command=plinfo).place(x=1300,y=325)
    yjhdb=Button(top,image=yjhd,borderwidth=0,command=yeh).place(x=15,y=575)
    sktksb=Button(top,image=sktks,borderwidth=0,command=ke).place(x=400,y=575)
    znmdb=Button(top,image=znmd,borderwidth=0,command=zindagi).place(x=775,y=575)
    dchb=Button(top,image=dch,borderwidth=0,command=dil).place(x=1050,y=575)
    kkhhb=Button(top,image=kkhh,borderwidth=0,command=kuch).place(x=1300,y=575)
    top.mainloop()
top=Tk()
top.title("PRIME VIDEO SIGN-IN")
top.geometry("500x600")
top.configure(background="#333333")
frame=Frame(top,width=350,height=400,bg="white",highlightbackground="red",highlightthickness="3")
frame.place(x=75,y=125)
google=PhotoImage(file="C:\\Users\\Devarsh\\Desktop\\SGP\\voice.png")
global p
p=StringVar()
global u
u=StringVar()
#LABELS
amazon=Label(top,text="amazon",font=("arial",30,"bold"),borderwidth=0,bg="#333333",fg="white").place(x=155,y=32)
primevideo=Label(top,text="prime video",font=("arial",25,"bold"),borderwidth=0,bg="#333333",fg="white").place(x=190,y=69)
signin=Label(frame,text="Sign-In",font=("arial",20,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=20)
username=Label(frame,text="Username",font=("arial",16,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=70)
password=Label(frame,text="Password",font=("arial",16,"bold"),borderwidth=0,bg="white",fg="black").place(x=20,y=140)
new=Label(frame,text="New To Amazon?",font=("arial",10,"bold"),borderwidth=0,bg="white",fg="black").place(x=110,y=270)
#ENTRIES
user=Entry(frame,textvariable=u,width=45,highlightthickness="3").place(x=20,y=100)
pas=Entry(frame,textvariable=p,width=45,highlightthickness="3").place(x=20,y=170)
#BUTTONS
signin=Button(frame,text="Sign In",width=34,command=profile,font=("arial",10,"bold"),highlightbackground="black",highlightthickness="3",borderwidth=0,bg="#e6e600",fg="black",relief="sunken").place(x=20,y=220)
signup=Button(frame,text="Create Your Amazon Account",width=34,command=sign_up,font=("arial",10,"bold"),highlightbackground="black",highlightthickness="3",borderwidth=0,bg="grey",fg="black",relief="sunken").place(x=20,y=310)
voice=Button(frame,image=google,command=voice_recorder,borderwidth=0).place(x=278,y=100)
voice1=Button(frame,image=google,command=voice_recorder1,borderwidth=0).place(x=278,y=170)
top.mainloop()

