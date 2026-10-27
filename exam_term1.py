

from tkinter import *
from tkinter import ttk
window=Tk()
window.geometry("700x450")



food_var = StringVar()   
drink_var = StringVar()  
var = IntVar()          
result_var = StringVar()


lbl1=Label(window,text="name:",font="calibri 20")
lbl1.pack()
lbl1.place(x=50,y=10)


ent1=Entry(window,font="calibri 20",width=7)
ent1.pack()
ent1.place(x=250, y=10)


lbl2=Label(window,text="phone number:",font="calabri 20")
lbl2.pack()
lbl2.place(x=50,y=60)



ent2=Entry(window,font="calibri 20",width=7)
ent2.pack()
ent2.place(x=250,y=60)



lbl3 = Label(window, text="food:", font="calibri 20")
lbl3.place(x=50, y=120)


combo_food = ttk.Combobox(window, font="calibri 20", textvariable=food_var, values=["Pizza", "Burger", "potato"])
combo_food.place(x=250, y=120)
combo_food.current(0)

R1 = Radiobutton(window, text="inside", variable=var, value=0)
R1.place(x=50, y=270)

R2 = Radiobutton(window, text="outside", variable=var, value=50)
R2.place(x=150, y=270)


lbl4 = Label(window, text="drink:", font="calibri 20")
lbl4.place(x=50, y=170)


combo2 = ttk.Combobox(window, font="calibri 20", textvariable=drink_var, values=["soda", "water", "beer"])
combo2.place(x=250, y=170)
combo2.current(0)


lbl_result = Label(window, textvariable=result_var, font="calibri 20")
lbl_result.place(x=170, y=340)


prices = {
    "Pizza": 100, "Burger": 80, "potato": 50,  
    "soda": 20, "water": 10, "beer": 30        
}



def apply():
   
    food_name = food_var.get()
    drink_name = drink_var.get()
    
 
    food_price = prices[food_name]
    drink_price = prices[drink_name]
    
    
   
    total = food_price + drink_price + var.get() 
    
    
    


    result_var.set(f"Total: {total}")





BTN=Button(window,text="apply",font="calibri 20",command=apply)
BTN.pack()
BTN.place(x=50,y=340)


window.mainloop()