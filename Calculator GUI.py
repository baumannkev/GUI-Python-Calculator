##KEVIN BAUMANN NERY HUERTA
#300298836
#GUI PROJECT
#CALCULATOR

from tkinter import *
import math
import tkinter.messagebox
window = Tk()
window.title("Calculator")

window.configure(bg = '#342aa1')

frame = Frame(window, padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

label = Label(frame,text = "Simple Calculator", width = 20, height = 1, bg="light blue")
label.place(x=5, y = 90)

e = Entry(frame, width = 46, borderwidth = 5, justify = RIGHT)
e.grid(row = 1, column = 1, columnspan = 3, padx = 10, pady= 10)



def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

#Assing number to the button with a value = lambda
button_1 = Button(frame, text = "1", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(1))
button_2 = Button(frame, text = "2", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(2))
button_3 = Button(frame, text = "3", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(3))
button_4 = Button(frame, text = "4", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(4))
button_5 = Button(frame, text = "5", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(5))
button_6 = Button(frame, text = "6", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(6))
button_7 = Button(frame, text = "7", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(7))
button_8 = Button(frame, text = "8", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(8))
button_9 = Button(frame, text = "9", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(9))
button_0 = Button(frame, text = "0", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(0))
button_add = Button(frame, text = "+", bg = "#2188f0", borderwidth = 5, padx = 40, pady = 20, command =button_add)
button_equal = Button(frame, text = "=",bg = "#2188f0", borderwidth = 5, padx = 40, pady = 20, command =button_equal)
button_clear = Button(frame, text = "clear",bg = "#2188f0", borderwidth = 5, padx = 30, pady = 20, command =button_clear)

button_multiply = Button(frame, text= "x", bg = "#2188f0", borderwidth = 5, padx = 40, pady= 20, command = button_multiply)
button_divide = Button(frame, text= "/", bg = "#2188f0", borderwidth = 5, padx = 40, pady= 20, command = button_divide)
button_subtract = Button(frame, text= "-", bg = "#2188f0", borderwidth = 5, padx =40 , pady= 20, command = button_subtract)


#put the buttons on the screen
button_clear.grid(row=8, column =3)

button_1.grid(row =6, column=0)
button_2.grid(row =6, column=1)
button_3.grid(row =6, column=2)

button_4.grid(row =5, column=0)
button_5.grid(row =5, column=1)
button_6.grid(row =5, column=2)

button_7.grid(row =4, column=0)
button_8.grid(row =4, column=1)
button_9.grid(row =4, column=2)

button_0.grid(row =7, column=1)

button_divide.grid(row=3,column=3)
button_multiply.grid(row=4,column=3)
button_subtract.grid(row=5,column=3)
button_add.grid(row =6, column= 3)
button_equal.grid(row = 7, column= 3)

button_close = Button(frame, text = "close", command = window.destroy)
button_close.grid(row = 8,column = 0)

######################################################################################


def open():

    
    top = Toplevel()
    top.title("Calculator")
    top.configure(bg = '#342aa1')
  

    frame = Frame(top, padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)
    
    label = Label(frame,text = "Advanced Calculator", width = 20, height = 1, bg="light blue")
    label.place(x=5, y = 90)

    e = Entry(frame, width = 46, borderwidth = 5, justify = RIGHT)
    e.grid(row = 1, column = 1, columnspan = 3, padx = 10, pady= 10)



    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)

    def button_squareroot():
        first_number = e.get()
        global f_num
        global math
        math = "squareroot"
        f_num = int(first_number)
        e.delete(0, END)

    def button_square():
        first_number = e.get()
        global f_num
        global math
        math = "square"
        f_num = int(first_number)
        e.delete(0,END)

    def button_euler():
        first_number = e.get()
        global f_num
        global math
        math = "e"
        f_num = int(first_number)
        e.delete(0,END)
        
    def button_equal():
        second_number = e.get()
        e.delete(0, END)
        
        if math == "squareroot":
            e.insert(0, f_num ** (1/2))
        if math == "e":
            e.insert(0, 2.718281828459045 ** f_num)
        if math == "square":
            e.insert(0, f_num ** 2)

    #Assing number to the button with a value = lambda
    button_1 = Button(frame, text = "1", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(1))
    button_2 = Button(frame, text = "2", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(2))
    button_3 = Button(frame, text = "3", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(3))
    button_4 = Button(frame, text = "4", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(4))
    button_5 = Button(frame, text = "5", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(5))
    button_6 = Button(frame, text = "6", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(6))
    button_7 = Button(frame, text = "7", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(7))
    button_8 = Button(frame, text = "8", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(8))
    button_9 = Button(frame, text = "9", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(9))
    button_0 = Button(frame, text = "0", bg = '#6fa5eb', borderwidth = 5, padx = 40, pady = 20, command= lambda: button_click(0))
    button_pi = Button(frame, text= "π", bg = "#2188f0", borderwidth = 5, padx = 40, pady= 20, command = lambda: button_click(3.14159265359))
    
    button_squareroot = Button(frame, text = "√", bg = "#2188f0", borderwidth = 5, padx = 40, pady = 20, command =button_squareroot)
    button_equal = Button(frame, text = "=",bg = "#2188f0", borderwidth = 5, padx = 40, pady = 20, command =button_equal)
    button_clear = Button(frame, text = "clear",bg = "#2188f0", borderwidth = 5, padx = 30, pady = 20, command =button_clear)
    button_square = Button(frame, text= "a²", bg = "#2188f0", borderwidth = 5, padx = 40, pady= 20, command = button_square)
    button_euler = Button(frame, text= "e", bg = "#2188f0", borderwidth = 5, padx =40 , pady= 20, command = button_euler)


    #put the buttons on the screen
    button_clear.grid(row=8, column =3)

    button_1.grid(row =6, column=0)
    button_2.grid(row =6, column=1)
    button_3.grid(row =6, column=2)

    button_4.grid(row =5, column=0)
    button_5.grid(row =5, column=1)
    button_6.grid(row =5, column=2)

    button_7.grid(row =4, column=0)
    button_8.grid(row =4, column=1)
    button_9.grid(row =4, column=2)

    button_0.grid(row =7, column=1)

    button_square.grid(row=3,column=3)
    button_pi.grid(row=4,column=3)
    button_euler.grid(row=5,column=3)
    button_squareroot.grid(row =6, column= 3)
    button_equal.grid(row = 7, column= 3)

    button_close = Button(frame, text = "close", command = top.destroy)
    button_close.grid(row = 8,column = 0)
    
button = Button(frame, text = "Advanced", command = open).grid(row = 0, column = 0)

#################################################################################################3


def jokes():
    joke = Toplevel()
    joke.title("Calculator")
    joke.configure(bg = '#342aa1')


    frame = Frame(joke, padx = 5, pady = 5)
    frame.pack(padx = 10, pady = 10)
    
    label = Label(frame,text = "Math Jokes :)", width = 20, height = 1, bg="light blue")
    label.place(x=5, y = 90)

    joke.choice = IntVar()
    joke.rb1 = Radiobutton(frame, text = "Why should you never talk to Pi?",variable = joke.choice, value = 1, command = joke.clicked1)

    def clicked1():
        tkinter.messagebox.show.info("Because she’ll go on and on and on forever.")

    
    
    Radiobutton(frame, text= "Why should you never talk to Pi?", variable = r, value= 1, command = clicked(r.get())).pack()
    Radiobutton2(frame, text= "Why should you ", variable = r, value= 2, command = clicked(r.get())).pack()
    
button2 = Button(frame, text = "Math Jokes", command = jokes).grid(row = 0, column = 1)  
window.mainloop()

