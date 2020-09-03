from tkinter import *

root = Tk()
root.title("Simple Calculator!") 
root.geometry("400x450")
root.configure(bg = "cyan")

e = Entry(root, width = 30, borderwidth = 5)
e.grid(row=0, column = 0, columnspan = 3, padx=5, pady=10)


def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	global first
	first_num = e.get()
	first = int(first_num)
	global s
	s = '+'
	e.delete(0,END)

def button_equal():
	second = e.get()
	e.delete(0,END)
	if s == '+':
		e.insert(0, first + int(second))
	if s == '-':
		e.insert(0, first - int(second))
	if s == '*':
		e.insert(0, first * int(second))
	if s == '/':
		e.insert(0, first / int(second))

def button_subtract():
	global first
	first_num = e.get()
	first = int(first_num)
	global s
	s = '-'
	e.delete(0, END)

def button_multiply():
	global first
	first_num = e.get()
	first = int(first_num)
	global s
	s = '*'
	e.delete(0, END)

def button_divide():
	global first
	first_num = e.get()
	first = int(first_num)
	global s
	s = '/'
	e.delete(0, END)

button_1 = Button(root, text = "1", padx=10, pady= 10, highlightbackground = "cyan", command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx=10, pady= 40, highlightbackground = "cyan",command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx=10, pady= 40, highlightbackground = "cyan",command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx=10, pady= 40, highlightbackground = "cyan",command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx=10, pady= 20, highlightbackground = "cyan",command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx=10, pady= 20, highlightbackground = "cyan",command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx=10, pady= 20, highlightbackground = "cyan",command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx=10, pady= 20, highlightbackground = "cyan",command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx=10, pady= 20, highlightbackground = "cyan",command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx=10, pady= 20, highlightbackground = "cyan",command = lambda: button_click(0))

button_add = Button(root, text = "+", padx=40, pady= 20, highlightbackground = "#ffcccb",command = button_add)
button_equal = Button(root, text = "=", padx=40, pady= 20, highlightbackground = "#ffcccb",command = button_equal)
button_clear = Button(root, text = "C", padx=40, pady= 20, highlightbackground = '#ffcccb', command =  button_clear)

button_subtract = Button(root, text = "-", padx=40, pady= 20, highlightbackground = "#ffcccb",command = button_subtract)
button_multiply = Button(root, text = "*", padx=40, pady= 20, highlightbackground = "#ffcccb",command = button_multiply)
button_divide = Button(root, text = "/", padx=40, pady= 20, highlightbackground = "#ffcccb",command = button_divide)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row = 4, column = 0)
button_clear.grid(row = 3, column = 3)
button_equal.grid(row = 4, column = 3)

button_subtract.grid(row = 4, column = 2)
button_multiply.grid(row = 1, column = 3)
button_divide.grid(row = 2, column = 3)







root.mainloop()

