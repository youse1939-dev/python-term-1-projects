from tkinter import *  
window = Tk()
window.geometry("600x400")

window.minsize(300,300)
window.maxsize(600,600)
window.title("Kanoon Project")


menuBar1=Menu(window)
window.config(menu=menuBar1)

lbl_name=Label(window,text="number 1",font="calibri 20")
lbl_name.pack()
lbl_name.place(x=100,y=10)
ent1=Entry(window,font='calibri 20')
ent1.pack()
ent1.place(x=230,y=10)

def save():
    print("save is clicked!")



file_menu=Menu(menuBar1)
menuBar1.add_cascade(label="file",menu=file_menu)
def show():
    print("hello its me")

file_menu.add_command(label="+",command=show)
file_menu.add_command(label="-",command=save)
file_menu.add_command(label="/")
file_menu.add_command(label="*")

setting_menu=Menu(menuBar1,tearoff=False)
menuBar1.add_cascade(label="setting",menu=setting_menu)
setting_menu.add_command(label="1")
setting_menu.add_separator()
setting_menu.add_command(label="2")
setting_menu.add_separator()
setting_menu.add_command(label="3")





window.mainloop()