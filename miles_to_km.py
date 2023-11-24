from tkinter import *

def convert_mile_to_km():
    miles = int(input_text.get())
    km = round(miles * 1.60934, 2)
    label2.config(text= km)

#Window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500,height=250)
window.config(padx=30, pady=30)

#Entry
input_text = Entry(width=20)
input_text.grid(column=1, row=0)

#Label1
label1 = Label(text= "is equal to:",font=("Arial", 20))
label1.grid(column=0,row=1)

#Label2
label2 = Label(text= 0, font=("Arial", 20))
label2.grid(column=1, row=1)

#Button
button = Button(text="Calculate", font=("Arial", 20), command=convert_mile_to_km)
button.grid(column=1, row=2)

#Label3
label3 = Label(text="Miles", font=("Arial", 20))
label3.grid(column=2, row=0)

#Label4
label4 = Label(text="Km", font=("Arial", 20))
label4.grid(column=2, row=1)
    
window.mainloop()