from tkinter import*

root = Tk()
#Title
root.title("Simple Calculator")
#Functions
def click():
    Get = input.get()
    return

def add():
    return

def clear():
    return

def sub():
    return

def equal():
    return
input = Entry(root,width=130)
input.grid(row =0,column = 0,columnspan=8)

#Buttons
btn_1=Button(root,text="1",padx=147,pady=25,command=click)
btn_1.grid(row=1,column=0)

btn_2=Button(root,text="2",padx=135,pady=25,command=click)
btn_2.grid(row=1,column=1)

btn_3=Button(root,text="3",padx=135,pady=25,command=click)
btn_3.grid(row=1,column=2)

btn_4=Button(root,text="4",padx=147,pady=25,command=click)
btn_4.grid(row=2,column=0)

btn_5=Button(root,text="5",padx=135,pady=25,command=click)
btn_5.grid(row=2,column=1)

btn_6=Button(root,text="6",padx=135,pady=25,command=click)
btn_6.grid(row=2,column=2)

btn_7=Button(root,text="7",padx=147,pady=25,command=click)
btn_7.grid(row=3,column=0)

btn_8=Button(root,text="8",padx=135,pady=25,command=click)
btn_8.grid(row=3,column=1)

btn_9=Button(root,text="9",padx=135,pady=25,command=click)
btn_9.grid(row=3,column=2)

btn_0=Button(root,text="0",padx=135,pady=25,command=click)
btn_0.grid(row=4,column=2)

#Add Button
btn_add=Button(root,text="+",padx=135,pady=25,command=add)
btn_add.grid(row=4,column=1)

#Clear
btn_clear=Button(root,text="AC",padx=130,pady=25, command=clear)
btn_clear.grid(row=4, column=0)

#sub Button
btn_add=Button(root,text="-",padx=155,pady=25,command=sub)
btn_add.grid(row=5,column=0)

#Equal
btn_equal=Button(root,text="=",padx=135,pady=25, command=equal)
btn_equal.grid(row=5,column=1)

root.mainloop() 
