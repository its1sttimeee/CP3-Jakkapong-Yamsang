from tkinter import *
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

b = BtcConverter()
b.get_latest_price('USD')

c = CurrencyRates()
c.get_rates('USD')

currency = c.get_rates('USD')

def click(event):
    amount = float(info.get())
    input_currency1 = input_currency.get()
    totalBTC = round(b.convert_to_btc(amount, input_currency1 ),2)

    totalBTC_output.configure(text=totalBTC)


def getcurrency_list(currency):
    currency_list = ['USD']
    for key in currency.keys():
        currency_list.append(key)
    return currency_list

currency_list = getcurrency_list(currency)

#Tk
mainwindow = Tk()
mainwindow.geometry('400x400')
#Header
label_header = Label(mainwindow, text= "โปรแกรมแปลงค่าเป็นสกุลBTC",font = ("Angsana New",17) )
label_header.grid(row = 0,columnspan=3,ipadx=15,ipady=15)

#Lebel
label_input = Label(mainwindow, text = "สกุลเงินต้นทาง",font=("Angsana New",12))
label_input.grid(row = 2 ,column= 0,padx=5,pady=5)
label_symbol2 = Label(mainwindow, text = "===>",font=("Angsana New",20))
label_symbol2.grid(row=4 ,column=1,padx=5 ,pady=5)
label_btc = Label(mainwindow, text = "สกุลBTC",font=("Angsana New",12))
label_btc.grid(row=2, column=2,padx=5,pady=5)

#choose Currency
input_currency = StringVar(mainwindow)
input_currency.set(currency_list[0])
dropdown_first_currency = OptionMenu(mainwindow, input_currency, *currency_list)
dropdown_first_currency.grid(row=3, column=0, padx=5, pady=10)

btc_button = StringVar(mainwindow)
btc_button.set("BTC")
dropdown_second_currency = OptionMenu(mainwindow, btc_button, "BTC")
dropdown_second_currency.grid(row=3,column =2,padx=5,pady=10)

#Receive info
info = Entry(mainwindow, justify=('center'))
info.grid(row = 4,column=0,padx=5,pady=5)

#Button
calculateButton = Button(mainwindow,text="Calculate",width=20)
calculateButton.grid(row=5, column=1)
calculateButton.bind('<Button-1>',click )

#Total
totalBTC_output = Label(mainwindow, text="ผลลัพธ์")
totalBTC_output.grid(row=4,column=2)


mainwindow.mainloop()