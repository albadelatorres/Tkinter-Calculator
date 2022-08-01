from tkinter import *
from tkinter import ttk
import re


# FUNCTIONS:

def inputnum(n):
    return n


# def sum(*args):
#     res = 0
#     for n in args:
#         res = res + n
#     return res
#
#
# def sub(*args):
#     res = 0
#     for n in args:
#         res = res - n
#     return res
#
#
# def mul(*args):
#     res = 1
#     for n in args:
#         res = res * n
#     return res
#
#
# def div(arg1, arg2):
#     return arg1 / arg2


def inputn(n):
    global expression
    expression = expression + str(n)
    number.set(expression)


def calculate(expr):
    rx = re.compile(r'\s*([+x÷-]|\d+)')
    factors = rx.findall(expr)
    list1= ""
    list1= expr.replace("x", "*")
    list1= list1.replace("÷", "/")

    number.set(eval(list1))

def clear():
    global expression
    expression = ""
    number.set("")

# Whole expression that will be calculated:
expression = ""

# MAIN WINDOW CONF:

# Main application window

root = Tk()
root.title("Calculator")

# Tells Tk that the frame should expand to fill extra space if
# window is resized

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Putting frame inside main window to ensure that the background
# is correct

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# CREATING WIDGETS:

# Entry for input number(s):

number = StringVar()
number_entry = Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=0, row=0, columnspan=3, sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))

# Buttons for numbers and operations
# NUMBERS:

num1 = StringVar()
ttk.Button(mainframe, text="1", command=lambda: inputn(1)).grid(column=0, row=1)
ttk.Button(mainframe, text="2", command=lambda: inputn(2)).grid(column=1, row=1)
ttk.Button(mainframe, text="3", command=lambda: inputn(3)).grid(column=2, row=1)
ttk.Button(mainframe, text="4", command=lambda: inputn(4)).grid(column=0, row=2)
ttk.Button(mainframe, text="5", command=lambda: inputn(5)).grid(column=1, row=2)
ttk.Button(mainframe, text="6", command=lambda: inputn(6)).grid(column=2, row=2)
ttk.Button(mainframe, text="7", command=lambda: inputn(7)).grid(column=0, row=3)
ttk.Button(mainframe, text="8", command=lambda: inputn(8)).grid(column=1, row=3)
ttk.Button(mainframe, text="9", command=lambda: inputn(9)).grid(column=2, row=3)
ttk.Button(mainframe, text="0", command=lambda: inputn(0)).grid(column=0, row=4)
ttk.Button(mainframe, text=".", command=lambda: inputn(".")).grid(column=1, row=4)

# OPERATIONS:

ttk.Button(mainframe, text="+", command=lambda: inputn('+')).grid(column=4, row=0)
ttk.Button(mainframe, text="-", command=lambda: inputn('-')).grid(column=4, row=1)
ttk.Button(mainframe, text="÷", command=lambda: inputn('÷')).grid(column=4, row=2)
ttk.Button(mainframe, text="x", command=lambda: inputn('x')).grid(column=4, row=3)
ttk.Button(mainframe, text="Calculate", command=lambda: calculate(expression)).grid(column=4, row=4)
ttk.Button(mainframe, text="Clear", command= lambda: clear()).grid(column=2, row=4)
# EXECUTES WINDOW:
root.mainloop()
