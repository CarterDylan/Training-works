
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
