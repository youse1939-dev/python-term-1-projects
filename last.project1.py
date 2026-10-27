from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("last project1")




lbl1=Label(window,text="press the buttun",font="calabri 20")
lbl1.pack()
lbl1.place(x=150,y=10)







def fun_next():
 win_next=Tk()
 win_next.title("calculater")
 win_next.geometry("300x300")

 ent1=Entry(win_next,font="calibri 20",width=7)
 ent1.pack()
 ent1.place(x=30, y=50)

 ent2=Entry(win_next,font="calibri 20",width=7)
 ent2.pack()
 ent2.place(x=160, y=50)

 lbl7=Label(win_next ,font="calibri 20",text="result:")
 lbl7.place(x=30,y=230)

 lable6=Label(win_next,font="calibri 20")
 lable6.place(x=130,y=230)

 def jam():
 
  num1=int(ent1.get())
  num2=int(ent2.get())
  result=num1+num2
  lbl_resul.config(text=result)
  lable6.config(text=result)

 BTN2=Button(win_next,text="+",font="calibri 20",command=jam)
 BTN2.pack()
 BTN2.place(x=130,y=150)

 lbl_resul=Label(font="calibri 20")
 lbl_resul.place(x=130,y=130)

 lbl7=Label(font="calibri 20",text="result:")
 lbl7.place(x=30,y=130)


 




BTN=Button(window,text="?????",font="calibri 20",command=fun_next)
BTN.pack()
BTN.place(x=200,y=250)






window.mainloop()