from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=75e61c24870aafc3319b83573eb7b530"
    ).json()
    wc_label1.config(text=data["weather"][0]["main"])
    wd_label2.config(text=data["weather"][0]["description"])
    temp_label3.config(text=int(data["main"]["temp"] - 273.15))
    pr_label4.config(text=data["main"]["pressure"])
    hum_label5.config(text=data["main"]["humidity"])


win = Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("400x500")


name_label = Label(win, text="Sumit Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=10, y=50, height=50, width=380)

city_name = StringVar()
list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh ",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Lakshadweep",
    "National Capital Territory of Delhi",
    "Puducherry",
]
com = ttk.Combobox(
    win,
    text="Weather App",
    values=list_name,
    font=("Time New Roman", 15),
    textvariable=city_name,
)
com.place(x=50, y=120, height=35, width=300)

wc_label = Label(win, text="Weather Climate", font=("Time New Roman", 15))
wc_label.place(x=25, y=230, height=30, width=160)

wc_label1 = Label(win, text="", font=("Time New Roman", 15))
wc_label1.place(x=205, y=230, height=30, width=160)

wd_label = Label(win, text="Descriptions", font=("Time New Roman", 15))
wd_label.place(x=25, y=280, height=30, width=160)

wd_label2 = Label(win, text="", font=("Time New Roman", 15))
wd_label2.place(x=205, y=280, height=30, width=160)

temp_labe = Label(win, text="Temperature", font=("Time New Roman", 15))
temp_labe.place(x=25, y=330, height=30, width=160)

temp_label3 = Label(win, text="", font=("Time New Roman", 15))
temp_label3.place(x=205, y=330, height=30, width=160)

pr_label = Label(win, text="Pressure", font=("Time New Roman", 15))
pr_label.place(x=25, y=380, height=30, width=160)

pr_label4 = Label(win, text="", font=("Time New Roman", 15))
pr_label4.place(x=205, y=380, height=30, width=160)

hum_label = Label(win, text="Humidity", font=("Time New Roman", 15))
hum_label.place(x=25, y=430, height=30, width=160)

hum_label5 = Label(win, text="", font=("Time New Roman", 15))
hum_label5.place(x=205, y=430, height=30, width=160)

done_button = Button(
    win, text="Done", font=("Time New Roman", 15, "bold"), command=data_get
)
done_button.place(x=150, y=175, height=35, width=100)


win.mainloop()
