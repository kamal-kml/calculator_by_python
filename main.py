from tkinter import *

window = Tk()
window.geometry("320x400")
window.resizable(0,0)
window.title("CALC BY KAMAL")

input = StringVar()

#input frame
frame = Frame(window,height=60,width=320,bg="black")
frame.pack(side=TOP)

#display
disp = Entry(frame,font=("arial",16,'bold'),textvariable=input,width=60,justify="right")
disp.config(state="readonly")
disp.grid(row=0,column=0)
disp.pack(ipady=10)

#buttons

btnframe = Frame(window,width=318,height=350,bg="#415a77")
btnframe.pack()

#row 1
clear = Button(btnframe,width=10,height=4,text="C")
clear.grid(row=0,column=0,padx=1,pady=1)

posorneg = Button(btnframe,width=10,height=4,text="+/-")
posorneg.grid(row=0,column=1,padx=1,pady=1)

mod = Button(btnframe,width=10,height=4,text="%")
mod.grid(row=0,column=2,padx=1,pady=1)

div = Button(btnframe,width=10,height=4,text="/")
div.grid(row=0,column=3,padx=1,pady=1)

# row=2

seven = Button(btnframe,width=10,height=4,text="7")
seven.grid(row=1,column=0,padx=1,pady=1)

eight = Button(btnframe,width=10,height=4,text="8")
eight.grid(row=1,column=1,padx=1,pady=1)

nine = Button(btnframe,width=10,height=4,text="9")
nine.grid(row=1,column=2,padx=1,pady=1)

mul = Button(btnframe,width=10,height=4,text="*")
mul.grid(row=1,column=3,padx=1,pady=1)



# row 3

four = Button(btnframe,width=10,height=4,text="4")
four.grid(row=2,column=0)

five = Button(btnframe,width=10,height=4,text="5")
five.grid(row=2,column=1)

six = Button(btnframe,width=10,height=4,text="6")
six.grid(row=2,column=2)

sub = Button(btnframe,width=10,height=4,text="-")
sub.grid(row=2,column=3)

window.mainloop()

