from tkinter import *
from PIL import Image,ImageTk
import requests
import keyboard
import json # javascript object notation
from urllib.request import Request, urlopen
from io import BytesIO
import os
import sys
import ctypes
import random

class Main:
    def __init__(self):
         self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
         for root, directories, files in os.walk(os.path.join(self.path)):
            self.self = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

         ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, random.choice(self.self)) , 0)


root = Tk()
root.title("Shib Generator")
#root.iconbitmap(r"icon/download.ico")
root.geometry("600x500")

label= Label(root)

def getshib():
    global img
    #label.destroy()
    try :
        api_request= requests.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrlstrue')
        api= json.loads(api_request.content)

        #print(api[0])

        req = Request(api[0], headers={'User-Agent': 'Mozilla/5.0'})
        resource = urlopen(req)
        output = open("img.jpg","wb")
        output.write(resource.read())
        output.close()

        #urllib.request.urlretrieve(api[0], "img.jpg")

        photo = Image.open("img.jpg")
        photo_resize= photo.resize((400,400))

        #photo.show()

        root.configure(bg="grey")

        img= ImageTk.PhotoImage(photo_resize)
        label= Label(root, image=img)
        label.grid(row=0, column=0)

        app= Main()

    except Exception as error:
        api= "Error..."

button= Button(root, text="Get Shib", command=getshib, bg= "#fcd612", fg= "#e6b9fb", font=("Comic Sans", 16))
keyboard.remap_key('space', 'p')
button.grid(row=1, column=0, pady=15, padx= 250)

mainloop()
