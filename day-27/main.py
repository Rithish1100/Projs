from tkinter import*

def action():
    to_km=IntVar()
    to_km=int(input.get())*1.60934
    calc_label=Label(text=to_km,font=("Arial",16,"bold"))
    calc_label.grid(row=2,column=1)
    

window=Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

my_label=Label(text="Miles",font=("Arial",16,"bold"))
my_label.grid(row=1,column=2)


input=Entry(font=("Arial",10))
input.grid(row=1,column=1)
print(input.get())

my_label2=Label(text="Km",font=("Arial",16,"bold"))
my_label2.grid(row=2,column=2)

my_label3=Label(text=0,font=("Arial",16,"bold"))
my_label3.grid(row=2,column=1)

button = Button(text="Calculate", command=action)
button.grid(row=3,column=1)

my_label3=Label(text="is equal to",font=("Arial",16,"bold"))
my_label3.grid(row=2,column=0)

window.mainloop()
