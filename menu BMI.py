from tkinter import *  
window = Tk()
window.geometry("600x400")

window.minsize(300,300)
window.maxsize(600,600)
window.title("menu bmi")
window.iconbitmap()


#-----------------------------------------------------------------------------------------------------------------------------------

menuBar = Menu(window)
window.config(menu=menuBar)

file_menu = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="BMI", menu=file_menu)

help_menu = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="محدوده نرمال", menu=help_menu)

file2_menu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="کمبود و اضافه ", menu=file2_menu)

lbl_result=Label(window,font="calibri 20")
lbl_result.pack()
lbl_result.place(x=150, y=120)


lbl_kambood_vazn=Label(window,font="calibri 20")
lbl_kambood_vazn.pack()
lbl_kambood_vazn.place(x=350, y=270)

lbl_kambood=Label(window,font="calibri 20")
lbl_kambood.pack()
lbl_kambood.place(x=150, y=270)



lbl1=Label(window,font="calibri 20")
lbl1.pack()
ent1=Entry(window,font="calibri 20",width=6)
ent1.pack()

ent2=Entry(window,font="calibri 20",width=6)
ent2.pack()

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

def mhdode():
    height = float(ent1.get())

    min_weight = 20 * (height * height)
    max_weight = 25 * (height * height)

    lbl_result.config(
        text=f"Normal Weight:\n{min_weight:.2f} kg  -  {max_weight:.2f} kg"
    )

def kambood():

    height = float(ent1.get())
    weight = float(ent2.get())

    normal_weight = 20 * (height * height)

    shortage = normal_weight - weight

    if shortage > 0:
        lbl_kambood.config(text=shortage)
        lbl_kambood_vazn.config(text="کمبود وزن شما ")

    else:
        lbl_kambood.config(text="شما کمبود وزن ندارید ")

def ezafeh():

    height = float(ent1.get())
    weight = float(ent2.get())

    normal_weight = 25 * (height * height)

    extra_weight = weight - normal_weight

    if extra_weight < 25:
        lbl_kambood.config(text=extra_weight)
        lbl_kambood_vazn.config(text="اضافه وزن شما ")

    else:
        lbl_kambood.config(text="شما اضافه وزن ندارید ")        
           





file_menu.add_command(label="show",command=bmi)
help_menu.add_command(label= "حداقل و حداکثر وزن شما ",command=mhdode)
file2_menu.add_command(label="کمبود وزن شما",command=kambood)
file2_menu.add_command(label="اضافه وزن شما",command=ezafeh)







window.mainloop()