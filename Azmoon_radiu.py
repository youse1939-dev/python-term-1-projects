from tkinter import *

window = Tk()
window.geometry("350x500")
window.iconbitmap()

var1 = IntVar()
result_var = StringVar()

lbl1 = Label(window, text="کدام گزینه صحیح است؟", font="calibri 20")
lbl1.place(x=50, y=10)

R1 = Radiobutton(
    window,
    text="آقا محمدخان پس از مرگ کریم خان به خراسان برای دستیابی به غنائم نادر لشکرکشی کرد.",
    variable=var1,
    value=1
)
R1.pack()

R2 = Radiobutton(
    window,
    text="آقا محمدخان در شیراز تاج‌گذاری کرد اما تهران را پایتخت خود قرار داد.",
    variable=var1,
    value=2
)
R2.pack()

R3 = Radiobutton(
    window,
    text="آقا محمدخان در جریان لشکرکشی به قفقاز به قتل رسید.",
    variable=var1,
    value=3
)
R3.pack()

R4 = Radiobutton(
    window,
    text="آقا محمدخان کوچک‌ترین فرزند محمدحسین خان قاجار رئیس ایل قاجار بود.",
    variable=var1,
    value=4
)
R4.pack()


# ---------------- سوال 2 ----------------

lbl2 = Label(window, text="2- پایتخت حکومت آقامحمدخان قاجار کدام شهر بود؟", font="calibri 16")
lbl2.pack()

var2 = IntVar()

Radiobutton(window, text="اصفهان", variable=var2, value=1).pack()
Radiobutton(window, text="تبریز", variable=var2, value=2).pack()
Radiobutton(window, text="تهران", variable=var2, value=3).pack()   # صحیح
Radiobutton(window, text="شیراز", variable=var2, value=4).pack()


# ---------------- سوال 3 ----------------

lbl3 = Label(window, text="3- بنیان‌گذار سلسله قاجار چه کسی بود؟", font="calibri 16")
lbl3.pack()

var3 = IntVar()

Radiobutton(window, text="فتحعلی شاه", variable=var3, value=1).pack()
Radiobutton(window, text="آقامحمدخان قاجار", variable=var3, value=2).pack()   # صحیح
Radiobutton(window, text="ناصرالدین شاه", variable=var3, value=3).pack()
Radiobutton(window, text="کریم خان زند", variable=var3, value=4).pack()


# ---------------- سوال 4 ----------------

lbl4 = Label(window, text="4- آقامحمدخان به کدام سلسله پایان داد؟", font="calibri 16")
lbl4.pack()

var4 = IntVar()

Radiobutton(window, text="صفویه", variable=var4, value=1).pack()
Radiobutton(window, text="افشاریه", variable=var4, value=2).pack()
Radiobutton(window, text="زندیه", variable=var4, value=3).pack()   # صحیح
Radiobutton(window, text="پهلوی", variable=var4, value=4).pack()



# ---------------- سوال 5 ----------------

lbl5 = Label(window, text="5- آقامحمدخان در کدام شهر تاج‌گذاری کرد؟", font="calibri 16")
lbl5.pack()

var5 = IntVar()

Radiobutton(window, text="تهران", variable=var5, value=1).pack()
Radiobutton(window, text="تبریز", variable=var5, value=2).pack()
Radiobutton(window, text="شیراز", variable=var5, value=3).pack()
Radiobutton(window, text="ساری", variable=var5, value=4).pack()   # صحیح



# ---------------- سوال 6 ----------------

lbl6 = Label(window, text="6- آقامحمدخان در چه سالی به قتل رسید؟", font="calibri 16")
lbl6.pack()

var6 = IntVar()

Radiobutton(window, text="۱۲۰۹ هجری قمری", variable=var6, value=1).pack()
Radiobutton(window, text="۱۲۱۲ هجری قمری", variable=var6, value=2).pack()
Radiobutton(window, text="۱۲۱۱ هجری قمری", variable=var6, value=3).pack()
Radiobutton(window, text="۱۲۱۰ هجری قمری", variable=var6, value=4).pack()   # صحیح


# ---------------- سوال 7 ----------------

lbl7 = Label(window, text="7- پس از آقامحمدخان چه کسی به سلطنت رسید؟", font="calibri 16")
lbl7.pack()

var7 = IntVar()

Radiobutton(window, text="ناصرالدین شاه", variable=var7, value=1).pack()
Radiobutton(window, text="فتحعلی شاه", variable=var7, value=2).pack()   # صحیح
Radiobutton(window, text="محمدشاه", variable=var7, value=3).pack()
Radiobutton(window, text="رضاشاه", variable=var7, value=4).pack()

# ---------------- سوال 8 ----------------

lbl8 = Label(window, text="8- آقامحمدخان بیشتر برای چه کاری شناخته می‌شود؟", font="calibri 16")
lbl8.pack()

var8 = IntVar()

Radiobutton(window, text="تأسیس سلسله قاجار و یکپارچه کردن کشور", variable=var8, value=1).pack()   # صحیح
Radiobutton(window, text="تأسیس دانشگاه تهران", variable=var8, value=2).pack()
Radiobutton(window, text="امضای قرارداد گلستان", variable=var8, value=3).pack()
Radiobutton(window, text="نهضت مشروطه", variable=var8, value=4).pack()


# ---------------- سوال 9 ----------------

lbl9 = Label(window, text="9- آقامحمدخان از کدام ایل بود؟", font="calibri 16")
lbl9.pack()

var9 = IntVar()

Radiobutton(window, text="بختیاری", variable=var9, value=1).pack()
Radiobutton(window, text="قاجار", variable=var9, value=2).pack()   # صحیح
Radiobutton(window, text="قشقایی", variable=var9, value=3).pack()
Radiobutton(window, text="کرد", variable=var9, value=4).pack()






def add():
    correct = 0
    wrong = 0
    empty = 0

    if var1.get() == 0:
        empty += 1

    elif var1.get() == 3:   # جواب صحیح سؤال سوم است
        correct += 1

    else:
        wrong += 1

    result_var.set(
        f"Correct: {correct}\nWrong: {wrong}\nEmpty: {empty}"
    )


lbl_result = Label(window, textvariable=result_var, font="calibri 16")
lbl_result.pack(pady=20)

btn1 = Button(window, text="Check", command=add)
btn1.pack()

window.mainloop()