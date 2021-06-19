# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:05:29 2021

@author: Anjolaoluwa
A Simple App to order Pizza
"""

from tkinter import *

class Application (Frame):
    def __init__(self,anjie):
        super(Application,self).__init__(anjie)
        #getting the init() function in frame,the superclass
        #super is a function that takes two parameters: the name of your subclass i.e. Application and self
        self.grid() #allows grid function to work
        self.toppings=["sausage","pepperoni","chicken","mushroom","black olive","green pepper","red pepper","onion"]
        self.prices={"medium":9.99, "large":12.99, "x-large":14.99, "mid-topping":1.0, "large-topping":1.4, "xl-topping":1.8}
        self.checkbox=list(self.toppings)
        self.checkboxVar=list(self.toppings)
        self.create_widgets()
        
    def create_widgets(self):
        menubar=Menu(self)
        filemenu=Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Quit",command=window.quit)
        
        filemenu.add_command(label="Submit",command=self.process)
        
            
        self.label1=Label(self,text="Select size: ")
        self.label1.grid(row=0,column=0,sticky=W)
        self.size=StringVar() #similar to name in html, groups similar elements together with variable self.size
        # print(StringVar())
        
        self.radio1=Radiobutton(self,text="Medium",variable=self.size,value="Medium")
        self.radio1.grid(row=1,column=0,sticky=W)
        self.radio1.select() #makes radio1 the default selected radio button
        
        self.radio2=Radiobutton(self,text="Large",variable=self.size,value="Large")
        self.radio2.grid(row=1,column=1,sticky=W)
        
        
        self.radio3=Radiobutton(self,text="Extra Large",variable=self.size,value="X-Large")
        self.radio3.grid(row=1,column=2,sticky=W)
        
        
        self.label2=Label(self,text="Select size: ")
        self.label2.grid(row=2,column=0,sticky=W)
        
        
        line=2#last row number
        for i in range(len(self.toppings)):
            line+=1
            self.checkboxVar[i]=BooleanVar() #default value added is false
            self.checkbox[i]=Checkbutton(self,text=self.toppings[i], variable=self.checkboxVar[i])
            self.checkbox[i].grid(row=line,column=0,sticky=W)
            
        line+=1
        self.button1=Button(self,text="Reset",command=self.reset)
        self.button1.grid(row=line,column=0,sticky=E)
        self.button2=Button(self,text="Calculate Price",command=self.calculate)
        self.button2.grid(row=line,column=2)
        
        line+=1
        self.label3=Label(self,text="")
        self.label3.grid(row=line,column=0)
        
        line+=1
        self.label4=Label(self,text="Total: ")
        self.label4.grid(row=line,column=0,sticky=E)
        self.result=Entry(self,width=10)
        self.result.grid(row=line,column=1,sticky=W)
        
        window.config(menu=menubar)
        
    def process(self):
        print("This is the process to submit: ")
        
    def reset(self):
        self.radio1.select()
        for i in range(len(self.toppings)):
            self.checkbox[i].deselect()
        self.result.delete(0,END)
        
    def calculate(self):
        self.totalToppings=0
        for i in range(len(self.toppings)):
            if self.checkboxVar[i].get():
                self.totalToppings+=1
                        
            if self.size.get()=="Medium":
                self.price=self.prices["medium"]+(self.totalToppings * self.prices["mid-topping"])
            if self.size.get()=="Large":
                self.price=self.prices["large"]+(self.totalToppings*self.prices["large-topping"])
            if self.size.get()=="X-Large":
                self.price=self.prices["x-large"]+(self.totalToppings*self.prices["xl-topping"])
                
            
            str_price="{:.2f}".format(self.price)
            self.result.delete(0,END)
            self.result.insert(END,str_price)
            
window=Tk()
window.title("Anjie\'s Pizza")
window.geometry("800x500") #WIDTH BY HEIGHT
app=Application(window)
app.mainloop()