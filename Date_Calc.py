from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import date

window = Tk()
window.title('Kalkulator Umur by Arya Tamvan')
window.geometry('500x260+430+300')
window.resizable(height=FALSE, width=FALSE)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('Times New Roman', 14))

button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('Times New Roman', 16))

entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))

big_label = Label(window, text='KALKULATOR USIA', font=('Times New Roman', 25))
canvas.create_window(245, 40, window=big_label)

day_label = ttk.Label(window, text="Hari : ", style='TLabel')
day_entry = ttk.Entry(window, width=15, style='TEntry')

month_label = ttk.Label(window, text="Bulan : ", style='TLabel')
month_entry = ttk.Entry(window, width=15, style='TEntry')

year_label = ttk.Label(window, text="Tahun : ", style='TLabel')
year_entry = ttk.Entry(window, width=15, style='TEntry')



canvas.create_window(114, 100, window=day_label)
canvas.create_window(130, 130, window=day_entry)
canvas.create_window(250, 100, window=month_label)
canvas.create_window(245, 130, window=month_entry)
canvas.create_window(350, 100, window=year_label)
canvas.create_window(360, 130, window=year_entry)


def calculate_age():
    try:
        today = date.today()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birthdate = date(year, month, day)
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        age_result.config(text='Kamu Berumur ' + str(age) + ' Tahun')
    except:
        showerror(title='Error', message='Masalah Tidak Diketahui')

calculate_button = ttk.Button(window, text="Kalkulasi Usia", command=calculate_age)
age_result = ttk.Label(window, text='', style='TLabel')
canvas.create_window(245, 180, window=age_result)
canvas.create_window(245, 220, window=calculate_button)

window.mainloop()