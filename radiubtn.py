from tkinter import *
from tkinter import ttk
window=Tk()
window.geometry("350x500")

def fun_btn1():
    a=var.get()
    n1=num1.get()
    n1=int(n1)
    n2=num2.get()
    n2=int(n2)

    if(a==1):
        print("گزینه ی 1 انتخاب شد ")

    a=var.get()
    if(a==2):
        print("گزینه ی 2 انتخاب شد ")    

  
    if(a==3):
        print("گزینه ی 3 انتخاب شد ")         

    if(a==4):
        print("گزینه ی 4 انتخاب شد ") 

var=IntVar()
R1=Radiobutton(window, text="inside", variable=var , value=1)
R1.pack()

R2=Radiobutton(window, text="outside ", variable=var , value=2)
R2.pack()

R3=Radiobutton(window, text="گزینه ی 3 ", variable=var , value=3)
R3.pack()

R4=Radiobutton(window, text="گزینه ی 4 ", variable=var , value=4)
R4.pack()




btn1=Button(window,text="add",command=fun_btn1)
btn1.pack()


combo = ttk.Combobox (window, Value=["+""/""-""*"] )
combo.pack()
combo.place()


           
window.mainloop()