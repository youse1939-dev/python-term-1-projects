from tkinter import *
window=Tk()
window.geometry("350x500")
window.title("calc")

window.minsize(400,400)
window.maxsize(600,600)

lbl1=Label(window,text="num1:",font="calabri 20")
lbl1.pack()
lbl1.place(x=50,y=10)


ent1=Entry(window,font="calibri 20",width=7)
ent1.pack()
ent1.place(x=250, y=10)


lbl2=Label(window,text="num2:",font="calabri 20")
lbl2.pack()
lbl2.place(x=50,y=60)



ent2=Entry(window,font="calibri 20",width=7)
ent2.pack()
ent2.place(x=250,y=60)




lbl_result = Label(window, text="Result:", font="calibri 20")
lbl_result.place(x=50, y=135)




def plus():
    num1 = int(ent1.get())
    num2 = int(ent2.get())

    res = num1 + num2

    lbl_result.config(text=f"Result: {res}")


def menha ():
    num1 = int(ent1.get())
    num2 = int(ent2.get())

    res = num1 - num2

    lbl_result.config(text=f"Result: {res}")    



def zarb ():
    num1 = int(ent1.get())
    num2 = int(ent2.get())

    res = num1 * num2

    lbl_result.config(text=f"Result: {res}")     


def taqsim ():
    num1 = int(ent1.get())
    num2 = int(ent2.get())

    res = num1 / num2

    lbl_result.config(text=f"Result: {res}") 




BTN=Button(window,text="+",font="calibri 20",command=plus)
BTN.pack()
BTN.place(x=50,y=250)



BTN=Button(window,text="-",font="calibri 20",command=menha)
BTN.pack()
BTN.place(x=130,y=250)


BTN=Button(window,text="*",font="calibri 20",command=zarb)
BTN.pack()
BTN.place(x=240,y=250)


BTN=Button(window,text="/",font="calibri 20",command=taqsim)
BTN.pack()
BTN.place(x=350,y=250)



window.mainloop()