from tkinter import *
window=Tk()
window.geometry("600x600")
window.title("garden")

window.minsize(400,400)
window.maxsize(600,600)


lbl1=Label(window,text="نام:",font="calabri 20")
lbl1.pack()
lbl1.place(x=50,y=10)




def show3():
    lbl2=Label(window,text="امیریوسف",font="calabri 20")
    lbl2.pack()
    lbl2.place(x=200,y=10)




lbl1=Label(window,text="نام پدر :",font="calabri 20")
lbl1.pack()
lbl1.place(x=50,y=50)




def show1():
    lbl2=Label(window,text="امیر",font="calabri 20")
    lbl2.pack()
    lbl2.place(x=200,y=50)


lbl1=Label(window,text="مقطع تحصیلی:",font="calabri 20")
lbl1.pack()
lbl1.place(x=50,y=100)




def show():
    lbl2=Label(window,text="نهم",font="calabri 20")
    lbl2.pack()
    lbl2.place(x=200,y=100)



    


BTN=Button(window,text="مقطع تحصیلی",font="calibri 20",command=show)
BTN.pack()
BTN.place(x=50,y=250)

BTN=Button(window,text="نام پدر ",font="calibri 20",command=show1)
BTN.pack()
BTN.place(x=320,y=250)

BTN=Button(window,text="نام",font="calibri 20",command=show3)
BTN.pack()
BTN.place(x=430,y=250)




window.mainloop()