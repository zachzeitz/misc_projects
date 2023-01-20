print("Reverse Add Sim Starting")

from tkinter import *

root = Tk()
root.configure(bg="#FFF300")
root.title("Reverse Addition Simulator")

num_1= Entry(root, borderwidth=5, width=35)
num_1.insert(0, "Enter First Number")
num_1.get()
num_1.grid(row=0,column=0,columnspan=1,padx=10,pady=10)


num_2= Entry(root, borderwidth=5, width=35)
num_2.insert(0, "Enter Second Number")
num_2.get()
num_2.grid(row=1, column=0, columnspan=1, padx=10, pady=10)


output_label = Label(root, text="Your Simulator Results Are: ")

def run_sim():
    sim = int(num_1.get()) - int(num_2.get())

    output_label["text"] = "Your Result is: " + str(sim)

button_1 = Button(root, text="Run Simulation", padx=50, pady=20, command= run_sim, bg="#FF00FF", fg="yellow").grid(row=3, column=0)
button_quit = Button(root, text="Close Simulator", command=root.quit, bg="#ed9121",fg="#f3f0f9").grid(row=5, column=0)

output_label.grid(row=4, column=0)

root.mainloop()
