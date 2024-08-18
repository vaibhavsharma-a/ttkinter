from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather Application")
root.iconbitmap(r"C:\Users\Asus\Downloads\cloud.ico")
root.geometry("600x250")

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=4ED775D8-41AC-4AC9-A217-7ED73578788A
def lookup():
  
  try:
    api_rqst = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_en.get() + "&distance=10&API_KEY=4ED775D8-41AC-4AC9-A217-7ED73578788A")

    api = json.loads(api_rqst.content)
    city = api[1]['ReportingArea']
    Quality = api[1]['AQI']
    category = api[1]['Category']['Name']

    if category == "Good":
      bg_clr = "#0C0"
    elif category == "Moderate":
      bg_clr = "#FFFF00"
    elif category == "Unhealty for Sensitive Groups":
      bg_clr = "#ff9900"
    elif category == "Unhealty":
      bg_clr = "#FF0000"
    elif category == "Very Unhealthy":
      bg_clr = "#990066"
    elif category == "Hazardous":
      bg_clr = "#660000"

    global weather_cat
    global weather_city
    global weather_qual

    root.configure(background=bg_clr)
    weather_city = Label(root,text="City : " + city,font=("Helvetica",20),background=bg_clr)
    weather_city.grid(row=2,column=0,columnspan=2)

    weather_qual = Label(root,text="AQI : " + str(Quality),font=("Helvetica",20),background=bg_clr)
    weather_qual.grid(row=3,column=0,columnspan=2)

    weather_cat = Label(root,text="Category : " + category,font=("Helvetica",20),background=bg_clr)
    weather_cat.grid(row=4,column=0,columnspan=2)
  except Exception as e:
    api = "Error..."

  

def cleanup():
  weather_cat.destroy()
  weather_city.destroy()
  weather_qual.destroy()
  root.configure(background="white")
  zip_en.delete(0,END)
  
zip_en = Entry(root,width=40)
zip_en.grid(row=0,column=1,padx=10)

lookup_btn = Button(root,text="Enter ZIP Code",command=lookup)
lookup_btn.grid(row=0,column=2,pady=5)

reset_bt = Button(root,text="Another code",command=cleanup)
reset_bt.grid(row=0,column=3,pady=5)


root.mainloop()