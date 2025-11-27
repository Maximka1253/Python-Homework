from tkinter import *
import requests

root = Tk()

def get_weather():
    city = cityField.get()
    key = 'df90b50dc6d6065d7abf012f3d7a7e77'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={'df90b50dc6d6065d7abf012f3d7a7e77'}'
    params = {'APPID': key, 'q': city, 'units': 'imperial'}
    result = requests.get(url, params=params)
    weather = result.json()

    print(weather)

root['bg'] = '#fafafa'
root.title('Приложение для погоды')
root.geometry('600x550')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb334', bd = 5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.22)

frame_bottom = Frame(root, bg='#ffb334', bd = 5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Погодная информация', bg='#ffb334', font=40)
info.pack()

root.mainloop()