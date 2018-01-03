# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:55:59 2018

@author: dcarter
"""

# Calculate Miles Per Gallon
#requires user input for how many gallons used and miles driven
print("This program calculates mpg.")
miles_driven = float(input("Enter miles driven:"))
gallons_used = float(input("Enter gallons used:"))
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)


#This calculates the area of a trapezoid, based on the bottom and top bases and height
height = float(input("Enter the height of the trapezoid: "))
bottom_length = float(input("Enter the Length of the bottom base: "))
top_length = float(input("Enter the Length of the top base: "))
area = (0.5 * (bottom_length + top_length)) * height
print (area)

#creates a pop up box asking for yes or no, which can be used by the user.
from tkinter import Tk, Label, Button, Radiobutton, IntVar
#    ^ Use capital T here if using Python 2.7

def ask_multiple_choice_question(prompt, options):
    root = Tk()
    if prompt:
        Label(root, text=prompt).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    if v.get() == 0: return None
    return options[v.get()]

result = ask_multiple_choice_question(
    "What do you want to convert to? ",
    [
        "None",
        "Farenheit",
        "Celsius"
    ]
)
#convert to celsius
if result == "Celsius":
    farenheit = float(input("Enter temperture in fahrenheit: "))
    celsius = farenheit - 32 * 1.8
    print("The temperture in celsius is", celsius)
#convert to farenheit
elif result == "Farenheit":
    celsius = float(input("Enter temperture in celsius: "))
    farenheit = celsius * 1.8 + 32
    print("The temperture in Farenheit is ", farenheit)
#neither    
else:
    quit()