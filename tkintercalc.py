import tkinter
from tkinter import RIGHT, END
from math import pi
# variables
root = tkinter.Tk()
root.title('Calculator')
root.geometry('300x400')
root.resizable(0, 0)
# fonts
light_blue = "#819BFF"
dark_blue = "#0326B3"
blue = "#214DFF"
button_font = ('Arial', 18)
display_font = ('Arial', 30)

# functions


def submit_number(number):
    display.insert(END, number)


def operations(operator):
    global first_number
    global operation

    operation = operator
    first_number = display.get()

    display.delete(0, END)


def equal():
    # checking if number is valid, if valid then do the math, if error then value = error.
    if operation == 'add':
        try:
            value = float(first_number) + float(display.get())
        except:
            value = "ERROR"
    elif operation == 'subtract':
        try:
            value = float(first_number) - float(display.get())
        except:
            value = "ERROR"
    elif operation == 'multiply':
        try:
            value = float(first_number) * float(display.get())
        except:
            value = "ERROR"
    elif operation == 'divide':
        if display.get() == "0":
            value = "ERROR"
        else:
            try:
                value = float(first_number) / float(display.get())
            except:
                value = "ERROR"
    elif operation == 'exponent':
        try:
            value = float(first_number) ** float(display.get())
        except:
            value = "ERROR"

    display.delete(0, END)
    display.insert(0, value)


def clear():
    display.delete(0, END)


def square():
    try:
        value = float(display.get())**2
    except:
        value = "ERROR"

    display.delete(0, END)
    display.insert(0, value)

# gui
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=5)

display = tkinter.Entry(display_frame, width=50, font=display_font, bg=blue, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)
# configuring buttons
clear_button = tkinter.Button(button_frame, text="C", font=button_font, bg=dark_blue, command=clear)

square_button = tkinter.Button(button_frame, text='x^2', font=button_font, bg=light_blue, command=square)
exponent_button = tkinter.Button(button_frame, text='x^n', font=button_font, bg=light_blue, command=lambda:operations('exponent'))
divide_button = tkinter.Button(button_frame, text=' / ', font=button_font, bg=light_blue, command=lambda:operations('divide'))
multiply_button = tkinter.Button(button_frame, text='*', font=button_font, bg=light_blue, command=lambda:operations('multiply'))
subtract_button = tkinter.Button(button_frame, text='-', font=button_font, bg=light_blue, command=lambda:operations('subtract'))
add_button = tkinter.Button(button_frame, text='+', font=button_font, bg=light_blue, command=lambda:operations('add'))
equal_button = tkinter.Button(button_frame, text='=', font=button_font, bg=light_blue, command=equal)
decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg='black', fg='white', command=lambda:submit_number("."))
negative_button = tkinter.Button(button_frame, text="-", font=button_font, bg="black", fg="white", command=lambda:submit_number("-"))

nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg='black', fg='white', command=lambda:submit_number(9))
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg='black', fg='white', command=lambda:submit_number(8))
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg='black', fg='white', command=lambda:submit_number(7))
six_button = tkinter.Button(button_frame, text='6', font=button_font, bg='black', fg='white', command=lambda:submit_number(6))
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg='black', fg='white', command=lambda:submit_number(5))
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg='black', fg='white', command=lambda:submit_number(4))
three_button = tkinter.Button(button_frame, text='3', font=button_font, bg='black', fg='white', command=lambda:submit_number(3))
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg='black', fg='white', command=lambda:submit_number(2))
one_button = tkinter.Button(button_frame, text='1', font=button_font, bg='black', fg='white', command=lambda:submit_number(1))
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg='black', fg='white', command=lambda:submit_number(0))
pi_button = tkinter.Button(button_frame, text="π", font=button_font, bg=light_blue, command=lambda:submit_number(pi.__round__(6)))

# Packing Buttons
# First row
clear_button.grid(row=0, column=0, columnspan=4, pady=1, sticky="WE")
# Second row
pi_button.grid(row=1, column =0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")
# Third row (Add padding to create the size of the columns)
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)
# Fourth row
four_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
six_button.grid(row=3, column=2, pady=1, sticky="WE")
subtract_button.grid(row=3, column=3, pady=1, sticky="WE")
# Fifth row
one_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
three_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
# Sixth row
negative_button.grid(row=5, column=0, pady=1, sticky="WE")
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")

# running tkinter
root.mainloop()
