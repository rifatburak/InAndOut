import tkinter as tk
import datetime
import csv

current_mount = datetime.datetime.now().month
current_year = datetime.datetime.now().year

#  This two function allow to the user pick just one checkbutton
def my_upd():
    ChkBttn_1.deselect()
    ChkBttn_2.select()


def my_upd_2():
    ChkBttn_2.deselect()
    ChkBttn_1.select()

# This function is for to work add button
def send():
    if btn_1.get() == 1:
        income_btn = True
    else:
        income_btn = False
    money = int(entry_money.get())
    statement = entry_statement.get()
    num_of_month = period.get()
    if income_btn and num_of_month == 1:
        data = [f'{current_mount}/{current_year}', money, 0, statement]
        with open('InAndOut.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    elif income_btn and num_of_month > 1:
        year_s = current_year
        for i in range(num_of_month):
            mounth_s = (current_mount + i) % 12
            if (current_mount + i) % 12 == 0:
                mounth_s = 12
            if (current_mount + i) % 12 == 1:
                year_s += 1
            data = [f'{mounth_s}/{year_s}', money, 0, statement]
            with open('InAndOut.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
    elif not income_btn and num_of_month == 1:
        data = [f'{current_mount}/{current_year}', 0, money, statement]
        with open('InAndOut.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    elif not income_btn and num_of_month > 1:
        year_s = current_year
        for i in range(num_of_month):
            mounth_s = (current_mount + i) % 12

            if (current_mount + i) % 12 == 0:
                mounth_s = 12
            if (current_mount + i) % 12 == 1:
                year_s += 1
            data = [f'{mounth_s}/{year_s}', 0, money, statement]
            with open('InAndOut.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)


# This part is for create a UserInterface and set the configurations
root = tk.Tk()
root.geometry('300x300')
root.wm_iconbitmap('money.ico')
root.title('InAndOut')
entry_money = tk.Entry()
entry_money.grid(column=1, row=0)
entry_statement = tk.Entry()
entry_statement.grid(column=1, row=1)
label_1 = tk.Label(text='Amount:')
label_1.grid(column=0, row=0)
label_2 = tk.Label(text='Statement:')
label_2.grid(column=0, row=1)
label_3 = tk.Label(text='Period (Monthly):')
label_3.grid(column=0, row=2)
period = tk.Scale(root, from_=1, to=12, orient='horizontal')
period.grid(column=1, row=2)
btn_1 = tk.IntVar(root)
btn_2 = tk.IntVar(root)
ChkBttn_1 = tk.Checkbutton(root, width=15, variable=btn_1, text='Income', command=my_upd_2)
ChkBttn_1.grid(column=0, row=3)
ChkBttn_1.select()
ChkBttn_2 = tk.Checkbutton(root, width=15, variable=btn_2, text='Outgoings', command=my_upd)
ChkBttn_2.grid(column=1, row=3)
button = tk.Button(text='       Add       ', command=send)
button.place(relx=0.5, rely=0.4, anchor='center')

root.mainloop()
