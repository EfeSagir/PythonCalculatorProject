import utilities
from tkinter import *

root = Tk() #Tk() creates main window

global addition_number_count, substraction_number_count, multiplication_number_count, division_number_count, f_num

e = Entry(root, width = 20, bg = "blue", fg = "yellow", borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_addition():
    global addition_number_count, substraction_number_count, multiplication_number_count, division_number_count, f_num
    addition_number_count = 1
    substraction_number_count = 0
    multiplication_number_count = 0
    division_number_count = 0

    first_number = e.get()
    f_num = first_number
    e.delete(0, END)

def button_substraction():

    global addition_number_count, substraction_number_count, multiplication_number_count, division_number_count, f_num
    addition_number_count = 0
    substraction_number_count = 1
    multiplication_number_count = 0
    division_number_count = 0

    first_number = e.get()

    if first_number == "" or first_number == "-":
        first_number = "0"
    f_num = first_number
    e.delete(0, END)

def button_multiplication():
    global addition_number_count, substraction_number_count, multiplication_number_count, division_number_count, f_num
    addition_number_count = 0
    substraction_number_count = 0
    multiplication_number_count = 1
    division_number_count = 0

    first_number = e.get()
    f_num = first_number
    e.delete(0, END)


def button_division():
    global addition_number_count, substraction_number_count, multiplication_number_count, division_number_count, f_num
    addition_number_count = 0
    substraction_number_count = 0
    multiplication_number_count = 0
    division_number_count = 1


    first_number = e.get()
    f_num = first_number
    e.delete(0, END)


def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    if(addition_number_count == 1):
        e.insert(0, float(f_num) + float(second_number))
    elif(substraction_number_count ==1):
        e.insert(0, float(f_num) - float(second_number))
    elif (multiplication_number_count == 1):
        e.insert(0, float(f_num) * float(second_number))
    elif (division_number_count == 1):
        e.insert(0, float(f_num) / float(second_number))

button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))

button_plus = Button(root, text = "+", padx = 40, pady = 20, command = button_addition)
button_minus = Button(root, text = "-", padx = 40, pady = 20, command = button_substraction)
button_star = Button(root, text = "*", padx = 40, pady = 20, command =button_multiplication)
button_slash = Button(root, text = "/", padx = 40, pady = 20, command = button_division)
button_equation = Button(root, text = "=", padx = 40, pady = 20, command = button_equal)

button_clear = Button(root, text ="CLEAR", padx = 23, pady = 20, command =button_clear)

button_0.grid(row=5, column=1)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_plus.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_star.grid(row=4, column=3)
button_slash.grid(row=5, column=3)
button_equation.grid(row=5, column=2)
button_clear.grid(row=5, column= 0)

root.mainloop()
