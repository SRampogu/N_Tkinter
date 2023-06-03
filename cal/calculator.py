import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Calculator")
#root.geometry("600x600")

e=Entry(root, width=45, borderwidth=5)
e.grid(row=0,column=0, columnspan=3,padx=10,pady=10)



def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        
def button_clear():
         e.delete(0, END)

def button_add():
        first= e.get()
        global f_num
        global maths
        maths = 'add'
        f_num = int(first)
        e.delete(0, END)

def button_equal():
        second_number=e.get()
        e.delete(0, END)
        
        if maths =="add":
                e.insert(0, f_num+int(second_number))
        if maths =="mul":
                e.insert(0, f_num * int(second_number))
        if maths =="sub":
                e.insert(0, f_num - int(second_number))
        if maths =="div":
                e.insert(0, f_num / int(second_number))
       
def button_mul():
         first= e.get()
         global f_num
         global maths
         maths = 'mul'
         f_num = int(first)
         e.delete(0, END)
 #-----------------------------------------------       
def button_sub():
        first= e.get()
        global f_num
        global maths
        maths = 'sub'
        f_num = int(first)
        e.delete(0, END)

def button_div():
        first= e.get()
        global f_num
        global maths
        maths = 'div'
        f_num = int(first)
        e.delete(0, END)




b_1 = Button(root,text = "1", padx=40, pady=20, command= lambda: button_click(1),bg="pink", font = 15)
b_2 = Button(root,text = "2", padx=40, pady=20, command= lambda: button_click(2),bg="pink", font = 15)
b_3 = Button(root,text = "3", padx=40, pady=20, command=lambda: button_click(3),bg="pink", font = 15)
b_4 = Button(root,text = "4", padx=40, pady=20, command=lambda: button_click(4),bg="pink", font = 15)
b_5 = Button(root,text = "5", padx=40, pady=20, command=lambda: button_click(5),bg="pink", font = 15)
b_6 = Button(root,text = "6", padx=40, pady=20, command=lambda: button_click(6),bg="pink", font = 15)
b_7 = Button(root,text = "7", padx=40, pady=20, command=lambda: button_click(7),bg="pink", font = 15)
b_8 = Button(root,text = "8", padx=40, pady=20, command=lambda: button_click(8),bg="pink", font = 15)
b_9 = Button(root,text = "9", padx=40, pady=20, command=lambda: button_click(9),bg="pink", font = 15)
b_0 = Button(root,text = "0", padx=40, pady=20, command=lambda: button_click(0),bg='#8ed49f', font = 15)

b_add = Button(root,text = "+", padx=40, pady=20, command=button_add,bg='#8ed49f')
b_equal = Button(root,text = "=", padx=42, pady=20, command= button_equal,bg='#8ed49f')

b_mul = Button(root,text = "X", padx=39, pady=20, command=button_mul,bg='#8ed49f', font = 15)
b_sub = Button(root,text = "-", padx=40, pady=20, command=button_sub,bg="#8ed49f", font = 15)
b_div = Button(root,text = "/", padx=40, pady=20, command= button_div,bg='#8ed49f', font = 15)

b_clear = Button(root,text = "CLEAR", padx=120, pady=20, command=button_clear,bg="coral",font = 15)

#grid
b_1.grid(row=3, column=0)
b_2.grid(row=3, column=1)
b_3.grid(row=3, column=2)

b_4.grid(row=2, column=0)
b_5.grid(row=2, column=1)
b_6.grid(row=2, column=2)


b_7.grid(row=1, column=0)
b_8.grid(row=1, column=1)
b_9.grid(row=1, column=2)


b_0.grid(row=4, column=0)

b_add.grid(row=4, column=2)
b_equal.grid(row=4, column=1)

b_mul.grid(row=5, column=0)
b_sub.grid(row=5, column=1)
b_div.grid(row=5, column=2)

b_clear.grid(row=6,column=0,columnspan=3)

# icon
root.iconphoto(False, tkinter.PhotoImage(file="py.png"))

root.mainloop()
