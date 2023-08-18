from tkinter import *
from tkinter import ttk

from currency_converter import CurrencyConverter
def change(amt,base_cur,dest_cur):
    
    c = CurrencyConverter()
    temp = c.convert(amt,base_cur,dest_cur)
    return temp


def Data():
    amount = Amt.get(1.0,END)
    base = base_cur.get()
    dest = dest_cur.get()
    final = change(amount,base,dest)
    result.insert(END,final)
    
def Clear():
    Amt.delete(1.0,END)
    result.delete(1.0,END)
    


root = Tk()
root.title("Translator")
root.geometry("500x500")
root.config(bg='#24fde6')
frame = Frame(root).pack(side=BOTTOM)
Lab_txt = Label(root,text="Currency Coverter",font=("Simplified Arabic Fixed",30,"bold"),bg='#24fde6') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt.place(x=50,y=40,height=50,width=412)

Lab_txt2 = Label(root,text="Amount: ",font=("Simplified Arabic Fixed",15,"bold"),bg='#24fde6') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt2.place(x=70,y=110,height=30,width=100)

Amt =Text(frame,font=("Time New Romen",10,"bold"),wrap=WORD)# It give source text to type with font style and size
Amt.place(x=180,y=110,height=25,width=200)

Lab_txt3 = Label(root,text="From: ",font=("Simplified Arabic Fixed",15,"bold"),bg='#24fde6') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt3.place(x=81,y=160,height=30,width=100)

currency_codes = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD",
    "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY",
    "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK",
    "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK",
    "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD",
    "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP",
    "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD",
    "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STN",
    "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
    "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND",
    "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW",
    "ZWD"
]


base_cur = ttk.Combobox(frame,value=currency_codes) #It is a option box with options
base_cur.place(x=180,y=160,height=25,width=200) # it refer where did it align
base_cur.set("Currency Code")

Lab_txt4 = Label(root,text="To: ",font=("Simplified Arabic Fixed",15,"bold"),bg='#24fde6') #This is Text with font colour,size and backgroung color and it like heading
Lab_txt4.place(x=90,y=210,height=30,width=100)

dest_cur = ttk.Combobox(frame,value=currency_codes) #It is a option box with options
dest_cur.place(x=180,y=210,height=25,width=200) # it refer where did it align
dest_cur.set("Currency Code")

Submit = Button(frame,text="Convert",relief=RAISED,bg='#f9fe82',font="bold",command=Data) # IT give button with name translate and give 3D animation
Submit.place(x=80,y=270,height=30,width=100)

Clear = Button(frame,text="Clear",relief=RAISED,bg='#f3763c',font="bold",command=Clear) # IT give button with name translate and give 3D animation
Clear.place(x=300,y=270,height=30,width=100)


result=Text(frame,font=("Time New Romen",30,"bold"),wrap=WORD,bg='#24fde6')# It give source text to type with font style and size
result.place(x=90,y=350,height=55,width=300)



root.mainloop()