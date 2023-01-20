from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title("Number Guessing Game!")
root.iconbitmap("icon/download.ico")
root.geometry("300x400")
my_label=Label(root)
my_button=Button(root)

actual_num =random.randint(1,100)

def restart():
    global actual_num
    global my_label
    my_label.grid_remove()
    global my_button
    my_button.grid_remove()
    del actual_num
    actual_num = random.randint(1,100)



def submit():
    global user_guess
    global my_label
    global my_button
    
    user_guess= int(entry_label.get())
    global actual_num
    
    if user_guess > actual_num:
        my_label= Label(root, text="Too high")
        my_label.grid(row=3, column=0, pady=10, padx=85)
    if user_guess < actual_num:
        my_label= Label(root, text="Too low")
        my_label.grid(row=3, column=0, pady=10, padx=85)
    if user_guess == actual_num:
        my_label= Label(root, text="That's Right!")
        my_label.grid(row=3, column=0, pady=10, padx=85)
        my_button= Button(root, text= "Play Again?", command= restart)
        my_button.grid(row=5, column=0, columnspan=2,pady=10, padx=85)


Top_label = Label(root, text="Enter Number Between 1 and 100")
Top_label.grid(row=0, column=0,columnspan=2, pady=10)

#he grid, pack and place functions of the Entry object and of all other widgets returns None.
#In python when you do a().b(), the result of the expression is whatever b() returns,
#therefore Entry(...).grid(...) will return None.
#Splt them into two lines to avoid error
entry_label= Entry(root)
entry_label.grid(row=1, column=0, pady=10, padx=85)

sub_button= Button(root, text="Submit", command=submit).grid(row=2, column=0, pady=10, padx=85)

exit_button= Button(root, text="Close", command=root.destroy).grid(row=3, column=0, pady=10, padx=85)


mainloop()
