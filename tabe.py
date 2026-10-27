from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("form")


l1 = Label(window, text="نام:", font="calibri 20")
l1.place(x=50, y=20) 
l90= Label(window,text="amiryousef",font='calibri 20')
l90.place(x=100, y=20)


l2 = Label(window, text="نام خانوادگی:", font="calibri 20",justify=LEFT)
l2.place(x=50, y=80) # 
l100=Label(window,text="elmi",font="calibri 20")
l100.place(x=200, y=80)


l3 = Label(window, text="نام پدر:", font="calibri 20")          
l3.place(x=50, y=140) # 
l50=Label(window,text="Amir",font="calibri 20")
l50.place(x=150, y=140)


l4 = Label(window, text="مقطع تحصیلی:", font="calibri 20")
l4.place(x=50, y=200) # 
l70=Label(window,text="8 grade",font="calibri 20")
l70.place(x=230, y=200)

window.mainloop()
    