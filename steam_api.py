from tkinter import *
import requests
import json
from tkinter import ttk

API_KEY="19C802CE0682478C92E4D978AAEC10A1"
root = Tk()
root.title("Using API Example")
root.geometry("550x800")
 
#create a main frame
main_frame= Frame(root)
main_frame.pack(fill=BOTH, expand=1)

#create a canvas
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT, fill= BOTH, expand=1)

#add a scrollbar to canvas
my_scrollbar= ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas
my_canvas.configure(yscrollcommand= my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#create another frame insie the canvas
second_frame= Frame(my_canvas)

#add that new frame to windo inisde the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

myLabel= Label(second_frame)
myLabel2= Label(second_frame)

names_list= []
percents_list= []

def id_lookup():
    global myLabel
    global myLabel2
    
    names_list.clear()
    percents_list.clear()
    
    #myLabel.destroy()
    #myLabel2.destroy()
    
    try:
        api_request = requests.get("http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid="+gameid_input.get()+"&format=json&API_KEY="+API_KEY)

        # No parenthesis after content, causes error to occur
        api = json.loads(api_request.content) #dictionary

        my_label=Label(second_frame, text="Achievements")
        my_label.grid(row=1, column=0, columnspan=1, sticky=W)
        my_label2=Label(second_frame, text="Percentage of Players Earned")
        my_label2.grid(row=1, column=1, columnspan=1, sticky=W)

        a= api['achievementpercentages']['achievements']
        
        names=[i["name"] for i in a]
        
        for x in range(len(names)):
           names_list.append(names[x])  

        for x in range(len(names_list)):
            myLabel =Label(second_frame, text=names_list[x], fg="blue")   
            myLabel.grid(row=x+2, column=0, columnspan=1, sticky=W)

        percents= [p["percent"] for p in a]
        
        for x in range(len(percents)):
           percents_list.append(percents[x])
        
        for x in range(0, len(percents_list)):
            myLabel2=Label(second_frame, text=percents_list[x], fg="purple")
            myLabel2.grid(row=x+2, column=1, columnspan=1)

    except Exception as e:
        api = "Error..."

    gameid_input.delete(0, END)

gameid_input = Entry(second_frame)
gameid_input.grid(row=0, column=0, stick=W+E+N+S)

id_button = Button(second_frame, text="Input App ID", command=id_lookup)
id_button.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()
