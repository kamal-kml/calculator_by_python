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


clear = Button(btnframe,width=10,height=4,text="C")
clear.grid(row=0,column=0,padx=2,pady=2)

posorneg = Button(btnframe,width=10,height=4,text="+/-")
posorneg.grid(row=0,column=1,padx=2,pady=2)

mod = Button(btnframe,width=10,height=4,text="%")
mod.grid(row=0,column=2,padx=2,pady=2)

div = Button(btnframe,width=10,height=4,text="/")
div.grid(row=0,column=3,padx=2,pady=2)

window.mainloop()
