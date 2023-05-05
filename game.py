from tkinter import *
from tkinter import messagebox
import new
class game:
    def __init__(self):
        self.root=Tk()
        self.root.config(background="#FFFFCC")
        self.root.state('zoomed')
        self.l1=Label(self.root,text="TIC TAC TOE",)
        self.l1.config(background="#FFFFCC",font=("Times New Roman",35))
        self.l1.place(relx=0.4,rely=0.03)
        self.l2=Label(self.root,text="PLAYER 1 (X):")
        self.l2.config(background="#FFFFCC",font=("Times New Roman",25))
        self.l2.place(relx=0.3,rely=0.15)
        self.l3=Label(self.root,text="PLAYER 2 (O):")
        self.l3.config(background="#FFFFCC",font=("Times New Roman",25))
        self.l3.place(relx=0.3,rely=0.25)
        self.e1=Entry(self.root)
        self.e1.config(font=("Times New Roman",25,"bold"))
        self.e1.place(relx=0.5,rely=0.15)

        self.e2=Entry(self.root)
        self.e2.config(font=("Times New Roman",25,"bold"))
        self.e2.place(relx=0.5,rely=0.25)
        
            

        self.b1=Button(self.root,text="Start",command=self.start)
        self.b1.bind("7",self.start)
        self.b1.config(background="white",font=("Times New Roman",25,"bold"))
        self.b1.place(relx=0.45,rely=0.35)
        self.root.mainloop()
    def start(self):
        if self.e1.get() ==self.e2.get() or self.e1.get()=="" or self.e2.get()=="":
            messagebox.showerror("error", "enter valid player names:")
            self.e1.delete(0,END)
            self.e2.delete(0,END)
        else:
            self.p1=self.e1.get()
            self.p2=self.e2.get()
            self.root.destroy()
            obj=new.demo(self.p1,self.p2,0,0)
obj=game()
