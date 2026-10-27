from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("500x500")
window.title("bmi and bmr")


lbl1 = Label(window, text="chose what you want", font="calabri 20")
lbl1.pack()
lbl1.place(x=150, y=10)


def fun_next():

    win_next = Tk()
    win_next.title("calculater")
    win_next.geometry("450x450")


    lbl1 = Label(win_next, text="your height:", font="calabri 20")
    lbl1.pack()
    lbl1.place(x=50, y=10)


    ent1 = Entry(win_next, font="calibri 20", width=7)
    ent1.pack()
    ent1.place(x=250, y=10)


    lbl2 = Label(win_next, text="your weight:", font="calabri 20")
    lbl2.pack()
    lbl2.place(x=50, y=60)


    ent2 = Entry(win_next, font="calibri 20", width=7)
    ent2.pack()
    ent2.place(x=250, y=60)


    lbl_result = Label(win_next, text="Result:", font="calibri 20")
    lbl_result.place(x=50, y=135)


    def bmi():

        height = float(ent1.get())
        weight = float(ent2.get())

        BMI = weight / (height * height)

        lbl_result.config(text=f"Result: {BMI}")

        if BMI > 25:
            lbl_comment = Label(
                win_next,
                text="you are overweighted",
                font="calibri 20"
            )
            lbl_comment.place(x=50, y=200)

        if BMI < 20:
            lbl_comment = Label(
                win_next,
                text="you are undererweighted",
                font="calibri 20"
            )
            lbl_comment.place(x=50, y=200)

        if BMI > 20 and BMI < 25:
            lbl_comment = Label(
                win_next,
                text="you are normal",
                font="calibri 20"
            )
            lbl_comment.place(x=50, y=200)


    BTN = Button(
        win_next,
        text="Show my BMI",
        font="calibri 20",
        command=bmi
    )
    BTN.pack()
    BTN.place(x=50, y=250)





def b_next():

    win_next2 = Tk()
    win_next2.title("calculater")
    win_next2.geometry("470x450")

    combo = ttk.Combobox(win_next2, font="calibri 20")
    combo["values"] = (
        "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25"
    )
    combo.place(x=150, y=120)

    lbl1 = Label(
        win_next2,
        text="your height:",
        font="calabri 20"
    )
    lbl1.place(x=50, y=10)

    ent1 = Entry(
        win_next2,
        font="calibri 20",
        width=7
    )
    ent1.place(x=250, y=10)

    lbl2 = Label(
        win_next2,
        text="your weight:",
        font="calabri 20"
    )
    lbl2.place(x=50, y=60)

    ent2 = Entry(
        win_next2,
        font="calibri 20",
        width=7
    )
    ent2.place(x=250, y=60)

    lbl_result = Label(
        win_next2,
        text="Result:",
        font="calibri 20"
    )
    lbl_result.place(x=80, y=390)

   
    var = IntVar(win_next2)

    zan = Radiobutton(
        win_next2,
        text="women",
        variable=var,
        value=1
    )
    zan.place(x=70, y=340)

    mard = Radiobutton(
        win_next2,
        text="men",
        variable=var,
        value=2
    )
    mard.place(x=170, y=340)

    lbl_c = Label(
        win_next2,
        font="calibri 20",
        text="age"
    )
    lbl_c.place(x=50, y=120)

    def bmr():

        height = float(ent1.get())
        weight = float(ent2.get())

        age = int(combo.get())
        gender = var.get()
        print("Gender:", gender)
        print("Age:", age)

        if gender == 1:
            BMR = 10 * weight + 6.25 * height - 5 * age - 161

        elif gender == 2:
            BMR = 10 * weight + 6.25 * height - 5 * age + 5

        else:
            lbl_result.config(
                text="Please choose your gender"
            )
            return

        lbl_result.config(
            text=f"Result: {BMR:.2f}"
        )

    BTN = Button(
        win_next2,
        text="Show my BMR",
        font="calibri 20",
        command=bmr
    )
    BTN.place(x=50, y=250)







BTN1 = Button(
    window,
    text="BMI",
    font="calibri 20",
    command=fun_next
)
BTN1.pack()
BTN1.place(x=200, y=250)


BTN2 = Button(
    window,
    text="BMR",
    font="calibri 20",
    command=b_next
)
BTN2.pack()
BTN2.place(x=200, y=350)


window.mainloop()