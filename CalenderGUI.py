from tkinter import *
import calendar
from datetime import date

def printCalender():
    month = int(month_box.get())
    year = int(year_box.get())
    output_calendar = calendar.month(year,month)
    calendar_field.delete(1.0,'end')
    calendar_field.insert('end',output_calendar)

def reset():
    calendar_field.delete(1.0,'end')
    month_var.set(current_month)
    year_var.set(current_year)
    month_box.config(textvariable=month_var)
    year_box.config(textvariable=year_var)

def close():
    guiWindow.destroy()

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("Calender")
    guiWindow.geometry('500x550')
    guiWindow.resizable(0,0)

    header_frame = Frame(guiWindow)
    entry_frame = Frame(guiWindow)
    result_frame = Frame(guiWindow)
    button_frame = Frame(guiWindow)

    header_frame.pack(expand=True,fill="both")
    entry_frame.pack(expand=True,fill="both")
    result_frame.pack(expand=True,fill="both")
    button_frame.pack(expand=True,fill="both")

    header_label = Label(header_frame,text="CALENDER", font=('arial',20,'bold'))
    header_label.pack(expand=True,fill="both")

    month_label = Label(entry_frame,text="Month", font=('arial',20,'bold'),fg='#000000')
    year_label = Label(entry_frame,text="YEAR", font=('arial',20,'bold'),fg='#000000')
    month_label.place(x=30,y=0)
    year_label.place(x=275,y=0)
    month_var = IntVar(entry_frame)
    year_var = IntVar(entry_frame)

    current_month = date.today().month
    current_year = date.today().year
    month_var.set(current_month)
    year_var.set(current_year)

    month_box = Spinbox(entry_frame, from_=1, to=12, width="10", textvariable=month_var, font=('arial',15))
    year_box = Spinbox(entry_frame, from_=0000, to=3000, width="10", textvariable=year_var, font=('arial',15))

    month_box.place(x=130,y=5)
    year_box.place(x=360,y=5)

    calendar_field = Text(result_frame, width=20, height=8, font=("courier",18), relief=RIDGE, borderwidth=2)
    calendar_field.pack()

    display_button = Button(button_frame, text="DISPLAY", bg="#A020F0", fg="#E0FFFF", command=printCalender, font=("arial",15))
    reset_button = Button(button_frame, text="RESET", bg="#A020F0", fg="#E0FFFF", command=reset, font=("arial",15))
    close_button = Button(button_frame, text="CLOSE", bg="#A020F0", fg="#E0FFFF", command=close, font=("arial",15))

    display_button.place(x=55,y=0)
    reset_button.place(x=210,y=0)
    close_button.place(x=350,y=0)

guiWindow.mainloop()