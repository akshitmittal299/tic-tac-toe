from tkinter import *
from tkinter import messagebox
import random
class demo:

    def __init__(self,p1,p2,a,b):
        self.a_score=a
        self.b_score=b
        print(self.a_score)
        self.m=["","","","","","","","",""]
        self.count=1
        self.a=p1
        self.b=p2
        self.root=Tk()
        self.root.config(background="#FFFFCC")
        self.root.state('zoomed')
        self.l1=Label(self.root,text="TIC TAC TOE",)
        self.l1.config(background="#FFFFCC",font=("Times New Roman",35))
        self.l1.place(relx=0.4,rely=0.03)
        self.c1=Canvas(self.root)
        self.c1.place(relx=0.35,rely=0.15)
        self.c1.config(width=450, height=450,background="black")
        line1=self.c1.create_line(150,0,150,500,fill="white")
        line1=self.c1.create_line(300,0,300,500,fill="white")
        line1=self.c1.create_line(0,150,450,150,fill="white")
        line1=self.c1.create_line(0,300,450,300,fill="white")
        self.c1.bind('<1>',self.call)

        self.l2=Label(self.root)
        self.l2.config(text="PLAYER 1:  "+ self.a,background="#FFFFCC",font=("Times New Roman",25))
        self.l2.place(relx=0.1,rely=0.1)

        self.l3=Label(self.root,text=self.a +":"+str(self.a_score))
        self.l3.config(background="#FFFFCC",font=("Times New Roman",25))
        self.l3.place(relx=0.8,rely=0.2)

        self.l4=Label(self.root,text=self.b +":"+str(self.b_score))
        self.l4.config(background="#FFFFCC",font=("Times New Roman",25))
        self.l4.place(relx=0.8,rely=0.3)
        
        self.l3=Label(self.root)
        self.l3.config(text="PLAYER 2:  "+ self.b,background="#FFFFCC",font=("Times New Roman",25))
        self.l3.place(relx=0.1,rely=0.2)
        self.root.mainloop()
    def call(self,evt):
        
        x=evt.x
        y=evt.y
        if(self.count%2!=0):
            
            if(x>0 and x<150 and y>0 and y<150):
                self.m[0]="1"
                print(self.m)
                self.c1.create_line(10,10,140,140,fill="white",width=4)
                self.c1.create_line(140,10,10,140,fill="white",width=4)
            elif(x>150 and x<300 and y>0 and y<150):
                self.m[1]="1"
                print(self.m)
                self.c1.create_line(160,10,290,140,fill="white",width=4)
                self.c1.create_line(290,10,160,140,fill="white",width=4)
            elif(x>300 and x<450 and y>0 and y<150):
                self.m[2]="1"
                print(self.m)
                self.c1.create_line(310,10,440,140,fill="white",width=4)
                self.c1.create_line(440,10,310,140,fill="white",width=4)
            elif(x>0 and x<150 and y>150 and y<300):
                self.m[3]="1"
                print(self.m)
                self.c1.create_line(10,160,140,290,fill="white",width=4)
                self.c1.create_line(140,160,10,290,fill="white",width=4)
            elif(x>0 and x<150 and y>300 and y<450):
                self.m[6]="1"
                print(self.m)
                self.c1.create_line(10,310,140,440,fill="white",width=4)
                self.c1.create_line(140,310,10,440,fill="white",width=4)
            elif(x>150 and x<300 and y>150 and y<300):
                self.m[4]="1"
                print(self.m)
                self.c1.create_line(160,160,290,290,fill="white",width=4)
                self.c1.create_line(290,160,160,290,fill="white",width=4)
            elif(x>150 and x<300 and y>300 and y<450):
                self.m[7]="1"
                print(self.m)
                self.c1.create_line(160,310,290,440,fill="white",width=4)
                self.c1.create_line(290,310,160,440,fill="white",width=4)
            elif(x>300 and x<450 and y>150 and y<300):
                self.m[5]="1"
                print(self.m)
                self.c1.create_line(310,160,440,290,fill="white",width=4)
                self.c1.create_line(440,160,310,290,fill="white",width=4)
            elif(x>300 and x<450 and y>300 and y<450):
                self.m[8]="1"
                print(self.m)
                self.c1.create_line(310,310,440,440,fill="white",width=4)
                self.c1.create_line(440,310,310,440,fill="white",width=4)
            self.count=self.count+1
            if ( self.m[0]==self.m[1]==self.m[2]=="1" or self.m[0]==self.m[3]==self.m[6]=="1" or self.m[0]==self.m[4]==self.m[8]=="1" or self.m[1]==self.m[4]==self.m[7]=="1" or self.m[2]==self.m[4]==self.m[6]=="1" or self.m[2]==self.m[5]==self.m[8]=="1" or self.m[3]==self.m[4]==self.m[5]=="1" or self.m[6]==self.m[7]==self.m[8]=="1" ):
                messagebox.showinfo("validation","player A :"+self.a +" won the game")
                self.a_score=self.a_score+1
                print(self.a_score)
                self.restart()
        else:
            
            if(x>0 and x<150 and y>0 and y<150):
                self.m[0]="0"
                print(self.m)
                self.c1.create_oval(10,10,140,140,fill="black",outline="white",width=4)
                self.c1.create_oval(140,10,10,140,fill="black",outline="white",width=4)
            elif(x>150 and x<300 and y>0 and y<150):
                self.m[1]="0"
                print(self.m)
                self.c1.create_oval(160,10,290,140,fill="black",outline="white",width=4)
                self.c1.create_oval(290,10,160,140,fill="black",outline="white",width=4)
            elif(x>300 and x<450 and y>0 and y<150):
                self.m[2]="0"
                print(self.m)
                self.c1.create_oval(310,10,440,140,fill="black",outline="white",width=4)
                self.c1.create_oval(440,10,310,140,fill="black",outline="white",width=4)
            elif(x>0 and x<150 and y>150 and y<300):
                self.m[3]="0"
                print(self.m)
                self.c1.create_oval(10,160,140,290,fill="black",outline="white",width=4)
                self.c1.create_oval(140,160,10,290,fill="black",outline="white",width=4)
            elif(x>0 and x<150 and y>300 and y<450):
                self.m[6]="0"
                print(self.m)
                self.c1.create_oval(10,310,140,440,fill="black",outline="white",width=4)
                self.c1.create_oval(140,310,10,440,fill="black",outline="white",width=4)
            elif(x>150 and x<300 and y>150 and y<300):
                self.m[4]="0"
                print(self.m)
                self.c1.create_oval(160,160,290,290,fill="black",outline="white",width=4)
                self.c1.create_oval(290,160,160,290,fill="black",outline="white",width=4)
            elif(x>150 and x<300 and y>300 and y<450):
                self.m[7]="0"
                print(self.m)
                self.c1.create_oval(160,310,290,440,fill="black",outline="white",width=4)
                self.c1.create_oval(290,310,160,440,fill="black",outline="white",width=4)
            elif(x>300 and x<450 and y>150 and y<300):
                self.m[5]="0"
                print(self.m)
                self.c1.create_oval(310,160,440,290,fill="black",outline="white",width=4)
                self.c1.create_oval(440,160,310,290,fill="black",outline="white",width=4)
            elif(x>300 and x<450 and y>300 and y<450):
                self.m[8]="0"
                print(self.m)
                self.c1.create_oval(310,310,440,440,fill="black",outline="white",width=4)
                self.c1.create_oval(440,310,310,440,fill="black",outline="white",width=4)
            self.count=self.count+1
            if ( self.m[0]==self.m[1]==self.m[2]=="0" or self.m[0]==self.m[3]==self.m[6]=="0" or self.m[0]==self.m[4]==self.m[8]=="0" or self.m[1]==self.m[4]==self.m[7]=="0" or self.m[2]==self.m[4]==self.m[6]=="0" or self.m[2]==self.m[5]==self.m[8]=="0" or self.m[3]==self.m[4]==self.m[5]=="0" or self.m[6]==self.m[7]==self.m[8]=="0" ):
                messagebox.showinfo("validation","player B :"+self.b+" won the game")
                self.b_score=self.b_score+1
                print(self.b_score)
                self.restart()
        if not(self.m[0]=="" or self.m[1]=="" or self.m[2]=="" or self.m[3]=="" or self.m[4]=="" or self.m[5]==""or self.m[6]==""or self.m[7]==""or self.m[8]==""):
            messagebox.showinfo("DRAW", "GAME DRAW....")
            self.a_score=self.a_score+1
            self.b_score=self.b_score+1
            print(self.a_score,self.b_score)
            self.restart()
            
    def restart(self):
        m=messagebox.askyesno("game","do you wnat a reamatch ?")
        if (m):
            self.root.destroy()
            obj=demo(self.a,self.b,self.a_score,self.b_score)  
        else:
            self.root.destroy()
            self.main=Tk()
            self.main.config(background="#FFFFCC")
            self.main.state('zoomed')
            self.l=Label(self.main,text=self.a+" scored : "+ str(self.a_score))
            self.l.config(background="#FFFFCC",font=("Times New Roman",25))
            self.l.place(relx=0.2,rely=0.2)

            self.l2=Label(self.main,text=self.b+" scored : "+ str(self.b_score))
            self.l2.config(background="#FFFFCC",font=("Times New Roman",25))
            self.l2.place(relx=0.2,rely=0.3)

