from tkinter import *
from tkinter.ttk import *
import requests
from time import strftime

root = Tk()
root.title("Clock & Weather")

def time():
    current_time = strftime('%I:%M:%S %p')  # Change format to 12-hour
    label.config(text=current_time)
    label.after(1000, time)

def get_weather():
    city = city_entry.get()  # Get city from entry widget
    api_key = "4fbf1bf8875c2edf95fcb43d48fcff77"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        weather_data = response.json()
        weather_info = weather_data['weather'][0]['main']
        temperature = weather_data['main']['temp']
        weather_label.config(text=f"Weather: {weather_info}, Temperature: {temperature}°C")
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        weather_label.config(text="Error fetching weather data.")
    except KeyError:
        print("Invalid response from server.")
        weather_label.config(text="City not found.")
label = Label(root, font=("ds-digital", 80), background="black", foreground="red")
label.pack(anchor='center')

city_label = Label(root, text="Enter City:", font=("Arial", 16), background="black", foreground="white")
city_label.pack(anchor='s')

city_entry = Entry(root, font=("Arial", 16))
city_entry.pack(anchor='s')

search_button = Button(root, text="Search", command=get_weather)
search_button.pack(anchor='s', pady=10)

weather_label = Label(root, font=("Arial", 16), background="black", foreground="white")
weather_label.pack(anchor='s')

time()
get_weather()  # Initially fetch weather for default city

mainloop()
