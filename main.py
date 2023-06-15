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
disp = Entry(frame,font=("arial",16,'bold'),textvariable=input,width=100,justify="right")
disp.config(state="readonly",background="black")
disp.grid(row=0,column=0)
disp.pack(ipady=10)


window.mainloop()
