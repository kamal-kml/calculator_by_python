from tkinter import *

window = Tk()
window.geometry("321x411")
window.resizable(0,0)
window.title("CALC BY KAMAL")

def update_display(text):
    input.set(text)


def btn_equal():
    try:
        result = eval(input.get())
        update_display(str(result))
    except Exception as e:
        update_display("Error")

def btn_click(item):
    global expression


def btn_clr():
    global expression


def btn_mod():
    global expression


def btn_posorneg():
    global expression


expression=""
input = StringVar()

#input frame
frame = Frame(window,height=60,width=320,bg="black")
frame.pack(side=TOP)

#display
disp = Entry(frame,font=("arial",16),textvariable=input,width=60,justify="right")
disp.config(state="readonly")
disp.grid(row=0,column=0)
disp.pack(ipady=10)

#buttons

btnframe = Frame(window,width=318,height=350,bg="#415a77")
btnframe.pack()

#row 1
clear = Button(btnframe,width=10,height=4,text="C",command=lambda : btn_clr())
clear.grid(row=0,column=0,padx=1,pady=1)

posorneg = Button(btnframe,width=10,height=4,text="+/-",command=lambda : btn_posorneg())
posorneg.grid(row=0,column=1,padx=1,pady=1)

mod = Button(btnframe,width=10,height=4,text="%",command=lambda :btn_mod())
mod.grid(row=0,column=2,padx=1,pady=1)

div = Button(btnframe,width=10,height=4,text="/",command=lambda : btn_click("/"))
div.grid(row=0,column=3,padx=1,pady=1)


# row=2

seven = Button(btnframe,width=10,height=4,text="7",command=lambda : btn_click("7"))
seven.grid(row=1,column=0,padx=1,pady=1)

eight = Button(btnframe,width=10,height=4,text="8",command=lambda : btn_click("8"))
eight.grid(row=1,column=1,padx=1,pady=1)

nine = Button(btnframe,width=10,height=4,text="9",command=lambda : btn_click("9"))
nine.grid(row=1,column=2,padx=1,pady=1)

mul = Button(btnframe,width=10,height=4,text="*",command=lambda : btn_click("*"))
mul.grid(row=1,column=3,padx=1,pady=1)



# row 3

four = Button(btnframe,width=10,height=4,text="4",command=lambda : btn_click("4"))
four.grid(row=2,column=0,padx=1,pady=1)

five = Button(btnframe,width=10,height=4,text="5",command=lambda : btn_click("5"))
five.grid(row=2,column=1,padx=1,pady=1)

six = Button(btnframe,width=10,height=4,text="6",command=lambda : btn_click("6"))
six.grid(row=2,column=2,padx=1,pady=1)

sub = Button(btnframe,width=10,height=4,text="-",command=lambda : btn_click("-"))
sub.grid(row=2,column=3,padx=1,pady=1)

# row 4

one = Button(btnframe,width=10,height=4,text="1",command=lambda : btn_click("1"))
one.grid(row=3,column=0,padx=1,pady=1)

two = Button(btnframe,width=10,height=4,text="2",command=lambda : btn_click("2"))
two.grid(row=3,column=1,padx=1,pady=1)

three = Button(btnframe,width=10,height=4,text="3",command=lambda : btn_click("3"))
three.grid(row=3,column=2,padx=1,pady=1)

add = Button(btnframe,width=10,height=4,text="+",command=lambda : btn_click("+"))
add.grid(row=3,column=3,padx=1,pady=1)

# row 5

zero = Button(btnframe,width=22,height=4,text="0",command=lambda : btn_click("0"))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)

dot = Button(btnframe,width=10,height=4,text=".",command=lambda : btn_click("."))
dot.grid(row=4,column=2,padx=1,pady=1)

equal = Button(btnframe,width=10,height=4,text="=",command=lambda :btn_equal())
equal.grid(row=4,column=3,padx=1,pady=1)



window.mainloop()

