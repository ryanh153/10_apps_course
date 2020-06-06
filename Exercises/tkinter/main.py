import tkinter as tk


window = tk.Tk()


def convert():
    grams = str(float(e1_value.get())*1000)
    t1.insert(tk.END, grams)
    pounds = str(float(e1_value.get()) * 2.20462)
    t2.insert(tk.END, pounds)
    ounces = str(float(e1_value.get()) * 35.274)
    t3.insert(tk.END, ounces)


e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=0)

e2 = tk.Label(window, text='kg')
e2.grid(row=0, column=1)

b1 = tk.Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)

t1 = tk.Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = tk.Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = tk.Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()