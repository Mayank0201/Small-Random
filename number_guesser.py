import tkinter as tk
import random as r

root = tk.Tk()
root.title("Number Guessing Game")

c = r.randint(1, 10)

root.geometry("200x200")
def fun():
    global c

    a = int(e.get())

    if a < 1 or a > 10:
        l.config(text="Please enter a valid number (1-10)", fg="black", bg="red")
    elif a == c:
        l.config(text="Correct!Now try your luck with another one", fg="black", bg="green")
        c = r.randint(1, 10)
    elif a > c:
        l.config(text="Go lower!", fg="black", bg="blue")
    else:
        l.config(text="Go higher!", fg="black", bg="red")

    e.delete(0, tk.END)

e = tk.Entry(root)
e.pack()

b = tk.Button(root, text="Press me", command=fun)
b.pack()

l = tk.Label(root, text="Guess a number between 1 and 10")
l.pack()

root.mainloop()
