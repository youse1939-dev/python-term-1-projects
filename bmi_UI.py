from tkinter import *
window=Tk()
window.geometry("450x450")
window.title("BMI")

window.minsize(400,400)
window.maxsize(600,600)

lbl1=Label(window,text="your height:",font="calabri 20")
lbl1.pack()
lbl1.place(x=50,y=10)


ent1=Entry(window,font="calibri 20",width=7)
ent1.pack()
ent1.place(x=250, y=10)


lbl2=Label(window,text="your weight:",font="calabri 20")
lbl2.pack()
lbl2.place(x=50,y=60)



ent2=Entry(window,font="calibri 20",width=7)
ent2.pack()
ent2.place(x=250,y=60)




lbl_result = Label(window, text="Result:", font="calibri 20")
lbl_result.place(x=50, y=135)




def bmi():
    height = float(ent1.get())
    weight = float(ent2.get())

    BMI = weight/(height*height)

    lbl_result.config(text=f"Result: {BMI}")
    if(BMI>25):
      lbl_comment= Label(window, text="you are overweighted", font="calibri 20")
      lbl_comment.place(x=50, y=200)

    if(BMI<20):
      lbl_comment= Label(window, text="you are undererweighted", font="calibri 20")
      lbl_comment.place(x=50, y=200)

    if(BMI>20 and BMI<25):
      lbl_comment= Label(window, text="you are normal", font="calibri 20")
      lbl_comment.place(x=50, y=200)    


BTN=Button(window,text="Show my BMI",font="calibri 20",command=bmi)
BTN.pack()
BTN.place(x=50,y=250)






window.mainloop()