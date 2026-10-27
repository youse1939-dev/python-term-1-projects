from tkinter import *
window=Tk()
window.geometry("500x500")
def fun_next():
    win_next=Tk()
    win_next.geometry("300x300")
    lbl1=Label(win_next,text="متن شما",font="calibri 20")
    lbl1.pack()
    lbl1.place(x=100,y=100)
    
    def fun_exit():
       win_next.destroy()
    
    btn_exit=Button(win_next,text="exit",font="calibri 20",command=fun_exit)
    btn_exit.pack()
    btn_exit.place(x=100,y=200)
    win_next.mainloop()

btn1=Button(window,text="صفحه بعد",font="calibri 20",command=fun_next)
btn1.pack()
btn1.place(x=200,y=250)
window.mainloop()
  

