from tkinter import *
from PIL import ImageTk,Image
from numpy import array
import os

root = Tk()
root.title("Mad Libs Input")
root.iconbitmap("icon/download.ico")
root.geometry("350x400")

user_entries= []

S_entries= ["Last Name", "Small Town Name", "Man's Name", "Blue Collar Job Title", "Relative", "Type of Accident",
            "Strange Occurance", "Synonym For Creepy", "Childs Name", "Strange Occurance", "Emotion",
            "Strange Occurance", "Weird Loner's Name"]

T_entries = ["Man's Name", "Famous Actor", "Occupation", "Number", "Obscure Japanese Movie", "Verb", "Body Part",
               "Verb", "Noun", "Obscure Movie Title", "Cool Old Car", "Man's Name", "Very Famous Actor",
               "Older Tarantino Movie", "Obscure Movie Title", "Adjective", "Verb", "Body Part", "Nouns",
               "Obscure Movie Title"]

user_input = ["Mans Name", "Occupation", "Noun", "Noun", "Noun", "Shape", "Verb", "Body Part",
                   "Womans Name", "Verb", "Noun", "Restaurant", "Noun", "Historical Monument", "Verb", "Noun",
                   "Noun", "Noun", "Noun", "Verb", "Adjective", "Adjective", "Emotion", "Verb",
                   "Noun", "Verb", "Noun"]

def submit():
    top = Toplevel()
    top.title("Mad Libs")
    top.geometry("870x410")
    top.configure(bg= "#727200")
    top.iconbitmap("icon/download.ico")
    global entry_list
    global director
    entry_list = ''

    output_label= Label(top, text='', font=('Comic Sans MS', 14, 'italic'), fg="#0093AF", bg="#727200")
    output_label.grid(row=1, column=0)

    for entries in user_entries:
       entry_list = entry_list + " " +str(entries.get())

    entry_list= entry_list.split()

    if director == "Bay":
       output_label.config(text=str(entry_list[0]) + " is a normal " + str(entry_list[1]) + ". Then, one day, a " + str(entry_list[2]) + '\n'
       " explodes, causing a " + str(entry_list[3]) + " to blow up, and a nearby " + str(entry_list[4]) + " erupts into a" + str(entry_list[5]) + '\n'
       " of flames." + entry_list[0] + " realizes that he's being chased by the government, who's trying to\n"
       + str(entry_list[6]) + " him. While on the run, he teams up with an incredibly attractive woman named " + str(entry_list[7]) + '\n'
       ", who has an incredible" + str(entry_list[8]) + ". She may be from the streets, but she can " + str(entry_list[9]) + "like\n"
       " nobodies business. The duo decide to turn the tables on their pursuers by blowing up a " + str(entry_list[10]) + '\n'
       ", which triggers a chain reaction, causing the local " + str(entry_list[11]) + "," + str(entry_list[12]) + ", and the\n"
       + str(entry_list[13]) + " to explode. Then, the bad guys' helicopter gets " + str(entry_list[14]) + " by a piece of " + str(entry_list[15]) + '\n'
       " from when the " + str(entry_list[16]) + " exploded, and the helicopter explodes and falls onto a " + str(entry_list[17]) + "causing\n"
       " it to " + str(entry_list[18]) + " which shoots a fireball straight into the heart of " + str(entry_list[19]) + " and destroys\n"
       " the bad guy leader. Everything is "+ str(entry_list[20]) + " and the two decide that such a(n) " + str(entry_list[21]) + '\n'
       " ordeal has caused them to fall in" + str(entry_list[22]) + " with each other. They decide to celebrate by\n"
       + str(entry_list[23]) +"ing on the " + str(entry_list[24]) + ", and they even managed to use a " + str(entry_list[25]) + " from the\n"
       " beginning of the movie, to " + str(entry_list[26]) + " the whole story together.")

    elif director == "Tarantino":
        output_label.config(text=str(entry_list[0]) + " is a very suave guy played by " + str(entry_list[1]) + "." + '\n'
        " He's done some bad stuff, but he's very cool. He has a long conversation with a " + str(entry_list[2]) + ", in which he makes\n"
        + str(entry_list[3]) + "references to a classic hollywood film that was based on the obscure japanese film " + str(entry_list[4]) + '\n'
        ", then he kills him very violently by " + str(entry_list[5]) + "ing him in the " + str(entry_list[6]) + "and then\n"
        + str(entry_list[7]) + "ing his " + str(entry_list[8]) + "off. After making another really great reference to\n"
        + str(entry_list[9]) +", he drives a " + str(entry_list[10]) + " to the home of " + str(entry_list[11]) + ',\n'
        " who is played by " + str(entry_list[12]) + ". They have a very long, wordy, sharp-tongued conversation in which\n"
        " the cinemetography references " + str(entry_list[13]) + " and the dialogue is a homage to " + str(entry_list[14]) + '\n'
        ", and then they get into a very bloody, " + str(entry_list[15])+ " fight in which they" + str(entry_list[16]) + '\n'
        " each other's " + str(entry_list[17]) + " with " + str(entry_list[18]) + " and talk about " + str(entry_list[19]) + " for\n"
        " a really long time, before one or both of them die in a really artsy and dramatic fashion.")

    elif director == "Shyamalan":
        output_label.config(text="The " + str(entry_list[0]) + " family lives on a farm in " + str(entry_list[1]) + " Pennsylvania. \n"
        + str(entry_list[2]) + " is a former " + str(entry_list[3]) + " who lost his " + str(entry_list[4]) + " in a \n"
        + str(entry_list[5]) + ". But soon a " + str(entry_list[6]) + " begins to happen. The only other person who undertands \n"
        "what is going on is a " + str(entry_list[7]) + " child. He and " + str(entry_list[8]) + " begin to uncover clues \n"
        "about the " + str(entry_list[9]) + ", and it continues to get more awkard and uncomfortable but the child helps \n"
        "give him " + str(entry_list[10]) + ". The two work to get to the bottom of the " + str(entry_list[11]) + ". Then \n"
        "when it seems unsolvable, " + str(entry_list[12]) + " (played by M. Night Shyamalan) shows up to explain what's going on.")

def bay_submit():
        input = Toplevel()
        input.title("Mad Libs")
        input.geometry("300x810")
        input.iconbitmap("icon/download.ico")
        input.configure(bg="#00008B")
        global director
        director= "Bay"


        for x in range(len(user_input)):
            my_label= Label(input, text= user_input[x], bg= "#ff007f" , fg= "#000033")
            my_label.grid(row=x, column=0, sticky=W)
            my_entry = Entry(input)
            my_entry.grid(row=x, column=1, pady=5, padx=5)
            user_entries.append(my_entry)

        submit_button = Button(input,text="Create Mad Lib", font= ('Comic Sans MS', 14, 'bold italic'), fg="#ff007f", bg="#ccff00", command= submit)
        submit_button.grid(row=27, column=1, columnspan=2)

def tarantino_submit():
    input = Toplevel()
    input.title("Mad Libs")
    input.geometry("350x650")
    input.iconbitmap("icon/download.ico")
    input.configure(bg="#00008B")
    global director
    director= "Tarantino"

    for x in range(len(T_entries)):
        my_label= Label(input, text= T_entries[x],  bg= "#ff007f" , fg= "#000033")
        my_label.grid(row=x, column=0, sticky=W)
        my_entry = Entry(input)
        my_entry.grid(row=x, column=1, pady=5, padx=5)
        user_entries.append(my_entry)

    submit_button = Button(input,text="Create Mad Lib", font= ('Comic Sans MS', 14, 'bold italic'), fg="#ff007f", bg="#ccff00", command= submit)
    submit_button.grid(row=20, column=1, columnspan=2, pady=20)

def shyamalan_submit():
        input = Toplevel()
        input.title("Mad Libs")
        input.geometry("350x650")
        input.iconbitmap("icon/download.ico")
        input.configure(bg="#00008B")
        global director
        director= "Shyamalan"

        for x in range(len(S_entries)):
            my_label= Label(input, text= T_entries[x],  bg= "#ff007f" , fg= "#000033")
            my_label.grid(row=x, column=0, sticky=W)
            my_entry = Entry(input)
            my_entry.grid(row=x, column=1, pady=5, padx=5)
            user_entries.append(my_entry)

        submit_button = Button(input,text="Create Mad Lib", font= ('Comic Sans MS', 14, 'bold italic'), fg="#ff007f", bg="#ccff00", command= submit)
        submit_button.grid(row=20, column=1, columnspan=2, pady=20)


bay_button= Button(root, text="Michael Bay",command=bay_submit)
bay_button.grid(row=1, column=0, padx=130, pady=5)

tarantino_button= Button(root, text="Quentin Tarantino", command=tarantino_submit)
tarantino_button.grid(row=2, column=0, padx=130, pady=5)

shyamalan_button= Button(root, text= "M. Night Shyamalan", command= shyamalan_submit)
shyamalan_button.grid(row=3, column=0, padx=130, pady=5)

exit_button= Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=6, column=0, columnspan=2, pady=20)

mainloop()
