from tkinter import *
from time import strftime
from datetime import datetime

root = Tk()
root.geometry("370x510")
root.resizable(0,0)
root.title('HourGlass')


root.attributes('-alpha',0.85)

bg = PhotoImage(file="pic5.png")
icon=PhotoImage(file="hour.png")
root.iconphoto(False,icon)

label=Label(root,image=bg)
label.place(x=0,y=0,relwidth=1,relheight=1)

def clock():
    string = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, clock)

    today = datetime.now()
    current_date_time = today.strftime("%A %d %B")

    date_label.config(text=current_date_time)

def alarm():
    alarmWindow = Toplevel(root)


time_label=Label(root,font=('arial',36,'normal'),pady=60,foreground='white',bg="black")
date_label=Label(root,font=('arial',17,'normal'),pady=10,fg="white",bg="black")
time_label.pack(anchor='n')
date_label.pack(anchor='n')

clock()
root.mainloop()

