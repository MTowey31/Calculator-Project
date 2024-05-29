import tkinter as tk
window = tk.Tk()
window.title("Calculator")

output_string = tk.StringVar()
output_string.set("d")
first_number = ""
second_number = ""
operator_clicked = False
operator_string = ""

def change(item):
    global first_number
    global second_number
    global operator_clicked
    global operator_string
    global output_string
    if not operator_clicked:
        first_number += item
        output_string.set(first_number)
    else:
        second_number += item
        output_string.set(first_number + operator_string + second_numner)



button1 = tk.Button(text="C", width=10, height=5)
button1.grid(row=0, column=0)

button2 = tk.Button(text="()", width=10, height=5)
button2.grid(row=0, column=1)

button3 = tk.Button(text="%", width=10, height=5)
button3.grid(row=0, column=2)

button4 = tk.Button(text="/", width=10, height=5, command=lambda: change("/"))
button4.grid(row=0, column=3)

button5 = tk.Button(window, text="7", width=10, height=5, command=lambda: change("7"))
button5.grid(row=1, column=0)

button6 = tk.Button(window, text="8", width=10, height=5, command=lambda: change("8"))
button6.grid(row=1, column=1)

button7 = tk.Button(text="9", width=10, height=5, command=lambda: change("9"))
button7.grid(row=1, column=2)

button8 = tk.Button(text="*", width=10, height=5, command=lambda: change("*"))
button8.grid(row=1, column=3)

button9 = tk.Button(text="4", width=10, height=5, command=lambda: change("4"))
button9.grid(row=2, column=0)

button10 = tk.Button(text="5", width=10, height=5, command=lambda: change("5"))
button10.grid(row=2, column=1)

button11 = tk.Button(text="6", width=10, height=5, command=lambda: change("6"))
button11.grid(row=2, column=2)

button12 = tk.Button(text="-", width=10, height=5, command=lambda: change("-"))
button12.grid(row=2, column=3)

button13 = tk.Button(text="1", width=10, height=5, command=lambda: change("1"))
button13.grid(row=3, column=0)

button14 = tk.Button(text="2", width=10, height=5, command=lambda: change("2"))
button14.grid(row=3, column=1)

button15 = tk.Button(text="3", width=10, height=5, command=lambda: change("3"))
button15.grid(row=3, column=2)

button15 = tk.Button(text="+", width=10, height=5, command=lambda: change("+"))
button15.grid(row=3, column=3)

output_string = tk.Label(window, textvariable=output_string)
output_string.grid(row=4, column=0, columnspan=2)

button18 = tk.Button(text="0", width=10, height=5)
button18.grid(row=4, column=2)

button19 = tk.Button(text="=", width=10, height=5)
button19.grid(row=4, column=3)


window.mainloop()
