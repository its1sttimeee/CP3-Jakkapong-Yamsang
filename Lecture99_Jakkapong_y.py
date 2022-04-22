from tkinter import *
def calculateBMI(event):
    h = float(textbox_height.get())
    h = h/100
    w = float(textbox_wight.get())
    bmi = w / (h**2)
    bmi = round(bmi, 1)
    statlist = ["Under Weight","Normal Weight","Over Weight","Obesity"]
    stat = 0
    if bmi <= 18.5 :
        stat = statlist[0]
    elif bmi < 25 :
        stat = statlist[1]
    elif bmi < 30 :
        stat = statlist[2]
    else :
        stat = statlist[3]
    total.configure(text=stat)




window = Tk()
label_main = Label(window,text = "BMI Caculator",font=50,width=15 ).grid(row = 0, column=2)

label_height = Label(window, text = "Height (cm.)",font=20 ,width = 10).grid(row=1,column=1)
textbox_height = Entry(window, width=20)
textbox_height.grid(row=1,column=2)

label_wight = Label(window, text="Wight (kg.)",font=20, width=10).grid(row=2, column=1)
textbox_wight = Entry(window, width=20)
textbox_wight.grid(row=2, column=2)

calculateButton = Button(window,text="Check BMI")
calculateButton.grid(row=3, column=1)
calculateButton.bind('<Button-1>', calculateBMI)

total = Label(window, text="", font=20, width=15)
total.grid(row=3, column=2)

window.mainloop()
