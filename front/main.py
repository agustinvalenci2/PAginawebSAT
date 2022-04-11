from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Consultant registration form")
heading = Label(text="Consultant registration",font="times 15 bold")
heading.grid(row=0,column=2)

general_fields = ["Full legal name","Country","State/Providence","City","Phone number"]
n_general = len(general_fields)
general_values = [StringVar for _ in range(n_general)]

label_text = Label(text="General",font="times 12 bold")
label_text.grid(row=1,column=0)

last_row_index=2

for i in range(n_general):
    label_text = Label(text=general_fields[i])
    label_text.grid(row=i+last_row_index,column=1)
    textbox = Entry(textvariable=general_values[i])
    textbox.grid(row=i+last_row_index,column=2)

last_row_index+=n_general
label_text = Label(text="Social Presence",font="times 12 bold")
label_text.grid(row=last_row_index,column=0)
last_row_index+=1

social_fields=["LinkedIn","Skype","Facebook","Twitter"]
n_social = len(social_fields)
social_values = [StringVar for _ in range(n_social)]

for i in range(n_social):
    label_text = Label(text=social_fields[i])
    label_text.grid(row=last_row_index+i,column=1)
    textbox = Entry(textvariable=social_values[i])
    textbox.grid(row=i+last_row_index,column=2)

window.mainloop()