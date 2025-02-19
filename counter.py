import tkinter as tk


root=tk.Tk()

count=0
def counter():
    global count

    count+=1
    s=str(count)
    l.config(text=s)


l=tk.Label(root,fg="Red",bg="Cyan",width=10)
l.pack()
b=tk.Button(root,text="Press me",command=counter)
b.pack()
root.mainloop()
